# 材质格式：`.vmat`

## `.vmat` 语法（只写 csgo_complex）

只使用最常用的 `csgo_complex.vfx` 写法，以 `materials/test.vmat` 为规范模板：

```
Layer0
{
    shader "csgo_complex.vfx"

    //---- PBR（检测到对应贴图/效果才加）----
    F_ANISOTROPIC_GLOSS 1
    F_METALNESS_TEXTURE 1
    F_SELF_ILLUM 1
    F_TRANSMISSIVE_BACKFACE_NDOTL 1

    //---- Ambient Occlusion ----
    TextureAmbientOcclusion "materials/test_ao.png"

    //---- Color ----
    g_flModelTintAmount "1.000"
    g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
    TextureColor "materials/test_basecolor.png"

    //---- Lighting ----
    TextureMetalness "materials/test_specular.png"
    TextureRoughness "materials/test_roughness.png"

    //---- Normal Map ----
    TextureNormal "materials/test_normal.png"

    //---- Self Illum ----
    g_flSelfIllumAlbedoFactor "1.000"
    TextureSelfIllumMask "materials/test_selfillum.png"

    //---- Transmission ----
    TextureTransmissiveColor "materials/test_color.png"
}
```

要点：

- 常用纹理槽位（无后缀版）：`TextureColor`、`TextureNormal`、`TextureRoughness`、`TextureMetalness`、`TextureAmbientOcclusion`、`TextureSelfIllumMask`。
- 向量值使用带引号的 `[x y z w]` 语法；标量值使用带引号的数字。
- 检测到金属度/自发光等贴图或效果时，加对应的 `F_` 标志位并填槽位；没有就不加、用默认写法（见"PBR 贴图与标志位"）。
- **不编写其他 shader（water、glass 等）的语法**；识别为其他类型时向用户提问参数。

## 纹理定义（`.vtex`）

`.vtex` 是纹理格式，与材质不同。纹理定义由 CS2 纹理创作技能（cs2-texture-creation）负责，本技能只处理 `.vmat`。材质槽位可以直接引用源图片（如 `TextureColor "materials/test_basecolor.jpg"`），也可以引用 vtex。

## 其他 shader 类型（water、glass 等）

本技能只提供 `csgo_complex.vfx` 的语法。当材质类型被识别为其他 shader（例如水面、玻璃、天空盒）时：

- **不要凭记忆编写**这些 shader 的 vmat 语法。
- **向用户提问参数**：确认 shader 类型，并请用户提供具体参数（或参考文件、官方文档链接），拿到后再生成。

## 贴图命名规则

不要询问"有没有法线贴图/粗糙度贴图"这类问题。先扫描 addon 中现有 `.vmat` 的纹理引用，按命名规则自动匹配。常见后缀约定：

- 常见 PBR 素材包后缀（如 Substance 导出）：`_BaseColor`（颜色）、`_Normal`（法线）、`_Roughness`（粗糙度）、`_AO`（环境光遮蔽）、`_Metalness`（金属度）、`_Height`（高度）、`_Emissive`（自发光遮罩）。
- 法线贴图：`_normal` 最常见，旧素材也可能用 `_n`/`_nm`/`_nrm`。
- 粗糙度：`_rough` 最常见，也可能用 `_roughness`。
- 金属度：`_metal`；环境光遮蔽：`_ao`；高度图：`_height`；遮罩：`_mask`。
- 图片格式常见 png/tga/jpg，以 addon 现有文件为准。
- 不同 addon 命名习惯可能不同：先看目标 addon 的实际规律，再套用。

匹配规则：

- 颜色贴图使用原文件名（如 `materials/test.png` → `TextureColor1`）。
- 法线贴图优先找 `原文件名 + _normal`，没有时再试 `_n`/`_nm`/`_nrm`。
- 粗糙度优先找 `原文件名 + _rough`，没有时再试 `_roughness`。
- 金属度找 `原文件名 + _metal`；AO 找 `+ _ao`；高度图找 `+ _height`。
- **没有对应贴图时不追问**：粗糙度/金属度/AO 直接用常量（如 `"[0.082353 0.082353 0.082353 0.000000]"`）或默认贴图（如 `materials/default/default_rough.tga`、`materials/default/default_metal.tga`、`materials/default/default_ao.tga`），这是常见做法。

## PBR 贴图与标志位（按检测自动决定）

生成材质时，按检测到的素材自动决定是否加标志位：

- 检测到**金属度贴图**（`_Metalness` / `_metal`）→ 加 `F_METALNESS_TEXTURE 1`，并填 `TextureMetalness "路径"`。
- 检测到**自发光**（`_Emissive` 贴图或用户要求自发光）→ 加 `F_SELF_ILLUM 1`，填 `TextureSelfIllumMask "路径"`（或 `g_flSelfIllum*` 参数）。
- 检测到**法线贴图**（`_Normal` / `_normal`）→ `TextureNormal "路径"`。
- 检测到**粗糙度贴图**（`_Roughness` / `_rough`）→ `TextureRoughness "路径"`。
- 检测到 **AO 贴图**（`_AO` / `_ao`）→ `TextureAmbientOcclusion "路径"`。
- 没有对应贴图/效果 → **不加标志位**，保持默认基础写法（金属度用常量 `g_flMetalness "0.000"` 或默认贴图），不要凭空加 F_ 标志位。

检测到金属度与自发光时的写法：

```
Layer0
{
    shader "csgo_complex.vfx"

    F_METALNESS_TEXTURE 1
    F_SELF_ILLUM 1

    TextureColor "materials/<name>_BaseColor.jpg"
    TextureMetalness "materials/<name>_Metalness.jpg"
    TextureRoughness "materials/<name>_Roughness.jpg"
    TextureNormal "materials/<name>_Normal.jpg"
    TextureAmbientOcclusion "materials/<name>_AO.jpg"
    TextureSelfIllumMask "materials/<name>_Emissive.jpg"
}
```

什么都没检测到时的默认写法（无标志位）：

```
Layer0
{
    shader "csgo_complex.vfx"

    g_flMetalness "0.000"
    TextureColor "materials/<name>_BaseColor.jpg"
    TextureRoughness "materials/<name>_Roughness.jpg"
    TextureNormal "materials/<name>_Normal.jpg"
    TextureAmbientOcclusion "materials/<name>_AO.jpg"
}
```

注意：不要为了"显得完整"添加空槽位或 `UnusedVariables` 之类的结构；有对应贴图/效果才加标志位和槽位，没有就保持默认。

## 粗糙度参考值

仅当用户没有粗糙度贴图时使用，作为起步默认值：

| 材质类型 | roughness 值 |
|---|---|
| 抛光金属 | 0.0 - 0.2 |
| 粗糙金属 | 0.3 - 0.5 |
| 光滑塑料/玻璃 | 0.0 - 0.1 |
| 粗糙塑料 | 0.3 - 0.5 |
| 光滑石材 | 0.2 - 0.4 |
| 粗糙石材/砖墙 | 0.7 - 0.9 |
| 布料/织物 | 0.8 - 1.0 |
| 木头 | 0.6 - 0.8 |
| 橡胶 | 0.8 - 0.9 |

## 在 Hammer 中生效

- 保存/打开时 Hammer 会自动编译资源，无需手动编译。
- 若材质不生效，对照 addon 中的现有文件检查源图片路径、色彩空间、着色器名称和 kv3 文件头版本 GUID。

## 官方文档

- [Csgo Complex](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Materials/Material_Creation/Csgo_Complex) - `csgo_complex.vfx` 的完整参数说明。
