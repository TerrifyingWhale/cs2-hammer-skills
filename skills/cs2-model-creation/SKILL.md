---
name: cs2-model-creation
description: "创建或编辑 Counter-Strike 2 模型（.vmdl）：按模板直接生成——kv3 头永远一模一样，默认材质取 materials 下与模型同名的 vmat，没有就用同名 png/jpg/tga 生成。"
---

# CS2 模型创作

按模板直接生成 `.vmdl`，不跑多余流程。使用前提：Agent 已打开目标 addon 文件夹。

## 规则

1. **kv3 头永远一模一样**：第一行 `<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc41:version{12fc9d44-453a-4ae4-b4d9-7e2ac0bbd4e0} -->` 原样照抄，不许改动、不许换版本。
2. **模型路径**：`RenderMeshFile.filename` / `PhysicsMeshFile.filename` 填相对 addon `content/` 根目录的路径（`<name>` 换成实际模型名）。
3. **默认材质**：`DefaultMaterialGroup.remaps.to` 填 `materials/<name>.vmat`。
4. **没有 vmat 时**：在 `materials/` 下找同名 png/jpg/tga；找到则触发 CS2 材质创作技能（cs2-material-creation）生成 vmat 后填入；找不到保持 `use_global_default`，不编造路径。

## 模板

最基本的模板（以 test.vmdl 为准）写在 [references/model-formats.md](references/model-formats.md) 里，生成时直接复制；kv3 头永远一模一样，只替换 `<name>` 与路径。

## 生成步骤

1. 确认模型路径（相对 `content/` 根目录）与模型名。
2. 按规则 3/4 确定默认材质。
3. 从 references/model-formats.md 复制模板，替换 `<name>` 与路径，写入 `models/` 对应目录；Hammer 自动编译。

## 复杂需求

骨骼/动画/LOD/多网格/多材质组等读 [references/model-formats.md](references/model-formats.md) 按需处理；默认一律用上面的基本模板。

## References

- [references/model-formats.md](references/model-formats.md) - 基本模板 + 复杂模型属性与 ModelDoc 工作流
- 官方：[VMDL](https://developer.valvesoftware.com/wiki/VMDL)、[Modeling](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Modeling)
