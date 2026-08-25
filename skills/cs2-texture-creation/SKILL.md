---
name: cs2-texture-creation
description: "创建或编辑 Counter-Strike 2 纹理定义（.vtex），用于 Source 2 Hammer（CS2 Workshop Tools），包括 PNG/TGA/JPG 转换、色彩空间与压缩格式设置。动手编写前必须先提出澄清问题。"
---

# CS2 纹理创作

当任务是创建或编辑 CS2 纹理定义时使用本技能：编写 `.vtex` 文件，把 PNG/TGA/JPG 源图配置成引擎纹理（色彩空间、压缩格式、mipmap 等）。材质（`.vmat`）由 CS2 材质创作技能（cs2-material-creation）负责；地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写纹理：

1. "这个纹理是什么用途？(颜色图/法线/粗糙度/金属度/AO/自发光/粒子贴图)"
2. "源图片路径是什么？(png/tga/jpg，相对 content 根目录)"
3. "色彩空间用 srgb 还是 linear？"（颜色图 srgb；法线/粗糙度/金属度等数据图 linear）
4. "需要自定义压缩格式或 mipmap 吗？"（默认 DXT5）

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

**能推断的不要问。** 先看 addon 现有 `.vtex` 文件和素材命名，按惯例推断用途与色彩空间；只有真正有歧义时才提问。

## 工作流

1. 确定源图片路径与用途（颜色图/数据图）。
2. 以 `materials/test.vtex` 为规范模板（见 [references/texture-formats.md](references/texture-formats.md)），只改 `m_fileName` 和 `m_colorSpace`，其余结构保持不变。
3. 把 `.vtex` 写入 addon 的 `materials/` 目录，保存后 Hammer 会自动编译。

## 批量模式（Batch mode）

多个纹理（例如一组 PBR 图：颜色/法线/粗糙度/金属度/AO）：

1. 公共设置只问一次：色彩空间规则、压缩格式。
2. 接受规则文件或命名约定（如"`_Normal`/`_n` 结尾 → linear"）。
3. 一次性输出全部 `.vtex` 文件清单与内容。

## References

- [references/texture-formats.md](references/texture-formats.md) - `.vtex` 规范模板（基于 test.vtex）与关键选项。
- 官方：[VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture))。
