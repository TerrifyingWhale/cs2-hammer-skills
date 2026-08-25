---
name: cs2-material-creation
description: "创建或编辑 Counter-Strike 2 材质（.vmat），用于 Source 2 Hammer（CS2 Workshop Tools），包括 PNG/TGA/JPG 转换与 csgo_complex 着色器语法。纹理定义（.vtex）请改用 CS2 纹理创作技能（cs2-texture-creation）。"
---

# CS2 材质创作

从图片生成/编辑 `.vmat`。使用前提：Agent 已打开目标 addon 文件夹。

## 先提问（只问关键差异）

1. "材质用在哪？(墙壁/地面/水面/玻璃/金属/布料/自发光/贴花)"
2. "需要透明或自发光效果吗？"
3. "纹理需要平铺/重复吗？"
4. "材质是给世界几何还是给模型用？"（决定 lightmapped / vertexlit）

**不逐张问贴图**：法线/粗糙度/金属度/AO/自发光按 addon 命名规则自动匹配（`_Normal`/`_normal`、`_Roughness`/`_rough`、`_Metalness`/`_metal`、`_AO`/`_ao`、`_Emissive`）。匹配到才填槽位并加标志位，匹配不到保持默认。

**只写 csgo_complex**：模板见 [references/material-formats.md](references/material-formats.md)；识别为 water/glass/skybox 等其他 shader 时不凭记忆写，向用户提问参数。

## 工作流

1. 扫描 addon 现有 `.vmat`（着色器、语法风格、纹理命名规则）。
2. 提问；批量任务走批量模式。
3. 按模板生成 `.vmat`（**不要加 kv3 头，直接以 `Layer0` 开头，写法照抄 addon 现有 `.vmat`**），写入 `materials/`；保存后 Hammer 自动编译。

## 批量模式

1. 公共设置只问一次（这批是否同一设置）。
2. 接受规则文件（文件名 → 类型 → roughness → 贴图）或文件夹默认值（如 `materials/walls/*` → 砖墙）。
3. 一次性输出全部文件清单与内容。
4. 能推断的不要问（贴图按命名规则匹配）。

## References

- [references/material-formats.md](references/material-formats.md) - `csgo_complex` 模板、命名规则、PBR 标志位、roughness 默认值
- 官方：[Csgo Complex](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Materials/Material_Creation/Csgo_Complex)
