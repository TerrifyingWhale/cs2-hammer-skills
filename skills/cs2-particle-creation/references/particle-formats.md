# 粒子格式：`.vpcf`

## 是什么

`.vpcf` 是 kv3 文本，根节点 `CParticleSystemDefinition`，由 Particle Editor 编辑，Hammer 自动编译为 `.vpcf_c`。

结构示例（**kv3 头永远一模一样**：第一行原样照抄，不许改动、不许换版本）：

```text
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:vpcf63:version{a6e6a69e-52d3-4527-8b9c-ff3bb91aca3e} -->
{
    _class = "CParticleSystemDefinition"
    m_nBehaviorVersion = 12
    m_nMaxParticles = 5000
    m_bInfiniteBounds = true
    m_controlPointConfigurations =
    [
        { m_name = "preview" }
    ]
    m_Emitters =
    [
        {
            _class = "C_OP_ContinuousEmitter"
            m_flEmitRate =
            {
                m_nType = "PF_TYPE_LITERAL"
                m_flLiteralValue = 5000.0
            }
        }
    ]
    m_Operators = [ ... ]
    m_Renderers = [ ... ]
    m_Children =
    [
        { m_ChildRef = resource:"particles/<文件名>.vpcf" }
    ]
}
```

## 常用节点

- 发射器：`C_OP_ContinuousEmitter`（持续）、`C_OP_InstantaneousEmitter`（爆发）。
- 初始化器（`C_INIT_*`）：随机颜色、位置、半径、生命周期、初速度、朝向。
- 操作器（`C_OP_*`）：`C_OP_BasicMovement`、`C_OP_InterpolateRadius`、`C_OP_ColorInterpolate`、`C_OP_FadeAndKill`/`FadeIn`/`FadeOut`、`C_OP_Decay`、`C_OP_CurlNoiseForce`。
- 渲染器：`C_OP_RenderSprites`（最常见）、`C_OP_RenderTrails`。
- 子粒子：`m_ChildRef = resource:"particles/xxx.vpcf"`。
- `m_nMaxParticles` 控制数量上限；`m_nBehaviorVersion` 复制现有文件保持一致。

## 组件与属性写法（官方文档对照）

| 类别 | 官方页面 | vpcf 位置 |
|---|---|---|
| 发射器 Emitters | [Emitters](https://developer.valvesoftware.com/wiki/Particle_System_Emitters) | `m_Emitters` |
| 初始化器 Initializers | [Initializers](https://developer.valvesoftware.com/wiki/Particle_System_Initializers) | `m_Initializers`（`C_INIT_*`） |
| 操作器 Operators | [Operators](https://developer.valvesoftware.com/wiki/Particle_System_Operators) | `m_Operators`（`C_OP_*`） |
| 渲染器 Renderers | [Renderers](https://developer.valvesoftware.com/wiki/Particle_System_Renderers) | `m_Renderers` |
| 力 Forces | [Forces](https://developer.valvesoftware.com/wiki/Particle_System_Forces) | 通常为 `C_OP_*` 放 `m_Operators` |
| 约束 Constraints | [Constraints](https://developer.valvesoftware.com/wiki/Particle_System_Constraints) | 通常为 `C_OP_*` 放 `m_Operators` |
| 子粒子 Children | [Children](https://developer.valvesoftware.com/wiki/Particle_System_Children) | `m_Children` |

属性写法：节点 `_class = "C_..."` + `m_*` 字段（`m_fl*` float、`m_n*` int、`m_b*` bool、`m_v*` vector、`m_*Array` 数组）。数值类属性常包值类型对象（`PF_TYPE_LITERAL`、`PF_TYPE_RANDOM_RANGE`）；具体写法从 addon 现有 `.vpcf` 复制最稳妥，不确定就问用户。

## 命名与挂载

- 文件放 `particles/`，可按主题分子目录；贴图通常由 `.vtex` 定义（cs2-texture-creation）。
- 地图用 `info_particle_system` 放置，`particle_system_name` 填 `.vpcf` 相对路径。
- 不生效时检查粒子贴图路径、子粒子引用（kv3 头永远一模一样，不要改动）。

## 官方文档

- [Particle Editor (Source 2)](https://developer.valvesoftware.com/wiki/Particle_Editor_(Source_2))
- [Source 2 Particle System Properties](https://developer.valvesoftware.com/w/index.php?title=Source_2_Particle_System_Properties)
