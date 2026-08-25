# 滤镜格式：`.vpost` 与 Postprocessing Editor

## 是什么

- `.vpost` 是 kv3 文本，根节点为 `CPostProcessData`，由 Postprocessing Editor 编辑，保存后由 Hammer 自动编译为 `.vpost_c`。
- 规范模板（以 test.vpost 为准，包含全部图层；kv3 头部版本 GUID 与 addon 中现有文件保持一致）：

```text
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:generic:version{7412167c-06e9-4698-aff2-e63eb59037e7} -->
{
    _class = "CPostProcessData"
    m_layers =
    [
        {
            _class = "CBrightnessContrastColorCorrectionLayer"
            m_name = "Brightness/Contrast 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nBrightness = 0
            m_nContrast = 0
        },
        {
            _class = "CVibranceColorCorrectionLayer"
            m_name = "Saturation/Vibrance 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nVibrance = 0
            m_nSaturation = 0
        },
        {
            _class = "CLevelsColorCorrectionLayer"
            m_name = "Levels 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nInputBlackPointRGB = 0
            m_nInputBlackPointR = 0
            m_nInputBlackPointG = 0
            m_nInputBlackPointB = 0
            m_nInputWhitePointRGB = 255
            m_nInputWhitePointR = 255
            m_nInputWhitePointG = 255
            m_nInputWhitePointB = 255
            m_nOutputBlackPointRGB = 0
            m_nOutputBlackPointR = 0
            m_nOutputBlackPointG = 0
            m_nOutputBlackPointB = 0
            m_nOutputWhitePointRGB = 255
            m_nOutputWhitePointR = 255
            m_nOutputWhitePointG = 255
            m_nOutputWhitePointB = 255
            m_flGammaRGB = 1.0
            m_flGammaR = 1.0
            m_flGammaG = 1.0
            m_flGammaB = 1.0
        },
        {
            _class = "CLocalContrastLayer"
            m_name = "Local Contrast 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_params =
            {
                m_flLocalContrastStrength = 0.0
                m_flLocalContrastEdgeStrength = 0.0
                m_flLocalContrastVignetteStart = 0.0
                m_flLocalContrastVignetteEnd = 0.0
                m_flLocalContrastVignetteBlur = 0.0
            }
        },
        {
            _class = "CVignetteLayer"
            m_name = "Vignette 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_params =
            {
                m_flVignetteStrength = 0.0
                m_vCenter = [ 0.0, 0.0 ]
                m_flRadius = 0.5
                m_flRoundness = 1.0
                m_flFeather = 0.5
                m_vColorTint = [ 1.0, 1.0, 1.0 ]
            }
        },
        {
            _class = "CCurvesColorCorrectionLayer"
            m_name = "Curves 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_curvePointsRGB = [ [ 0.0, 0.0 ], [ 255.0, 255.0 ] ]
            m_curvePointsR = [ [ 0.0, 0.0 ], [ 255.0, 255.0 ] ]
            m_curvePointsG = [ [ 0.0, 0.0 ], [ 255.0, 255.0 ] ]
            m_curvePointsB = [ [ 0.0, 0.0 ], [ 255.0, 255.0 ] ]
        },
        {
            _class = "CHueSaturationColorCorrectionLayer"
            m_name = "Hue/Saturation 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nHueMaster = 0
            m_nHueRed = 0
            m_nHueYellow = 0
            m_nHueGreen = 0
            m_nHueCyan = 0
            m_nHueBlue = 0
            m_nHueMagenta = 0
            m_nSaturationMaster = 0
            m_nSaturationRed = 0
            m_nSaturationYellow = 0
            m_nSaturationGreen = 0
            m_nSaturationCyan = 0
            m_nSaturationBlue = 0
            m_nSaturationMagenta = 0
            m_nBrightnessMaster = 0
            m_nBrightnessRed = 0
            m_nBrightnessYellow = 0
            m_nBrightnessGreen = 0
            m_nBrightnessCyan = 0
            m_nBrightnessBlue = 0
            m_nBrightnessMagenta = 0
        },
        {
            _class = "CColorTintColorCorrectionLayer"
            m_name = "Color Tint 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nTintColorR = 255
            m_nTintColorG = 150
            m_nTintColorB = 20
            m_nStrength = 20
            m_bPreserveLuminosity = true
        },
        {
            _class = "CColorBalanceColorCorrectionLayer"
            m_name = "Color Balance 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_nRedCyanBalS = 0
            m_nRedCyanBalM = 0
            m_nRedCyanBalH = 0
            m_nGreenMagentaBalS = 0
            m_nGreenMagentaBalM = 0
            m_nGreenMagentaBalH = 0
            m_nBlueYellowBalS = 0
            m_nBlueYellowBalM = 0
            m_nBlueYellowBalH = 0
            m_bPreserveLuminosity = true
        },
        {
            _class = "CColorLookupColorCorrectionLayer"
            m_name = "Lookup Table 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_fileName = ""
            m_lut = [  ]
            m_nDim = 0
        },
        {
            _class = "CBloomLayer"
            m_name = "Bloom 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_params =
            {
                m_blendMode = "BLOOM_BLEND_SCREEN"
                m_flBloomStrength = 1.998
                m_flScreenBloomStrength = 0.1261
                m_flBlurBloomStrength = 1.0
                m_flBloomThreshold = 2.842
                m_flBloomThresholdWidth = 1.661
                m_flSkyboxBloomStrength = 1.0
                m_flBloomStartValue = 1.0
                m_flComputeBloomStrength = 0.03
                m_flComputeBloomThreshold = 1.0
                m_flComputeBloomRadius = 0.6
                m_flComputeBloomEffectsScale = 1.0
                m_flComputeBloomLensDirtStrength = 0.0
                m_flComputeBloomLensDirtBlackLevel = 0.1
                m_flBlurWeight = [ 0.1999, 0.1999, 0.1999, 0.1999, 0.5234 ]
                m_vBlurTint = [ [ 1.0, 1.0, 1.0 ], [ 1.0, 1.0, 1.0 ], [ 1.0, 1.0, 1.0 ], [ 1.0, 1.0, 1.0 ], [ 1.0, 1.0, 1.0 ] ]
            }
        },
        {
            _class = "CToneMappingLayer"
            m_name = "Tone Mapping 1"
            m_nOpacityPercent = 100
            m_bVisible = true
            m_pLayerMask = null
            m_params =
            {
                m_flExposureBias = 0.0
                m_flShoulderStrength = 0.0
                m_flLinearStrength = 0.001
                m_flLinearAngle = 0.001
                m_flToeStrength = 1.0
                m_flToeNum = 1.0
                m_flToeDenom = 1.0
                m_flWhitePoint = 1.498557
                m_flLuminanceSource = 0.0
                m_flExposureBiasShadows = 0.0
                m_flExposureBiasHighlights = 0.0
                m_flMinShadowLum = 0.0
                m_flMaxShadowLum = 0.5
                m_flMinHighlightLum = 2.0
                m_flMaxHighlightLum = 8.0
            }
        },
    ]
}
```

## 图层类型（test.vpost 全量）

- `CBrightnessContrastColorCorrectionLayer`：亮度/对比。
- `CVibranceColorCorrectionLayer`：饱和度/鲜艳度。
- `CLevelsColorCorrectionLayer`：色阶（输入/输出黑白点、Gamma）。
- `CLocalContrastLayer`：局部对比。
- `CVignetteLayer`：暗角。
- `CCurvesColorCorrectionLayer`：曲线。
- `CHueSaturationColorCorrectionLayer`：色相/饱和度。
- `CColorTintColorCorrectionLayer`：色调。
- `CColorBalanceColorCorrectionLayer`：色彩平衡。
- `CColorLookupColorCorrectionLayer`：查找表（LUT）。
- `CBloomLayer`：泛光。
- `CToneMappingLayer`：色调映射/曝光。

## 生成规则

- **用不到哪个图层就不写对应的字段块**；需要多个图层时按 `m_layers` 数组顺序排列。
- 每层有 `m_nOpacityPercent`（透明度）、`m_bVisible`（可见性）、`m_pLayerMask`（可选遮罩）。
- 复杂参数（如 Bloom 的 blur 权重、Curves 的曲线点）在需要调整时才改；不需要的图层整块省略。

## 挂载到地图

- 用 `post_processing_volume` 实体指定 `.vpost` 路径，并控制体积范围与过渡。
- 不同区域可以用不同 volume 给不同滤镜；多个 volume 重叠时注意优先级/过渡。
- 命名：滤镜文件通常放在 `postprocess/` 目录，建议按用途命名（如 `mapname.vpost`、`under_water.vpost`），沿用 addon 现有约定。

## 在 Hammer 中生效

- 保存/打开时 Hammer 会自动编译资源，无需手动编译。
- 在游戏中确认滤镜生效；若不生效，检查 post_processing_volume 的设置与 `.vpost` 路径。

## 官方文档

- [Post Processing Editor 文档](https://developer.valvesoftware.com/wiki/Postprocessing_Editor/Docs)
