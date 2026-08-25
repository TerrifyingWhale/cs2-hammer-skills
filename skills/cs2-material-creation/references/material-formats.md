# 材质格式：`.vmat`

## 规范模板（只写 csgo_complex）

检测到金属度/自发光等贴图或效果时的完整写法：

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

什么都没检测到时的默认写法（不加标志位）：

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

常用槽位：`TextureColor`、`TextureNormal`、`TextureRoughness`、`TextureMetalness`、`TextureAmbientOcclusion`、`TextureSelfIllumMask`。向量值用带引号的 `[x y z w]`，标量用带引号的数字。没有对应贴图时**不加标志位、不加空槽位**。

## 贴图命名规则（自动匹配，不逐张问）

- 常见后缀：`_BaseColor`（颜色）、`_Normal`/`_normal`（法线）、`_Roughness`/`_rough`（粗糙度）、`_Metalness`/`_metal`（金属度）、`_AO`/`_ao`、`_Height`（高度）、`_Emissive`（自发光）。
- 图片格式常见 png/tga/jpg；不同 addon 命名习惯不同，先看目标 addon 的实际规律。
- 匹配到才填槽位并加对应 `F_` 标志位；没有对应贴图时不追问，用常量或默认贴图（如 `materials/default/default_rough.tga`）。

## 标志位（按检测自动决定）

- 金属度贴图 → `F_METALNESS_TEXTURE 1` + `TextureMetalness`
- 自发光（`_Emissive` 或用户要求）→ `F_SELF_ILLUM 1` + `TextureSelfIllumMask`
- 法线 → `TextureNormal`；粗糙度 → `TextureRoughness`；AO → `TextureAmbientOcclusion`
- 没有 → 不加标志位，保持默认写法

## 其他 shader 类型（water、glass、skybox 等）

不要凭记忆编写这些 shader 的 vmat 语法；先向用户提问确认 shader 类型与参数（或参考文件、官方文档），拿到后再生成。

## 粗糙度参考值（仅无粗糙度贴图时）

| 材质类型 | roughness |
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

## 备注

- `.vtex` 由 CS2 纹理创作技能（cs2-texture-creation）负责；材质槽位可直接引用源图片，也可引用 vtex。
- Hammer 打开/保存时自动编译；不生效时对照 addon 现有文件检查路径、着色器名与 kv3 头版本 GUID。

## 官方文档

- [Csgo Complex](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Materials/Material_Creation/Csgo_Complex)
