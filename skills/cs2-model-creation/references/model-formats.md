# 模型格式：`.vmdl` 与导入工作流

## 基本模板（直接生成 .vmdl 用这个）

**kv3 头永远一模一样**（第一行照抄，不许改动、不许换版本），其余只替换 `<name>` 与路径：

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
								to = "materials/<name>.vmat"
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
						filename = "models/<name>.fbx"
						import_scale = 1.0
						simplification_params = 
						{
							qemError = 0.0
							maxMeshVertices = 0
							small_element_threshold = 0.0
							thin_element_threshold = 0.0
						}
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
						filename = "models/<name>.fbx"
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

- 模型路径 `models/<name>.fbx` 相对 addon 的 `content/` 根目录，大小写与磁盘一致。
- 默认材质 `DefaultMaterialGroup.remaps.to` = `materials/<name>.vmat`；没有同名 vmat 时在 `materials/` 下找同名 png/jpg/tga，找到则触发 CS2 材质创作技能（cs2-material-creation）生成后再填入；都没有保持 `use_global_default`。

## 复杂模型（骨骼/动画/LOD/多网格/多材质组等）

需要骨骼、动画、LOD、多网格、多材质组等复杂结构时，用 ModelDoc 导入 FBX/DMX，再编辑生成的文本。结构示例：

```
{
    rootNode =
    {
        _class = "RootNode"
        children =
        [
            { _class = "BoneMarkupList" ... },
            {
                _class = "RenderMeshList"
                children =
                [
                    { _class = "RenderMeshFile"
                      name = "unnamed_1"
                      filename = "models/<name>.dmx" }
                ]
            },
            {
                _class = "AnimationList"
                children =
                [
                    { _class = "AnimFile"
                      name = "<name>_anim"
                      source_filename = "models/<name>_anim.dmx"
                      looping = false }
                ]
            },
            {
                _class = "PhysicsShapeList"
                children =
                [
                    { _class = "PhysicsHullFile"
                      filename = "models/<name>_hull.dmx"
                      surface_prop = "metal" }
                ]
            },
        ]
    }
}
```

- `.dmx`/`.fbx` 路径相对 addon 的 `content/` 根目录，大小写与磁盘一致。
- 简单静态单网格直接手写 `.vmdl` 引用 FBX（见上面的基本模板）；复杂模型优先 ModelDoc 导入。

## VMDL 模型属性（官方文档对照）

| 属性 | 用途 | 官方页面 |
|---|---|---|
| Mesh | 渲染几何；一个 vmdl 可含多个网格 | [Mesh](https://developer.valvesoftware.com/wiki/VMDL/Mesh) |
| MeshGroup | 网格分组与可见性控制 | [MeshGroup](https://developer.valvesoftware.com/wiki/VMDL/MeshGroup) |
| LodGroup | LOD 层级（按距离切换，性能用） | [LodGroup](https://developer.valvesoftware.com/wiki/VMDL/LodGroup) |
| MaterialGroups | 多套材质（皮肤 skins） | [MaterialGroups](https://developer.valvesoftware.com/wiki/VMDL/MaterialGroups) |
| MaterialRemap | 按组重映射材质 | [MaterialRemap](https://developer.valvesoftware.com/wiki/VMDL/MaterialRemap) |
| Animation | 动画数据（AnimFile/AnimationList） | [Animation](https://developer.valvesoftware.com/wiki/VMDL/Animation) |
| Attachments | 附着点（粒子发射、物品挂点等） | [Attachments](https://developer.valvesoftware.com/wiki/VMDL/Attachments) |
| Hitboxes | 命中盒（对齐骨骼父关节） | [Hitboxes](https://developer.valvesoftware.com/wiki/VMDL/Hitboxes) |
| PhysicsMesh | 碰撞几何 | [PhysicsMesh](https://developer.valvesoftware.com/wiki/VMDL/PhysicsMesh) |
| Internal External References | 内部/外部引用存储方式 | [Internal External References](https://developer.valvesoftware.com/wiki/VMDL/Internal_External_References) |

多数属性在 ModelDoc 的大纲（outliner）中配置而非手写；涉及哪个属性就查对应页面，再对照 addon 现有 `.vmdl` 确认字段。

## 碰撞类型对照表

| 用户回答 | 碰撞体 |
|---|---|
| 简单/性能优先（箱子/柱子） | 盒体或凸包 (Convex Hull) |
| 需要精确碰撞（复杂形状） | 自定义碰撞网格 |
| 玩家会踩/站（地面/平台） | 精确碰撞网格 |
| 弹丸穿透（铁丝网/栏杆） | 无碰撞或仅视觉碰撞 |

## 导入工作流

1. ModelDoc 导入 FBX（推荐）或 DMX，自动写出 `.vmdl` 与同级 `.dmx`。
2. 检查生成的 `.vmdl` 段落，修正路径或 surface prop。
3. SMD 是 Source 1 旧格式，不要手工转 `.vmdl`；用 [Porting Legacy Content](https://developer.valvesoftware.com/wiki/Source_2/Docs/Porting_Legacy_Content) 中的导入工具。

## 备注

- Hammer 自动编译，不手动编译；不生效时检查引用的 `.dmx`/`.fbx` 路径、骨骼/UV 数据和 kv3 头版本 GUID。
