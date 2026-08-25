---
name: cs2-postprocess-creation
description: "创建或编辑 Counter-Strike 2 滤镜（.vpost），用于 Source 2 Hammer（CS2 Workshop Tools），包括色调映射、泛光、暗角、局部对比等图层配置，以及 post_processing_volume 挂载。动手编写前必须先提出澄清问题。"
---

# CS2 滤镜创作

创建/编辑 `.vpost`。使用前提：Agent 已打开目标 addon 文件夹。

## 先提问

1. "滤镜用在什么场景？(白天/夜晚/水下/恐怖/电影感)"
2. "需要哪些效果？(色调映射/泛光/暗角/局部对比/色彩校正)"
3. "范围是整张地图还是某区域？(post_processing_volume)"
4. "强度如何？(轻微校正还是明显风格化)"

## 生成规则

- 全部图层类型与写法见 [references/postprocess-formats.md](references/postprocess-formats.md)（规范模板，仅作参考）；按用户需求只写需要的图层。
- **用不到哪个图层就不写对应字段块**；需要多个时按 `m_layers` 顺序排列。
- **kv3 头永远一模一样**：第一行原样照抄，不许改动、不许换版本。

## 工作流

1. 按用户需求与回答确定效果（图层类型、强度、范围）。
2. 提问；批量任务走批量模式。
3. 参考 addon 现有 `postprocess/` 的 `.vpost` 写法（**kv3 头永远一模一样**，照抄第一行，不许改动、不许换版本），按需求手写或 Postprocessing Editor 调整，只保留需要的图层。
4. 地图中放 `post_processing_volume` 指定 `.vpost`，设置范围与过渡；Hammer 自动编译。

## References

- [references/postprocess-formats.md](references/postprocess-formats.md) - 全图层规范模板与挂载
- 官方：[Post Processing Editor 文档](https://developer.valvesoftware.com/wiki/Postprocessing_Editor/Docs)
