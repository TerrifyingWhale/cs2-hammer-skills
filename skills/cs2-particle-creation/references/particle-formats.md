# 粒子格式：`.vpcf` 与 Particle Editor

## 是什么

- `.vpcf` 是 kv3 文本，根节点为 `CParticleSystemDefinition`，由 Particle Editor（Source 2）编辑，保存后由 Hammer 自动编译为 `.vpcf_c`。
- 真实结构示例（kv3 头部版本 GUID 以 addon 中现有文件为准，不要凭记忆写）：

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
        { m_ChildRef = resource:"particles/<name>.vpcf" }
    ]
}
```

## 常用节点（真实 addon 中常见）

- 发射器 Emitters：`C_OP_ContinuousEmitter`（持续发射）、`C_OP_InstantaneousEmitter`（一次性爆发）。
- 初始化器 Initializers（`C_INIT_*`）：随机颜色、创建位置、半径、生命周期、初速度、朝向等。
- 操作器 Operators（`C_OP_*`）：`C_OP_BasicMovement`（基础移动）、`C_OP_InterpolateRadius`（半径插值）、`C_OP_ColorInterpolate`（颜色渐变）、`C_OP_FadeAndKill` / `C_OP_FadeIn` / `C_OP_FadeOut`（淡入淡出与销毁）、`C_OP_Decay`（衰减）、`C_OP_CurlNoiseForce`（噪点力）等。
- 渲染器 Renderers：`C_OP_RenderSprites`（精灵/贴图粒子，最常见）、`C_OP_RenderTrails`（拖尾）。
- 子粒子 Children：`m_ChildRef` 引用另一个 `.vpcf`，用于叠加子效果。
- 关键参数：`m_nMaxParticles` 控制粒子数量上限；`m_nBehaviorVersion` 是行为版本，复制现有文件保持一致。

## 粒子系统组件（官方文档对照）

官方文档把粒子系统组件分为以下类别，写属性时按类别查对应页面：

| 类别 | 官方页面 | 在 vpcf 中的位置 |
|---|---|---|
| 发射器 Emitters | [Particle System Emitters](https://developer.valvesoftware.com/wiki/Particle_System_Emitters) | `m_Emitters`（如 `C_OP_ContinuousEmitter`、`C_OP_InstantaneousEmitter`） |
| 初始化器 Initializers | [Particle System Initializers](https://developer.valvesoftware.com/wiki/Particle_System_Initializers) | `m_Initializers`（`C_INIT_*`） |
| 操作器 Operators | [Particle System Operators](https://developer.valvesoftware.com/wiki/Particle_System_Operators) | `m_Operators`（`C_OP_*`） |
| 渲染器 Renderers | [Particle System Renderers](https://developer.valvesoftware.com/wiki/Particle_System_Renderers) | `m_Renderers`（如 `C_OP_RenderSprites`、`C_OP_RenderTrails`） |
| 力 Forces | [Particle System Forces](https://developer.valvesoftware.com/wiki/Particle_System_Forces) | 通常作为 `C_OP_*` 节点放在 `m_Operators`（以 addon 现有文件为准） |
| 约束 Constraints | [Particle System Constraints](https://developer.valvesoftware.com/wiki/Particle_System_Constraints) | 通常作为 `C_OP_*` 节点放在 `m_Operators`（以 addon 现有文件为准） |
| 子粒子 Children | [Particle System Children](https://developer.valvesoftware.com/wiki/Particle_System_Children) | `m_Children`（`m_ChildRef = resource:"particles/xxx.vpcf"`） |

### 属性语句怎么写

每个组件在 vpcf 里是一个 kv3 节点：`_class = "C_..."` + 该节点自己的属性字段。例如发射器：

```
{
    _class = "C_OP_ContinuousEmitter"
    m_flEmitRate =
    {
        m_nType = "PF_TYPE_LITERAL"
        m_flLiteralValue = 5000.0
    }
}
```

- 属性名以 `m_` 开头（`m_fl*` float、`m_n*` int、`m_b*` bool、`m_v*` vector、`m_*Array` 数组等）。
- 数值类属性常包一层"值类型"对象（`PF_TYPE_LITERAL`、`PF_TYPE_RANDOM_RANGE` 等）；具体写法从 addon 现有 `.vpcf` 复制最稳妥。
- 某个节点支持哪些属性，查上表对应类别的官方页面；不确定时询问用户，不要凭记忆编字段。

## 命名与组织

- 粒子文件放在 addon 的 `particles/` 目录，可按主题/来源分子目录。
- 粒子贴图（精灵图）通常由 `.vtex` 定义（参见 CS2 纹理创作技能 cs2-texture-creation），放在 `materials/` 对应目录。
- 部分 addon 用 `_fix` 后缀的 `.vpcf` 作为覆盖/包装文件：文件里只含 `m_Children` 引用基础系统，用于不改原文件的情况下叠加或覆盖效果。
- 不要假设命名规则：先看目标 addon 的 `particles/` 目录结构。

## 保存与挂载

- Particle Editor 保存后会自动编译，无需手动编译。
- 地图中用 `info_particle_system` 实体放置，`particle_system_name` 填 `.vpcf` 相对路径（如 `particles/xxx.vpcf`），按需设置启动/触发条件。
- 若效果未生效，检查粒子贴图路径、子粒子引用和 kv3 文件头版本 GUID。

## 官方文档

- [Particle Editor (Source 2)](https://developer.valvesoftware.com/wiki/Particle_Editor_(Source_2))
- [Particle System Emitters](https://developer.valvesoftware.com/wiki/Particle_System_Emitters)
- [Particle System Initializers](https://developer.valvesoftware.com/wiki/Particle_System_Initializers)
- [Particle System Operators](https://developer.valvesoftware.com/wiki/Particle_System_Operators)
- [Particle System Renderers](https://developer.valvesoftware.com/wiki/Particle_System_Renderers)
- [Particle System Forces](https://developer.valvesoftware.com/wiki/Particle_System_Forces)
- [Particle System Constraints](https://developer.valvesoftware.com/wiki/Particle_System_Constraints)
- [Particle System Children](https://developer.valvesoftware.com/wiki/Particle_System_Children)
- [Source 2 Particle System Properties](https://developer.valvesoftware.com/w/index.php?title=Source_2_Particle_System_Properties)
