---
name: cs2-particle-creation
description: "创建或编辑 Counter-Strike 2 粒子系统（.vpcf），用于 Source 2 Hammer（CS2 Workshop Tools），包括发射器、操作器、渲染器、子粒子引用与贴图配置。动手编写前必须先提出澄清问题。"
---

# CS2 粒子创作

创建/编辑 `.vpcf`（烟雾、火花、火焰、雨雪、爆炸、激光等）。使用前提：Agent 已打开目标 addon 文件夹。

## 先提问

1. "效果用在什么地方？(环境/道具/BOSS/武器/天气)"
2. "希望是什么效果？"
3. "粒子贴图用什么？(已有素材还是从 addon 现有系统复制)"
4. "持续播放还是触发一次？循环吗？"

**不要逐项细问节点参数**：按用户需求自己写，addon 现有 `particles/` 里的 `.vpcf` 只作参考；只对贴图、数量、生命周期、触发方式提问。

## 粒子系统组件

- 发射器 Emitters、初始化器 Initializers、操作器 Operators、渲染器 Renderers、力 Forces、约束 Constraints、子粒子 Children，分别对应 vpcf 里的 `m_Emitters`、`m_Initializers`、`m_Operators`、`m_Renderers`、`m_Children` 等数组。
- 属性写法：节点 `_class = "C_..."` + `m_*` 字段；数值常包值类型对象（`PF_TYPE_LITERAL` / `PF_TYPE_RANDOM_RANGE`）。不确定时查官方页面与 addon 现有 vpcf，别凭记忆编字段。

## 工作流

1. 按用户需求与回答确定效果参数（数量、生命周期、贴图、触发方式）。
2. 提问；批量任务走批量模式。
3. 参考 addon 现有 `particles/` 的 `.vpcf` 写法（**kv3 头永远一模一样**，照抄第一行，不许改动、不许换版本），手写或 Particle Editor 调整 `.vpcf`；子粒子用 `resource:"particles/..."` 引用。
4. 地图中用 `info_particle_system` 放置，`particle_system_name` 填相对路径；Hammer 自动编译。

## 批量模式

1. 公共设置只问一次（贴图来源、数量级、播放方式）。
2. 接受规则文件或文件夹默认值。
3. 一次性输出全部 `.vpcf` 文件清单与内容。
4. 能推断的不要问（命名、贴图、组织方式按需求与惯例，addon 现有 `particles/` 仅作参考）。

## References

- [references/particle-formats.md](references/particle-formats.md) - vpcf 语法、常用节点、官方文档对照
- 官方：[Particle Editor (Source 2)](https://developer.valvesoftware.com/wiki/Particle_Editor_(Source_2)) 及 [Emitters](https://developer.valvesoftware.com/wiki/Particle_System_Emitters)、[Initializers](https://developer.valvesoftware.com/wiki/Particle_System_Initializers)、[Operators](https://developer.valvesoftware.com/wiki/Particle_System_Operators)、[Renderers](https://developer.valvesoftware.com/wiki/Particle_System_Renderers)、[Forces](https://developer.valvesoftware.com/wiki/Particle_System_Forces)、[Constraints](https://developer.valvesoftware.com/wiki/Particle_System_Constraints)、[Children](https://developer.valvesoftware.com/wiki/Particle_System_Children)
