---
name: cs2-particle-creation
description: "创建或编辑 Counter-Strike 2 粒子系统（.vpcf），用于 Source 2 Hammer（CS2 Workshop Tools），包括发射器、操作器、渲染器、子粒子引用与贴图配置。动手编写前必须先提出澄清问题。"
---

# CS2 粒子创作

当任务是创建或编辑 CS2 粒子系统时使用本技能：从零编写 `.vpcf`、改造 addon 中现有的粒子效果（烟雾、火花、火焰、雨雪、飞虫、爆炸、激光等）、配置粒子贴图，或在图中通过 `info_particle_system` 放置/触发。地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）；粒子贴图若需要新建材质属于 CS2 材质创作技能（cs2-material-creation）。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写粒子系统：

1. "这个粒子效果用在什么地方？(环境/交互道具/BOSS/武器/天气)"
2. "希望是什么效果？(烟雾/火花/火焰/雨雪/飞虫/血迹/爆炸/激光/光点)"
3. "粒子贴图用什么？(已有素材路径，还是从 addon 现有粒子系统里复制？)"
4. "是持续播放还是触发一次？需要循环吗？"
5. "大概的性能预算？(同时存在的粒子数量级、是否屏幕空间特效)"

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

**不要逐项细问节点参数。** 先看 addon 现有 `particles/` 目录，找到最接近的效果作为模板复制改造；只有关键差异（贴图、数量、生命周期、触发方式）才提问。命名与节点说明见 [references/particle-formats.md](references/particle-formats.md)。

## 粒子系统组件

粒子系统由多类组件组成，每类在 `.vpcf` 里有对应的数组和节点：

- 发射器 Emitters、初始化器 Initializers、操作器 Operators、渲染器 Renderers、力 Forces、约束 Constraints、子粒子 Children。
- 写属性时按"节点类 + 属性字段"的格式填写；不确定某个节点有哪些属性时，查对应类别的官方文档（见 References）和 addon 现有 `.vpcf`，拿不准就问用户。

## 工作流

1. 检查 addon 的 `particles/` 目录，找最接近的 `.vpcf` 作为模板（保留 kv3 版本 GUID 和既有约定）。
2. 提出上面的问题并收集答案；批量任务进入"批量模式"。
3. 用 Particle Editor 打开模板调整，或手写 `.vpcf`（kv3 文本）后保存；子粒子通过 `resource:"particles/..."` 引用。
4. 在地图中用 `info_particle_system` 实体放置/触发（粒子系统名称填 `.vpcf` 相对路径）。
5. 保存后 Hammer 会自动编译，在游戏中验证效果。

## 批量模式（Batch mode）

当用户需要一次生成多个粒子效果时，不要逐个确认：

1. 公共设置只问一次：贴图来源、大致数量级、播放方式。
2. 接受规则文件或文件夹级默认值（例如"`particles/weather/*` → 天气类，低数量，循环播放"）。
3. 一次性输出全部 `.vpcf` 文件清单与内容。
4. 能推断的不要问：命名、贴图、组织方式以 addon 现有 `particles/` 目录为准。

## References

- [references/particle-formats.md](references/particle-formats.md) - `.vpcf` 语法、常用节点、命名组织与挂载步骤。
- 官方：[Particle Editor (Source 2)](https://developer.valvesoftware.com/wiki/Particle_Editor_(Source_2))、[Emitters](https://developer.valvesoftware.com/wiki/Particle_System_Emitters)、[Initializers](https://developer.valvesoftware.com/wiki/Particle_System_Initializers)、[Operators](https://developer.valvesoftware.com/wiki/Particle_System_Operators)、[Renderers](https://developer.valvesoftware.com/wiki/Particle_System_Renderers)、[Forces](https://developer.valvesoftware.com/wiki/Particle_System_Forces)、[Constraints](https://developer.valvesoftware.com/wiki/Particle_System_Constraints)、[Children](https://developer.valvesoftware.com/wiki/Particle_System_Children)。
