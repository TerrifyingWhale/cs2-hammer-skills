# 处理 .vmap 文件

## .vmap 是什么

- Source 2 Hammer 的地图源文件。它是**二进制 DMX**，不是纯文本；文件头形如 `<!-- dmx encoding binary 9 format vmap 40 -->`。
- 可读字符串存在于共享字符串表中，因此直接对原始文件做文本搜索会产生误导：像 `trigger_teleport` 这样的类名会出现在类名/字符串表中，出现次数并不与实体一一对应。

## 把二进制转成文本

CS2 SDK 自带 `dmxconvert.exe`，常见路径：

`<game install>\game\bin\win64\dmxconvert.exe`

转换示例（路径取决于用户的安装位置）：

```
dmxconvert.exe -i <map.vmap> -o <map.txt> -oe keyvalues2 -of world
```

注意：

- 输出编码必须是 `keyvalues2`；`keyvalues` 会被拒绝为无效输出编码。
- 文本输出远大于二进制输入（43 MB 的 vmap 约产生 153 MB 文本）。
- 输出文件头为 `<!-- dmx encoding keyvalues2 4 format world 1 -->`。

## 可靠地检查实体

- 转换后的文本中，每个实体都有一个 `"entity_properties" "EditGameClassProps"` 块，其中恰好包含一行 `"classname" "string" "<class>"`。
- `"entity_properties" "EditGameClassProps"` 块的数量等于 `"classname" "string"` 行的数量——这是判断解析是否完整的有效自检，因为每个块恰好有一个 classname。
- 统计某个类别的实体数量（例如 `trigger_teleport`）时，精确匹配统计 `"classname" "string" "trigger_teleport"` 行。
- `"targetname" "string" "<name>"` 位于 classname 之后不久；targetname 为 `""` 表示实体未命名。

## 程序化添加刷子几何（无 GUI / 批量编辑）

当需要给 `.vmap` 批量添加轴对齐的刷子几何（墙体、地板、屋顶、房子等），或无法启动 Hammer 时使用。这套流程已在一台真实机器上用 CS2 Workshop Tools 验证：添加 8 个盒体刷子组成的房子后，Hammer 正常打开。

### 工作流

1. 用 `dmxconvert` 把二进制转成文本（见上节）。
2. 在文本中插入 `CMapMesh` 刷子元素。推荐直接使用本技能自带的脚本 [scripts/add_box_brush.py](../scripts/add_box_brush.py)，它接受一个 JSON 描述盒子列表（中心点 + 半边长 + 材质），生成完整的 8 顶点 / 6 面盒子网格：

   ```
   python add_box_brush.py map.txt map_house.txt boxes.json --material materials/dev/dev_measuregeneric01.vmat
   ```

3. 转回二进制。**关键：必须用 `-of vmap`，不能用 `-of world`**：

   ```
   dmxconvert.exe -i map_house.txt -o map.vmap -oe binary -of vmap
   ```

   用 `-of world` 会把文件头写成 `format world 1`，Hammer 打开时会警告 "This vmap file was upconverted from an unspecified format"。正确输出头应为 `format vmap 40`（与 Hammer 自己写的文件一致）。

### CMapMesh（刷子）结构要点

基于 Hammer 官方模板（`addon_template/maps/xxx_mapname_xxx.vmap` 转换后的文本）核对过：

- 刷子 = `CMapMesh` 元素，内含 `meshData` `CDmePolygonMesh`。网格采用**半边拓扑**：一个盒子 = 8 顶点、6 面、12 条无向边（表示为 24 条半边）。
- 拓扑数组：`vertexEdgeIndices`、`vertexDataIndices`、`edgeVertexIndices`（每条半边指向的顶点）、`edgeOppositeIndices`（半边对，`i^1`）、`edgeNextIndices`（面内下一条半边）、`edgeFaceIndices`（半边所属面）、`edgeDataIndices`、`edgeVertexDataIndices`（半边→面顶点数据槽）、`faceEdgeIndices`（每面起始半边）、`faceDataIndices`、`materials`。
- 数据块：
  - `vertexData`：`position:0`（vector3，8 条，本地坐标，相对 `origin`）。
  - `faceVertexData`：`texcoord:0`（vector2）、`normal:0`（vector3）、`tangent:0`（vector4）、`PerVertexLighting:0`（vector4，`vertexBufferLocation=1`），各 24 条（每面 4 角 × 6 面）。
  - `edgeData`：`flags:0`（int，12 条，全 0）。
  - `faceData`：`textureScale:0`、`textureAxisU:0`、`textureAxisV:0`、`materialindex:0`、`flags:0`、`lightmapScaleBias:0`，各 6 条。
  - `subdivisionData`：`subdivisionLevels`（盒子 24 个 0）+ 空 `streams`。
- 每个元素 id 必须是唯一 uuid4；`nodeID` 是唯一 int；`referenceID` 是唯一 uint64。
- world 的 `children` 数组可以同时包含内联元素与 `"element" "<uuid>"` 引用（Hammer 自己写的模板两种形式都有，如 CMapNavData 内联、多数 CMapMesh 为顶层引用）。dmxconvert 写二进制时可能把引用展开为内联，这不影响 Hammer 加载。

### 关键不变量（违反会导致 Hammer 打开地图直接闪退）

以下问题 `dmxconvert` 都能正常解析并写出，**只有 Hammer 在打开地图时会崩溃**，必须严格遵守：

1. **`edgeVertexDataIndices` 必须让每条无向边 k 的两个半边映射到连续的面顶点槽位 `{2k, 2k+1}`**（例如 `h ^ 1`）。任何其他排列（比如按面连续分配 4f+c）都能通过 dmxconvert，但 Hammer 加载即闪退。
2. 半边方向（`edgeVertexIndices`）必须与 `edgeNextIndices` / `faceEdgeIndices` 构成的面环一致。复制一个已知可用的盒子拓扑（`add_box_brush.py` 里的常量）最稳妥，不要凭记忆重排。

### 验证流程

1. 把改完的文本转回二进制（`-oe binary -of vmap`），再转回文本，确认 `CMapMesh` 数量、材质、顶点数/面数正确。
2. 做几何一致性检查：每个面的半边环闭合、面法线轴对齐、所有顶点都被引用、`edgeVertexDataIndices` 连续成对。
3. 记住：**dmxconvert 往返成功 ≠ Hammer 能打开**。Hammer 没有可用的命令行入口，最终必须让用户在 Hammer 里打开确认。基线证据：把原始 vmap 纯往返（转文本再转回 `-of vmap`）后，与原文相比只改变 `asset_preview_thumbnail` 的 id，说明 dmxconvert 的输出本身可被 Hammer 读取；新增内容崩溃时，问题在新增数据。

### 常见坑

- 反向转换用 `-of world` → 文件头变成 `format world 1` → Hammer 警告 upconverted（见上）。
- `edgeVertexDataIndices` 不连续成对 → Hammer 打开闪退。
- 元素 id 重复（例如把块内所有嵌套 id 替换成同一个 uuid）→ dmxconvert 直接访问冲突崩溃；只替换元素自身 id，保留嵌套 id。
- kv3 数组元素用逗号分隔：`},` 是合法分隔；在 `},` 之后再单独加一行 `,` 会解析失败。
- 大括号/缩进不参与解析，但 `}` 与 `},` 在"扫描块边界"时必须都算闭合。
