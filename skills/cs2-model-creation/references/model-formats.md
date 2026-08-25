# 模型格式：`.vmdl` 与导入工作流

> 默认场景直接使用 SKILL.md 里的"规则 + 模板"；本参考只用于复杂需求（骨骼/动画/LOD/多网格/多材质组等）。

## `.vmdl` 是什么

`.vmdl` 是描述模型的 kv3 文本：渲染网格、骨骼、动画和物理形状。`RenderMeshFile.filename` 可引用同级 `.dmx` 网格文件，也可（新版 ModelDoc）直接引用 `.fbx`，编译器构建时自动转换。保存后 Hammer 自动编译为 `.vmdl_c`。

结构示例（kv3 头以 addon 现有文件为准）：

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
                      filename = "models/test.dmx" }
                ]
            },
            {
                _class = "AnimationList"
                children =
                [
                    { _class = "AnimFile"
                      name = "test_anim"
                      source_filename = "models/test_anim.dmx"
                      looping = false }
                ]
            },
            {
                _class = "PhysicsShapeList"
                children =
                [
                    { _class = "PhysicsHullFile"
                      filename = "models/test_hull.dmx"
                      surface_prop = "metal" }
                ]
            },
        ]
    }
}
```

- `.dmx`/`.fbx` 路径相对 addon 的 `content/` 根目录，大小写与磁盘一致。
- 简单静态单网格可直接手写 `.vmdl` 引用 FBX；复杂模型优先 ModelDoc 导入，再编辑生成的文本。

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

- Hammer 自动编译，不手动编译；不生效时检查引用的 `.dmx` 路径、骨骼/UV 数据和 kv3 头版本 GUID。
