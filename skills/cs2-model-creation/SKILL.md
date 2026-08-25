---
name: cs2-model-creation
description: "创建或编辑 Counter-Strike 2 模型（.vmdl）：按 test 文件夹约定直接生成——kv3 头照抄，默认材质取 materials 下与 models 同路径的同名 vmat，没有就用同名 png/jpg/tga 生成。"
---

# CS2 模型创作

当任务是创建或编辑 CS2 模型时使用本技能。按目标 addon 的现有约定（以 test 文件夹为准）直接生成 `.vmdl`，不跑多余流程。

## 规则

1. **kv3 头文件照抄。** 模板第一行 `<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc41:version{12fc9d44-453a-4ae4-b4d9-7e2ac0bbd4e0} -->` 原样保留；如果目标 addon 中现有 `.vmdl` 的版本不同，则以 addon 内文件为准照抄。
2. **模型路径。** `RenderMeshFile.filename` 和 `PhysicsMeshFile.filename` 填模型相对 addon `content/` 根目录的路径（如 `models/test/test.fbx`）。
3. **默认材质路径。** `DefaultMaterialGroup.remaps.to` 填 `materials/` 下与 models **同路径**的同名 vmat：例如 `models/test/test.fbx` → `materials/test/test.vmat`。
4. **该路径没有 vmat 时。** 在 `materials/` 同路径下找同名 png/jpg/tga（如 `test_BaseColor.jpg`）；找到就触发 CS2 材质创作技能（cs2-material-creation）生成 vmat 后再填入；找不到就保持默认（`use_global_default`），不要凭空编造路径。

## 模板（以 test.vmdl 为准）

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
                                to = "materials/test/test.vmat"
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
                        name = "test"
                        parent_bone = ""
                        surface_prop = "default"
                        collision_prop = "default"
                        tool_material = ""
                        recenter_on_parent_bone = false
                        offset_origin = [ 0.0, 0.0, 0.0 ]
                        offset_angles = [ 0.0, 0.0, 0.0 ]
                        filename = "models/test/test.fbx"
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
                        filename = "models/test/test.fbx"
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

1. 确认模型文件路径（相对 content 根目录，如 `models/test/test.fbx`）。
2. 按"规则 3/4"确定默认材质路径：优先 `materials/<同路径>/<同名>.vmat`；没有 vmat 就找同名 png/jpg/tga 触发材质生成。
3. 套用上面的模板，替换路径，把 `.vmdl` 写入 `models/<同路径>/` 目录，完成；保存后 Hammer 会自动编译。

## 复杂需求才看参考

骨骼/动画、LOD、多网格/多材质组等复杂需求，读取 [references/model-formats.md](references/model-formats.md) 按需处理；默认一律用上面的模板。

## References

- [references/model-formats.md](references/model-formats.md) - 复杂模型属性、ModelDoc 工作流（仅在用户有复杂需求时读取）。
- 官方：[VMDL](https://developer.valvesoftware.com/wiki/VMDL)（含模型属性子页面：Animation、Attachments、Hitboxes、Internal External References、LodGroup、MaterialGroups、MaterialRemap、Mesh、MeshGroup、PhysicsMesh）和 [Modeling](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Modeling)。
