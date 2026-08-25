---
name: cs2-model-creation
description: "创建或编辑 Counter-Strike 2 模型（.vmdl）：按目标 addon 现有约定直接生成——kv3 头照抄，默认材质取 materials 下与 models 同路径的同名 vmat，没有就用同名 png/jpg/tga 生成。"
---

# CS2 模型创作

按目标 addon 现有约定直接生成 `.vmdl`，不跑多余流程。使用前提：Agent 已打开目标 addon 文件夹。

## 规则

1. **kv3 头照抄**：模板第一行 `<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc41:version{12fc9d44-453a-4ae4-b4d9-7e2ac0bbd4e0} -->` 原样保留；addon 现有 `.vmdl` 版本不同则以 addon 为准。
2. **模型路径**：`RenderMeshFile.filename` / `PhysicsMeshFile.filename` 填相对 addon `content/` 根目录的路径（如 `models/<name>/<name>.fbx`）。
3. **默认材质**：`DefaultMaterialGroup.remaps.to` 填 `materials/` 下与 models **同路径**的同名 vmat（`models/<name>/<name>.fbx` → `materials/<name>/<name>.vmat`）。
4. **没有 vmat 时**：同路径找同名 png/jpg/tga；找到则触发 CS2 材质创作技能（cs2-material-creation）生成 vmat 后填入；找不到保持 `use_global_default`，不编造路径。

## 模板（kv3 头与结构以 addon 现有 .vmdl 为准）

```text
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc41:version{12fc9d44-453a-4ae4-b4d9-7e2ac0bbd4e0} -->
{
    rootNode =
    {
        _class = "RootNode"
        children =
        [
            {
                _class = "MaterialGroupList"
                children =
                [
                    {
                        _class = "DefaultMaterialGroup"
                        remaps =
                        [
                            {
                                from = "matid_1.vmat"
                                to = "materials/<name>/<name>.vmat"
                            },
                        ]
                        use_global_default = false
                        global_default_material = ""
                    },
                ]
            },
            {
                _class = "PhysicsShapeList"
                children =
                [
                    {
                        _class = "PhysicsMeshFile"
                        name = "<name>"
                        parent_bone = ""
                        surface_prop = "default"
                        collision_prop = "default"
                        tool_material = ""
                        recenter_on_parent_bone = false
                        offset_origin = [ 0.0, 0.0, 0.0 ]
                        offset_angles = [ 0.0, 0.0, 0.0 ]
                        filename = "models/<name>/<name>.fbx"
                        import_scale = 1.0
                        import_filter =
                        {
                            exclude_by_default = false
                            exception_list = [  ]
                        }
                    },
                ]
                leave_body_collision_unmodified = false
                body_order = "bone_depth"
            },
            {
                _class = "RenderMeshList"
                children =
                [
                    {
                        _class = "RenderMeshFile"
                        filename = "models/<name>/<name>.fbx"
                        import_scale = 1.0
                        import_filter =
                        {
                            exclude_by_default = false
                            exception_list = [  ]
                        }
                    },
                ]
            },
        ]
        model_archetype = ""
        primary_associated_entity = ""
        document_sub_type = "ModelDocSubType_None"
    }
}
```

## 生成步骤

1. 确认模型路径（相对 `content/` 根目录）。
2. 按规则 3/4 确定默认材质。
3. 套模板替换路径，写入 `models/<同路径>/`；Hammer 自动编译。

## 复杂需求

骨骼/动画/LOD/多网格/多材质组等读 [references/model-formats.md](references/model-formats.md) 按需处理；默认一律用上面模板。

## References

- [references/model-formats.md](references/model-formats.md) - 复杂模型属性与 ModelDoc 工作流
- 官方：[VMDL](https://developer.valvesoftware.com/wiki/VMDL)、[Modeling](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Modeling)
