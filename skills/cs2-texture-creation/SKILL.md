---
name: cs2-texture-creation
description: "创建或编辑 Counter-Strike 2 纹理定义（.vtex），用于 Source 2 Hammer（CS2 Workshop Tools），包括 PNG/TGA/JPG 转换、色彩空间与压缩格式设置。动手编写前必须先提出澄清问题。"
---

# CS2 纹理创作

编写 `.vtex` 把 PNG/TGA/JPG 配置成引擎纹理。使用前提：Agent 已打开目标 addon 文件夹。

## 先提问

1. "纹理用途？(颜色/法线/粗糙度/金属度/AO/自发光/粒子贴图)"
2. "源图片路径？(相对 content 根目录)"
3. "色彩空间？"（颜色图 srgb；法线/粗糙度等数据图 linear）
4. "需要自定义压缩/mipmap 吗？"（默认 DXT5）

能推断的不要问：按 addon 现有 `.vtex` 与素材命名惯例推断用途与色彩空间。

## 工作流

1. 确定源图片路径与用途。
2. 以 `materials/test.vtex` 为模板（见 [references/texture-formats.md](references/texture-formats.md)），只改 `m_fileName` 和 `m_colorSpace`。
3. 写入 `materials/`；Hammer 自动编译。

## 批量模式

公共设置只问一次（色彩空间规则、压缩格式）；接受命名约定（如 `_Normal`/`_n` → linear）；一次性输出全部文件。

## References

- [references/texture-formats.md](references/texture-formats.md) - 规范模板与关键选项
- 官方：[VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture))
