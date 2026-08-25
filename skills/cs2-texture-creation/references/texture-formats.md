# 纹理格式：`.vtex`

## 是什么

`.vtex` 是纹理定义文件，描述"源图片 → 引擎纹理"的转换（源图路径、色彩空间、输出类型与压缩格式），由 Hammer 自动编译为 `.vtex_c`。

## 规范模板

```
<!-- dmx encoding keyvalues2_noids 1 format vtex 1 -->
"CDmeVtex"
{
    "m_inputTextureArray" "element_array"
    [
        "CDmeInputTexture"
        {
            "m_name" "string" "InputTexture0"
            "m_fileName" "string" "materials/<文件名>.png"
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

- 通常只改 `m_fileName`（源图片路径，相对 content 根目录）和 `m_colorSpace`（颜色图 `srgb`、数据图 `linear`）。
- `m_outputFormat` 默认 `DXT5`；cubemap/数组类型时再改 `m_typeString`/`m_outputTypeString`。
- `m_bNoLod` 为 1 时禁用 LOD；mipmap 由 `m_mipAlgorithm`（默认 Box）控制。
- Hammer 打开/保存时自动编译；不生效时检查源图片路径、色彩空间和文件名。

## 官方文档

- [VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture))
