# 材质格式：`.vmat`

## 规范模板（csgo_complex，语法以 addon 现有 .vmat 为准）

- **不要加 kv3 头**：vmat 与 vtex/vpcf/vpost 不同，直接以 `Layer0` 开头；键名不引号、值用引号（如 `shader "csgo_complex.vfx"`）。
- **标志位非必须**：检测到对应贴图或效果才写 `F_` 标志位，并且下方才有对应语句；没检测到就整块省略。

全部贴图/效果都检测到时的完整写法：

```text
Layer0
{
	shader "csgo_complex.vfx"

	//---- PBR（检测到对应贴图/效果才加）----
	F_ANISOTROPIC_GLOSS 1
	F_METALNESS_TEXTURE 1
	F_SELF_ILLUM 1
	F_TRANSMISSIVE_BACKFACE_NDOTL 1

	//---- Per-Instance Tint Mask（检测到 _TintMask 贴图才加）----
	F_TINT_MASK 1

	//---- Translucent（需要透明才加）----
	F_TRANSLUCENT 1

	//---- Ambient Occlusion ----
	TextureAmbientOcclusion "materials/<文件名>_AO.jpg"

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
	TextureColor "materials/<文件名>_BaseColor.jpg"
	TextureTintMask "materials/<文件名>_TintMask.jpg"

	//---- Fog ----
	g_bFogEnabled "1"

	//---- Lighting ----
	TextureMetalness "materials/<文件名>_Metalness.jpg"
	TextureRoughness "materials/<文件名>_Roughness.jpg"

	//---- Normal Map ----
	TextureNormal "materials/<文件名>_Normal.jpg"

	//---- Self Illum（检测到自发光贴图/效果才加）----
	g_flSelfIllumAlbedoFactor "1.000"
	g_flSelfIllumBrightness "0.000"
	g_flSelfIllumScale "1.000"
	g_vSelfIllumScrollSpeed "[0.000 0.000]"
	g_vSelfIllumTint "[1.000000 1.000000 1.000000 0.000000]"
	TextureSelfIllumMask "materials/<文件名>_Emissive.jpg"

	//---- Texture Address Mode ----
	g_nTextureAddressModeU "0" // Wrap
	g_nTextureAddressModeV "0" // Wrap

	//---- Translucent（检测到透明才加）----
	g_flOpacityScale "1.000"
	TextureTranslucency "materials/<文件名>_Translucency.jpg"

	//---- Transmission（检测到透射贴图才加）----
	TextureTransmissiveColor "materials/<文件名>_Color.jpg"

	UnusedVariables
	{
		"g_flMetalness" "0"
		"g_flAnimationFrame" "0"
		"g_flAnimationTimeOffset" "0"
		"g_flAnimationTimePerFrame" "0.1"
		"g_nNumAnimationCells" "1"
		"g_vAnimationGrid" "[1 1]"
		"g_flOcclusionCullingBoundsScale" "1"
	}

	VariableState
	{
		"Ambient Occlusion" {}
		"Color" {}
		"Fog" {}
		"Lighting" {}
		"Normal Map" {}
		"Self Illum" {}
		"Texture Address Mode" {}
		"Translucent" {}
		"Transmission" {}
	}
}
```

什么都没检测到时的默认写法（去掉所有 F_ 标志位与对应语句）：

```text
Layer0
{
	shader "csgo_complex.vfx"

	//---- Ambient Occlusion ----
	TextureAmbientOcclusion "materials/<文件名>_AO.jpg"

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
	TextureColor "materials/<文件名>_BaseColor.jpg"

	//---- Fog ----
	g_bFogEnabled "1"

	//---- Lighting ----
	TextureRoughness "materials/<文件名>_Roughness.jpg"

	//---- Normal Map ----
	TextureNormal "materials/<文件名>_Normal.jpg"

	//---- Texture Address Mode ----
	g_nTextureAddressModeU "0" // Wrap
	g_nTextureAddressModeV "0" // Wrap

	UnusedVariables
	{
		"g_flMetalness" "0"
	}
}
```

`F_` 标志位与对应语句（按检测自动决定）：

| `F_` 标志位 | 检测到 | 对应语句 |
|---|---|---|
| F_ANISOTROPIC_GLOSS | 各向异性高光（Gloss 类贴图） | 各向异性高光相关参数 |
| F_METALNESS_TEXTURE | 金属度贴图（`_Metalness`/`_metal`） | Lighting 组的 `TextureMetalness` |
| F_SELF_ILLUM | 自发光贴图/效果（`_Emissive`） | Self Illum 整组 + `TextureSelfIllumMask` |
| F_TRANSMISSIVE_BACKFACE_NDOTL | 透射贴图 | Transmission 组的 `TextureTransmissiveColor` |
| F_TINT_MASK | 染色遮罩贴图（`_TintMask`） | Color 组的 `TextureTintMask` |
| F_TRANSLUCENT | 需要透明效果 | Translucent 组的 `g_flOpacityScale` + `TextureTranslucency` |

常用槽位：`TextureColor`、`TextureNormal`、`TextureRoughness`、`TextureMetalness`、`TextureAmbientOcclusion`、`TextureSelfIllumMask`。向量值用带引号的 `[x y z w]`，标量用带引号的数字。没有对应贴图时**不加标志位、不加空槽位**。

## 贴图命名规则（自动匹配，不逐张问）

- 常见后缀：`_BaseColor`（颜色）、`_Normal`/`_normal`（法线）、`_Roughness`/`_rough`（粗糙度）、`_Metalness`/`_metal`（金属度）、`_AO`/`_ao`、`_Height`（高度）、`_Emissive`（自发光）。
- 图片格式常见 png/tga/jpg；不同 addon 命名习惯不同，先看目标 addon 的实际规律。
- 匹配到才填槽位并加对应 `F_` 标志位；没有对应贴图时不追问，用常量或默认贴图（如 `materials/default/default_rough.tga`）。

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
