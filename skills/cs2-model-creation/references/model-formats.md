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

## 复杂需求（一句话）

骨骼/动画/LOD/多网格/多材质组/碰撞等复杂结构用 ModelDoc 导入 FBX/DMX 处理，需要时查官方 [VMDL](https://developer.valvesoftware.com/wiki/VMDL) 文档；SMD 是 Source 1 旧格式，不要手工转。

## 备注

- Hammer 自动编译，不手动编译；不生效时检查引用的 `.fbx`/`.dmx` 路径与 kv3 头。
