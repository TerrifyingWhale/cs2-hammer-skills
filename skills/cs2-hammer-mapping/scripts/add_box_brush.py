#!/usr/bin/env python3
"""Insert axis-aligned box brushes (world CMapMesh) into a CS2 .vmap text file.

Usage:
    python add_box_brush.py <input.txt> <output.txt> <boxes.json> [--material <vmat>] [--node-start <int>]

    input.txt    keyvalues2 text of the .vmap (from dmxconvert)
    output.txt   modified text, ready to convert back to binary
    boxes.json   JSON array of brushes, e.g.
                 [
                   {"name": "floor",     "center": [0, 0, 8],    "half": [256, 256, 8]},
                   {"name": "back_wall", "center": [0, -248, 128], "half": [256, 8, 128]}
                 ]
                 center = world position of the box center, half = half extents (x/y/z).

Typical workflow (dmxconvert lives in <game>\\game\\bin\\win64\\):
    dmxconvert.exe -i map.vmap -o map.txt -oe keyvalues2 -of world
    python add_box_brush.py map.txt map_house.txt boxes.json
    dmxconvert.exe -i map_house.txt -o map.vmap -oe binary -of vmap

CRITICAL: convert back with `-of vmap`. Using `-of world` writes a `format world 1`
header, and Hammer then warns the file was "upconverted from an unspecified format".

Format notes (verified against CS2 Hammer-written maps, 2026):
- A brush is a CMapMesh element with a CDmePolygonMesh meshData block.
- The mesh uses a half-edge topology. For a box: 8 vertices, 6 faces,
  12 undirected edges represented as 24 directed half-edges.
- edgeVertexDataIndices must map each undirected edge k to the *consecutive*
  face-vertex slot pair {2k, 2k+1}. Any other permutation parses fine with
  dmxconvert but crashes Hammer when opening the map.
- faceVertexData holds 4 streams (texcoord:0, normal:0, tangent:0,
  PerVertexLighting:0), one entry per face-vertex (24 for a box).
- edgeData.flags:0 has one entry per undirected edge (12); faceData has one
  entry per face (6) with textureScale/textureAxisU/textureAxisV/
  materialindex/flags/lightmapScaleBias streams.
- element ids must be unique uuid4; nodeID unique int; referenceID unique uint64.
"""

import argparse
import json
import re
import uuid


# ---------------------------------------------------------------- box topology
# A box with vertices (local, relative to brush origin):
#   v0=(-hx,-hy,+hz) v1=(+hx,-hy,+hz) v2=(-hx,+hy,+hz) v3=(+hx,+hy,-hz)
#   v4=(-hx,+hy,-hz) v5=(+hx,+hy,+hz) v6=(+hx,-hy,-hz) v7=(-hx,-hy,-hz)
VERTEX_POS = [
    (-1, -1, 1), (1, -1, 1), (-1, 1, 1), (1, 1, -1),
    (-1, 1, -1), (1, 1, 1), (1, -1, -1), (-1, -1, -1),
]

# Half-edge heads, exactly as Hammer writes a box (index h -> vertex at head of h).
EDGE_VERTEX_INDICES = [1, 0, 5, 1, 2, 5, 1, 6, 3, 4, 6, 3,
                       7, 6, 3, 5, 7, 4, 0, 7, 2, 0, 4, 2]

EDGE_OPPOSITE = [i ^ 1 for i in range(24)]
EDGE_NEXT = [2, 19, 4, 7, 21, 14, 1, 11, 10, 23, 12, 15,
             17, 6, 9, 3, 18, 8, 20, 13, 22, 0, 16, 5]
EDGE_FACE = [0, 5, 0, 3, 0, 4, 5, 3, 1, 4, 1, 3,
             1, 5, 4, 3, 2, 1, 2, 5, 2, 0, 2, 4]
EDGE_DATA = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5,
             6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11]
VERTEX_EDGE = [0, 1, 22, 15, 8, 14, 6, 18]

# CRITICAL INVARIANT: half-edge h maps to face-vertex slot h^1 so each undirected
# edge k uses the consecutive pair {2k, 2k+1}. Hammer crashes on any other layout.
EDGE_VERTEX_DATA = [h ^ 1 for h in range(24)]

FACE_LOOPS = [[21, 0, 2, 4], [17, 8, 10, 12], [22, 16, 18, 20],
              [15, 3, 7, 11], [14, 9, 23, 5], [6, 1, 19, 13]]
FACE_EDGE_STARTS = [21, 17, 22, 15, 14, 6]
FACE_CORNERS = [[0, 1, 5, 2], [4, 3, 6, 7], [4, 7, 0, 2],
                [5, 1, 6, 3], [3, 4, 2, 5], [1, 0, 7, 6]]

FACE_NORMAL = [(0, 0, 1), (0, 0, -1), (-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0)]
FACE_U = [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 0), (1, 0, 0), (1, 0, 0)]
FACE_V = [(0, -1, 0), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 0, -1), (0, 0, -1)]
FACE_TANGENT = [(1, 0, 0, -1), (1, 0, 0, 1), (0, 1, 0, 1),
                (0, 1, 0, -1), (1, 0, 0, 1), (1, 0, 0, -1)]
UV_SCALE = 1.0 / 16.0


def fmt_num(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return "%.9g" % v


def fmt_vec(vals):
    return " ".join(fmt_num(v) for v in vals)


def new_id():
    return str(uuid.uuid4())


def new_ref():
    return "0x" + uuid.uuid4().hex[:16]


def build_streams(hx, hy, hz):
    pos = [fmt_vec((sx * hx, sy * hy, sz * hz)) for sx, sy, sz in VERTEX_POS]
    texcoord = [None] * 24
    normal = [None] * 24
    tangent = [None] * 24
    for f in range(6):
        U = FACE_U[f]
        V = FACE_V[f]
        for c in range(4):
            h = FACE_LOOPS[f][c]
            slot = EDGE_VERTEX_DATA[h]
            px, py, pz = (float(x) for x in pos[FACE_CORNERS[f][c]].split())
            texcoord[slot] = fmt_vec(((px * U[0] + py * U[1] + pz * U[2]) * UV_SCALE,
                                      (px * V[0] + py * V[1] + pz * V[2]) * UV_SCALE))
            normal[slot] = fmt_vec(FACE_NORMAL[f])
            tangent[slot] = fmt_vec(FACE_TANGENT[f])
    return pos, texcoord, normal, tangent


def _array(name, typ, vals, indent):
    pad = "\t" * indent
    if not vals:
        return pad + '\t"%s" "%s" \n%s\t[\n%s\t]' % (name, typ, pad, pad)
    body = ",\n".join(pad + '\t\t"%s"' % v for v in vals)
    return pad + '\t"%s" "%s" \n%s\t[\n%s\n%s\t]' % (name, typ, pad, body, pad)


def _stream(name, attr, sem, bufloc, flags, dtype, data):
    pad = "\t\t"
    body = ",\n".join(pad + '\t\t"%s"' % d for d in data)
    return "\n".join([
        pad + '"CDmePolygonMeshDataStream"',
        pad + "{",
        pad + '\t"id" "elementid" "' + new_id() + '"',
        pad + '\t"name" "string" "' + name + '"',
        pad + '\t"standardAttributeName" "string" "' + attr + '"',
        pad + '\t"semanticName" "string" "' + sem + '"',
        pad + '\t"semanticIndex" "int" "0"',
        pad + '\t"vertexBufferLocation" "int" "' + str(bufloc) + '"',
        pad + '\t"dataStateFlags" "int" "' + str(flags) + '"',
        pad + '\t"subdivisionBinding" "element" ""',
        pad + '\t"data" "' + dtype + '" ',
        pad + "\t[",
        body,
        pad + "\t]",
        pad + "}",
    ])


def build_mesh_block(origin, hx, hy, hz, node_id, material):
    pos, texcoord, normal, tangent = build_streams(hx, hy, hz)

    vertex_data = "\n".join([
        '\t\t"vertexData" "CDmePolygonMeshDataArray"',
        "\t\t{",
        '\t\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t\t"size" "int" "8"',
        '\t\t\t"streams" "element_array" ',
        "\t\t\t[",
        _stream("position:0", "position", "position", 0, 3, "vector3_array", pos),
        "\t\t\t]",
        "\t\t}",
    ])

    fvd_streams = [
        _stream("texcoord:0", "texcoord", "texcoord", 0, 1, "vector2_array", texcoord),
        _stream("normal:0", "normal", "normal", 0, 1, "vector3_array", normal),
        _stream("tangent:0", "tangent", "tangent", 0, 1, "vector4_array", tangent),
        _stream("PerVertexLighting:0", "", "PerVertexLighting", 1, 1, "vector4_array", ["1 1 1 0"] * 24),
    ]
    face_vertex_data = "\n".join([
        '\t\t"faceVertexData" "CDmePolygonMeshDataArray"',
        "\t\t{",
        '\t\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t\t"size" "int" "24"',
        '\t\t\t"streams" "element_array" ',
        "\t\t\t[",
        ",\n".join(fvd_streams),
        "\t\t\t]",
        "\t\t}",
    ])

    edge_data = "\n".join([
        '\t\t"edgeData" "CDmePolygonMeshDataArray"',
        "\t\t{",
        '\t\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t\t"size" "int" "12"',
        '\t\t\t"streams" "element_array" ',
        "\t\t\t[",
        _stream("flags:0", "flags", "flags", 0, 3, "int_array", ["0"] * 12),
        "\t\t\t]",
        "\t\t}",
    ])

    face_data_streams = [
        _stream("textureScale:0", "textureScale", "textureScale", 0, 0, "vector2_array", ["0.25 0.25"] * 6),
        _stream("textureAxisU:0", "textureAxisU", "textureAxisU", 0, 0, "vector4_array", [fmt_vec(U + (0,)) for U in FACE_U]),
        _stream("textureAxisV:0", "textureAxisV", "textureAxisV", 0, 0, "vector4_array", [fmt_vec(V + (0,)) for V in FACE_V]),
        _stream("materialindex:0", "materialindex", "materialindex", 0, 8, "int_array", ["0"] * 6),
        _stream("flags:0", "flags", "flags", 0, 3, "int_array", ["0"] * 6),
        _stream("lightmapScaleBias:0", "lightmapScaleBias", "lightmapScaleBias", 0, 1, "int_array", ["0"] * 6),
    ]
    face_data = "\n".join([
        '\t\t"faceData" "CDmePolygonMeshDataArray"',
        "\t\t{",
        '\t\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t\t"size" "int" "6"',
        '\t\t\t"streams" "element_array" ',
        "\t\t\t[",
        ",\n".join(face_data_streams),
        "\t\t\t]",
        "\t\t}",
    ])

    subdivision = "\n".join([
        '\t\t"subdivisionData" "CDmePolygonMeshSubdivisionData"',
        "\t\t{",
        '\t\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t\t"subdivisionLevels" "int_array" ',
        "\t\t\t[",
        ",\n".join('\t\t\t\t"0"' for _ in range(24)),
        "\t\t\t]",
        '\t\t\t"streams" "element_array" ',
        "\t\t\t[",
        "\t\t\t]",
        "\t\t}",
    ])

    mesh_data = "\n".join([
        '\t"meshData" "CDmePolygonMesh"',
        "\t{",
        '\t\t"id" "elementid" "' + new_id() + '"',
        '\t\t"name" "string" "meshData"',
        _array("vertexEdgeIndices", "int_array", [str(x) for x in VERTEX_EDGE], 2),
        _array("vertexDataIndices", "int_array", [str(x) for x in range(8)], 2),
        _array("edgeVertexIndices", "int_array", [str(x) for x in EDGE_VERTEX_INDICES], 2),
        _array("edgeOppositeIndices", "int_array", [str(x) for x in EDGE_OPPOSITE], 2),
        _array("edgeNextIndices", "int_array", [str(x) for x in EDGE_NEXT], 2),
        _array("edgeFaceIndices", "int_array", [str(x) for x in EDGE_FACE], 2),
        _array("edgeDataIndices", "int_array", [str(x) for x in EDGE_DATA], 2),
        _array("edgeVertexDataIndices", "int_array", [str(x) for x in EDGE_VERTEX_DATA], 2),
        _array("faceEdgeIndices", "int_array", [str(x) for x in FACE_EDGE_STARTS], 2),
        _array("faceDataIndices", "int_array", [str(x) for x in range(6)], 2),
        _array("materials", "string_array", [material], 2),
        vertex_data,
        face_vertex_data,
        edge_data,
        face_data,
        subdivision,
        "\t}",
    ])

    elem_id = new_id()
    lines = [
        '"CMapMesh"',
        "{",
        '\t"id" "elementid" "' + elem_id + '"',
        '\t"nodeID" "int" "' + str(node_id) + '"',
        '\t"referenceID" "uint64" "' + new_ref() + '"',
        '\t"children" "element_array" ',
        "\t[",
        "\t]",
        '\t"variableTargetKeys" "string_array" ',
        "\t[",
        "\t]",
        '\t"variableNames" "string_array" ',
        "\t[",
        "\t]",
        '\t"cubeMapName" "string" ""',
        '\t"lightGroup" "string" ""',
        '\t"visexclude" "bool" "0"',
        '\t"disablemerging" "bool" "0"',
        '\t"renderwithdynamic" "bool" "0"',
        '\t"disableHeightDisplacement" "bool" "0"',
        '\t"fademindist" "float" "-1"',
        '\t"fademaxdist" "float" "0"',
        '\t"bakelighting" "bool" "1"',
        '\t"precomputelightprobes" "bool" "1"',
        '\t"renderToCubemaps" "bool" "1"',
        '\t"emissiveLightingEnabled" "bool" "1"',
        '\t"emissiveLightingBoost" "float" "1"',
        '\t"disableShadows" "int" "0"',
        '\t"lightingDummy" "bool" "0"',
        '\t"smoothingAngle" "float" "40"',
        '\t"tintColor" "color" "255 255 255 255"',
        '\t"renderAmt" "int" "255"',
        '\t"physicsType" "string" "default"',
        '\t"physicsGroup" "string" ""',
        '\t"physicsInteractsAs" "string" ""',
        '\t"physicsInteractsWith" "string" ""',
        '\t"physicsInteractsExclude" "string" ""',
        mesh_data,
        '\t"physicsSimplificationOverride" "bool" "0"',
        '\t"physicsSimplificationError" "float" "0"',
        '\t"origin" "vector3" "' + fmt_vec(origin) + '"',
        '\t"angles" "qangle" "0 0 0"',
        '\t"scales" "vector3" "1 1 1"',
        '\t"transformLocked" "bool" "0"',
        '\t"force_hidden" "bool" "0"',
        '\t"editorOnly" "bool" "0"',
        "}",
    ]
    return "\n".join(lines), elem_id


def insert_brushes(lines, blocks, refs):
    """Add 'element' refs to world children and append CMapMesh blocks at the end."""
    world_i = next(i for i, l in enumerate(lines) if '"world" "CMapWorld"' in l)
    child_i = next(i for i in range(world_i, len(lines)) if '"children" "element_array"' in lines[i])
    open_i = next(i for i in range(child_i, len(lines)) if lines[i].strip() == "[")
    close_i = None
    depth = 0
    for i in range(child_i + 1, len(lines)):
        depth += lines[i].count("[") - lines[i].count("]")
        if depth == 0:
            close_i = i
            break
    if close_i is None:
        raise RuntimeError("world children array not closed")

    ref_lines = ['\t\t\t"element" "' + eid + '",' for eid in refs]
    out = []
    for i, l in enumerate(lines):
        if i == open_i:
            out.append(l)
            out.extend(ref_lines)
            continue
        out.append(l)
    out.append("")
    out.extend(blocks)
    out.append("")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="vmap keyvalues2 text file")
    ap.add_argument("output", help="output text file")
    ap.add_argument("boxes", help="JSON file with brush list")
    ap.add_argument("--material", default="materials/dev/dev_measuregeneric01.vmat")
    ap.add_argument("--node-start", type=int, default=200)
    args = ap.parse_args()

    with open(args.boxes, encoding="utf-8") as fh:
        boxes = json.load(fh)
    lines = open(args.input, encoding="utf-8", errors="replace").read().splitlines()

    blocks = []
    refs = []
    node_id = args.node_start
    for b in boxes:
        block, eid = build_mesh_block(tuple(b["center"]), *b["half"], node_id, args.material)
        node_id += 1
        blocks.append(block)
        refs.append(eid)

    out = insert_brushes(lines, blocks, refs)
    with open(args.output, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(out))
    print("wrote %s with %d brush(es)" % (args.output, len(boxes)))


if __name__ == "__main__":
    main()
