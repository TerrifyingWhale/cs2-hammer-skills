---
name: cs2-material-creation
description: "创建或编辑 Counter-Strike 2 材质（.vmat），用于 Source 2 Hammer（CS2 Workshop Tools），包括 PNG/TGA/JPG 转换与 csgo_complex 着色器语法。纹理定义（.vtex）请改用 CS2 纹理创作技能（cs2-texture-creation）。"
---

# CS2 材质创作

当任务是创建或编辑 CS2 材质时使用本技能：从图片生成 `.vmat`、选择着色器、配置透明或自发光。纹理定义（`.vtex`）由 CS2 纹理创作技能（cs2-texture-creation）负责；地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）；模型工作属于 CS2 模型创作技能（cs2-model-creation）。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写材质或纹理：

1. "这个材质是用在什么地方？(墙壁/地面/水面/玻璃/金属/布料/自发光/贴花)"
2. "需要透明效果吗？" (yes/no)
3. "需要发光/自发光效果吗？" (yes/no)
4. "纹理需要平铺/重复吗？" (yes/no)
5. "材质是给世界几何(刷出来的墙/地面)还是给模型用的？" - 决定使用 lightmapped 还是 vertexlit 着色器

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

**不要逐张询问贴图。** 法线、粗糙度、金属度、AO 等贴图直接按 addon 的命名规则自动匹配：先扫描 addon 里现有 `.vmat` 的纹理引用，总结后缀规律（常见 PBR 素材包后缀 `_BaseColor`/`_Color`、`_Normal`、`_Roughness`、`_AO`、`_Metalness`、`_Height`，以及 `_normal`/`_rough`/`_metal` 等缩写；图片常见 png/tga/jpg；规则见 [references/material-formats.md](references/material-formats.md)），再按"原文件名 + 后缀"匹配同目录素材。匹配到的贴图填进对应槽位并加上对应标志位；匹配不到就不加标志位、保持默认写法（见 material-formats.md），而不是追问用户。

**着色器只写 csgo_complex。** 创建材质时只使用 `csgo_complex.vfx` 语法（模板见 [references/material-formats.md](references/material-formats.md)）。如果材质被识别为其他类型（如 water、glass、skybox），不要凭记忆编写其他 shader 的语法，而是向用户提问参数后再生成。

提问前，先列出 addon 现有 `.vmat` 文件使用的着色器（真实 addon 中两种写法都会出现：`shader "..."` 和 `"Shader" "..."`），并确认它使用哪种 `.vmat` 风格。着色器的可用性随 SDK 版本不同而变化，所以永远不要假设某个着色器一定存在。

## 工作流

1. 检查目标 addon 的现有材质（着色器、语法风格、纹理路径、贴图命名规则）。
2. 提出上面的问题并收集答案；如果是批量任务，进入"批量模式"。
3. 使用 [references/material-formats.md](references/material-formats.md) 中的 `csgo_complex.vfx` 模板生成；识别为其他 shader 类型（water、glass 等）时向用户提问参数。
4. 按模板把 `.vmat`/`.vtex` 写入 addon 的 `materials/` 目录，保存后 Hammer 会自动编译。
5. 如果用户的回答与 addon 的现有做法冲突（例如使用了不存在的着色器），指出差异，并优先采用 addon 中已验证的约定。

## 批量模式（Batch mode）

当用户需要一次生成**多个**材质时（例如"我把 50 张 PNG 都转成材质"），进入批量模式，不要让用户逐张回答：

1. **公共设置只问一次，不要逐文件问。**
   - "这批材质都用同一个设置吗？(都用在墙壁/都用在金属/各自不同？)"
   - "如果都一样，告诉我一次；如果不一样，请提供一个映射表或规则。"
2. **接受规则文件。**
   - 用户提供 CSV/表格：文件名 → 材质类型 → roughness → 是否有法线贴图。
   - 按规则批量生成，不需要逐张确认。
3. **接受文件夹级默认值。**
   - "所有 `materials/walls/*.png` → 砖墙材质，roughness 0.8"
   - "所有 `materials/metal/*.png` → 金属材质，roughness 0.3"
4. **一次性生成全部配方，而不是逐个输出。**
   - 输出完整的文件清单 + 内容，让用户一次复制全部。
5. **设置确实不同时，要求结构化映射。**
   - 让用户给出"文件名 → 设置"的对照表或规则，而不是逐个对话确认。
6. **能推断的不要问。** 法线/粗糙度/金属度等贴图按 addon 命名规则自动匹配（见 material-formats.md），只对真正有歧义的部分提问。

## References

- [references/material-formats.md](references/material-formats.md) - `.vmat`（csgo_complex）模板、贴图命名规则、PBR 标志位、粗糙度默认值。
- 官方：[Csgo Complex](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Materials/Material_Creation/Csgo_Complex)。
