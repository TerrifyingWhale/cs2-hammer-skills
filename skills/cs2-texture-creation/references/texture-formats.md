# 纹理格式：`.vtex`

## 是什么

- `.vtex` 是纹理定义文件（DMX 文本），描述"源图片 → 引擎纹理"的转换：源图路径、色彩空间、输出类型与压缩格式。由 Hammer 自动编译为 `.vtex_c`。
- 与材质（`.vmat`）不同：vmat 是材质的配方（shader + 纹理槽位），vtex 是纹理的配方。材质槽位可以直接引用源图片，也可以用 vtex。

## 规范模板（以 materials/test.vtex 为例）

```
<!-- dmx encoding keyvalues2_noids 1 format vtex 1 -->
"CDmeVtex"
{
    "m_inputTextureArray" "element_array"
    [
        "CDmeInputTexture"
        {
            "m_name" "string" "InputTexture0"
            "m_fileName" "string" "materials/test.png"
            "m_colorSpace" "string" "srgb"      // 法线/粗糙度/金属度等数据图用 linear
            "m_typeString" "string" "2D"
            "m_imageProcessorArray" "element_array"
            [
                "CDmeImageProcessor"
                {
                    "m_algorithm" "string" "None"
                    "m_stringArg" "string" ""
                    "m_vFloat4Arg" "vector4" "0 0 0 0"
                }
            ]
        }
    ]
    "m_outputTypeString" "string" "2D"
    "m_outputFormat" "string" "DXT5"
    "m_textureOutputChannelArray" "element_array"
    [
        "CDmeTextureOutputChannel"
        {
            "m_inputTextureArray" "string_array" [ "InputTexture0" ]
            "m_srcChannels" "string" "rgba"
            "m_dstChannels" "string" "rgba"
            "m_mipAlgorithm" "CDmeImageProcessor"
            {
                "m_algorithm" "string" "Box"
                "m_stringArg" "string" ""
                "m_vFloat4Arg" "vector4" "0 0 0 0"
            }
            "m_outputColorSpace" "string" "srgb"
        }
    ]
    "m_vClamp" "vector3" "0 0 0"
    "m_bNoLod" "bool" "0"
}
```

## 要点

- 通常只改 `m_fileName`（源图片路径，相对 addon 的 `content/` 根目录）和 `m_colorSpace`（颜色图 `srgb`、法线/粗糙度/金属度等数据图 `linear`），其余结构保持不变。
- `m_outputFormat` 默认 `DXT5`；`m_typeString` / `m_outputTypeString` 默认 `2D`，需要 cubemap/数组类型时再改。
- mipmap 由输出通道里的 `m_mipAlgorithm`（默认 Box）控制；`m_bNoLod` 为 1 时禁用 LOD。
- 更详细的属性与选项见官方 [VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture))。

## 在 Hammer 中生效

- 保存/打开时 Hammer 会自动编译资源，无需手动编译。
- 若纹理不生效，检查源图片路径、色彩空间和文件名是否与磁盘一致。

## 官方文档

- [VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture)) - `.vtex` 源文件的属性与纹理选项（输出格式、色彩空间、mipmap 等）。官方 wiki 有反爬保护，可直接把链接提供给用户核实。
