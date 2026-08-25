# 材质格式：`.vmat`

## 规范模板（csgo_complex，语法以 addon 现有 .vmat 为准）

- **不要加 kv3 头**：vmat 与 vtex/vpcf/vpost 不同，直接以 `Layer0` 开头；键名不引号、值用引号（如 `shader "csgo_complex.vfx"`）。
- **PBR 标志位非必须**：只有勾选（或检测到对应贴图/效果）才写 `F_` 标志位，并且下方才有对应语句；没勾选就整块省略。

全部勾选 PBR 时的完整写法（对应 test.vmat 结构）：

```text
// THIS FILE IS AUTO-GENERATED

Layer0
{
	shader "csgo_complex.vfx"

	//---- PBR（勾选才加）----
	F_ANISOTROPIC_GLOSS 1
	F_METALNESS_TEXTURE 1
	F_SELF_ILLUM 1
	F_TRANSMISSIVE_BACKFACE_NDOTL 1

	//---- Ambient Occlusion ----
	TextureAmbientOcclusion "materials/<name>_AO.jpg"

	//---- Color ----
	g_flModelTintAmount "1.000"
	g_flTexCoordRotation "0.000"
	g_nScaleTexCoordUByModelScaleAxis "0" // None
	g_nScaleTexCoordVByModelScaleAxis "0" // None
	g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
	g_vTexCoordCenter "[0.500 0.500]"
	g_vTexCoordOffset "[0.000 0.000]"
	g_vTexCoordScale "[1.000 1.000]"
	g_vTexCoordScrollSpeed "[0.000 0.000]"
	TextureColor "materials/<name>_BaseColor.jpg"

	//---- Fog ----
	g_bFogEnabled "1"

	//---- Lighting ----
	TextureMetalness "materials/<name>_Metalness.jpg"
	TextureRoughness "materials/<name>_Roughness.jpg"

	//---- Normal Map ----
	TextureNormal "materials/<name>_Normal.jpg"

	//---- Self Illum（勾选 F_SELF_ILLUM 才有）----
	g_flSelfIllumAlbedoFactor "1.000"
	g_flSelfIllumBrightness "0.000"
	g_flSelfIllumScale "1.000"
	g_vSelfIllumScrollSpeed "[0.000 0.000]"
	g_vSelfIllumTint "[1.000000 1.000000 1.000000 0.000000]"
	TextureSelfIllumMask "materials/<name>_Emissive.jpg"

	//---- Texture Address Mode ----
	g_nTextureAddressModeU "0" // Wrap
	g_nTextureAddressModeV "0" // Wrap

	//---- Transmission（勾选 F_TRANSMISSIVE_BACKFACE_NDOTL 才有）----
	TextureTransmissiveColor "materials/<name>_Color.jpg"

	UnusedVariables
	{
		"g_flMetalness" "0"
	}
}
```

什么都没勾选时的默认写法（去掉 PBR 段与对应语句）：

```text
Layer0
{
	shader "csgo_complex.vfx"

	//---- Ambient Occlusion ----
	TextureAmbientOcclusion "materials/<name>_AO.jpg"

	//---- Color ----
	g_flModelTintAmount "1.000"
	g_flTexCoordRotation "0.000"
	g_nScaleTexCoordUByModelScaleAxis "0" // None
	g_nScaleTexCoordVByModelScaleAxis "0" // None
	g_vColorTint "[1.000000 1.000000 1.000000 0.000000]"
	g_vTexCoordCenter "[0.500 0.500]"
	g_vTexCoordOffset "[0.000 0.000]"
	g_vTexCoordScale "[1.000 1.000]"
	g_vTexCoordScrollSpeed "[0.000 0.000]"
	TextureColor "materials/<name>_BaseColor.jpg"

	//---- Fog ----
	g_bFogEnabled "1"

	//---- Lighting ----
	TextureRoughness "materials/<name>_Roughness.jpg"

	//---- Normal Map ----
	TextureNormal "materials/<name>_Normal.jpg"

	//---- Texture Address Mode ----
	g_nTextureAddressModeU "0" // Wrap
	g_nTextureAddressModeV "0" // Wrap

	UnusedVariables
	{
		"g_flMetalness" "0"
	}
}
```

PBR 标志位与对应语句：

| `F_` 标志位 | 对应语句 |
|---|---|
| F_ANISOTROPIC_GLOSS | 各向异性高光（配合 Gloss 类贴图） |
| F_METALNESS_TEXTURE | Lighting 组的 `TextureMetalness` |
| F_SELF_ILLUM | Self Illum 整组 + `TextureSelfIllumMask` |
| F_TRANSMISSIVE_BACKFACE_NDOTL | Transmission 组的 `TextureTransmissiveColor` |

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
- Hammer 打开/保存时自动编译；不生效时对照 addon 现有文件检查路径、着色器名与整体写法。

## 官方文档

- [Csgo Complex](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Materials/Material_Creation/Csgo_Complex)
