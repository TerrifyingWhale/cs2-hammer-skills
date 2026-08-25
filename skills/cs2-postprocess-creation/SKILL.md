---
name: cs2-postprocess-creation
description: "创建或编辑 Counter-Strike 2 滤镜（.vpost），用于 Source 2 Hammer（CS2 Workshop Tools），包括色调映射、泛光、暗角、局部对比等图层配置，以及 post_processing_volume 挂载。动手编写前必须先提出澄清问题。"
---

# CS2 滤镜创作

当任务是创建或编辑 CS2 滤镜时使用本技能：从零编写 `.vpost`、改造 addon 中现有的滤镜（色调、氛围、水下、暗角、泛光等）、配置图层，或在地图中用 `post_processing_volume` 挂载滤镜。地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写滤镜：

1. "这个滤镜用在什么场景？(白天/夜晚/水下/恐怖/强光/电影感)"
2. "希望有哪些效果？(色调映射/泛光/暗角/局部对比/色彩校正)"
3. "滤镜范围是整张地图还是某个区域？(post_processing_volume 大小)"
4. "强度大概要多强？(轻微校正还是明显风格化)"

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

提问前，先看 addon 现有 `postprocess/` 目录里的 `.vpost`，找最接近的作模板（保留 kv3 版本 GUID）。图层结构与参数见 [references/postprocess-formats.md](references/postprocess-formats.md)。

## 生成规则（以 test.vpost 为规范）

- `test.vpost` 包含全部图层类型（亮度/对比、饱和度/鲜艳度、色阶、局部对比、暗角、曲线、色相/饱和度、色调、色彩平衡、查找表、泛光、色调映射），是生成滤镜的规范模板，完整结构见 [references/postprocess-formats.md](references/postprocess-formats.md)。
- **生成时只保留需要的图层**：用不到哪个 layer 就不写对应的字段块；需要多个图层时按 `m_layers` 数组顺序排列。
- kv3 头部照抄模板（版本与目标 addon 现有文件一致）。

## 工作流

1. 检查 addon 的 `postprocess/` 目录，选择最接近的 `.vpost` 作为模板。
2. 提出上面的问题并收集答案。
3. 按 test.vpost 模板生成，只保留需要的图层；或用 Postprocessing Editor 调整后保存。
4. 在地图中放置 `post_processing_volume` 实体，把 `.vpost` 指定给它，并设置体积范围与过渡。
5. 保存后 Hammer 会自动编译，在 Hammer 视口/游戏中验证滤镜效果。

## References

- [references/postprocess-formats.md](references/postprocess-formats.md) - `.vpost` 规范模板（test.vpost 全图层）、图层类型与挂载步骤。
- 官方：[Post Processing Editor 文档](https://developer.valvesoftware.com/wiki/Postprocessing_Editor/Docs)。
