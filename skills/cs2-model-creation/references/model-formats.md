# 模型格式：`.vmdl` 与导入工作流

> 默认场景请直接使用 SKILL.md 里的"规则 + 模板"（以 test 文件夹约定为准）。本参考只用于用户提出复杂需求（骨骼/动画/LOD/多网格/多材质组等）时。

## `.vmdl` 是什么

`.vmdl` 是描述模型的 kv3 文本：渲染网格、骨骼、动画和物理形状。`RenderMeshFile.filename` 可以引用同级的 `.dmx` 网格文件，也可以（新版 ModelDoc）**直接引用 `.fbx` 源文件**——编译器会在构建时自动转换。保存后由 Hammer 自动编译为 `.vmdl_c`。

真实结构示例：

```
<!-- kv3 encoding:text:version{e21c7f3c-8a33-41c5-9977-a76d3a32aa0d} format:modeldoc28:version{fb63b6ca-f435-4aa0-a2c7-c66ddc651dca} -->
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
                    {
                        _class = "RenderMeshFile"
                        name = "unnamed_1"
                        filename = "models/test.dmx"
                    },
                ]
            },
            {
                _class = "AnimationList"
                children =
                [
                    {
                        _class = "AnimFile"
                        name = "test_anim"
                        source_filename = "models/test_anim.dmx"
                        looping = false
                    },
                ]
            },
            {
                _class = "PhysicsShapeList"
                children =
                [
                    {
                        _class = "PhysicsHullFile"
                        filename = "models/test_hull.dmx"
                        surface_prop = "metal"
                    },
                ]
            },
        ]
    }
}
```

- `.dmx` 路径相对于 addon 的 `content/` 根目录。
- 关键段落：`RenderMeshList`（对应 Mesh）、`AnimationList`（对应 Animation）、`PhysicsShapeList`（对应 PhysicsMesh）、`Skeleton`（骨骼）。其余属性（Hitboxes、Attachments、LodGroup、MaterialGroups 等）通常在 ModelDoc 中配置，见下节。

### 直接生成 vmdl（test 约定）

直接生成 `.vmdl`，模板与规则见 SKILL.md（以 test.vmdl 为准）：kv3 头照抄、`RenderMeshFile.filename` 填模型路径、`DefaultMaterialGroup.remaps.to` 填 `materials/<与 models 同路径>/<同名>.vmat`。

- **kv3 头部版本 GUID 必须照抄**（`format:modeldoc41:version{...}` 随 SDK 版本变化，直接复制 test.vmdl 或 addon 内现有 vmdl 的值），这是手写最容易出错的地方。
- FBX 路径相对于 addon 的 `content/` 根目录，大小写与磁盘上的文件一致。
- 骨骼、动画、LOD、多网格、多材质组等复杂模型仍用 ModelDoc 导入。

## VMDL 模型属性（官方文档对照）

`.vmdl` 的官方文档位于 [VMDL](https://developer.valvesoftware.com/wiki/VMDL)，以下子页面分别说明各项模型属性。涉及这些属性时，先读对应页面，再对照 addon 中已有的 `.vmdl` 确认字段写法；多数属性在 ModelDoc 的大纲（outliner）中配置，而不是手写。

| 属性 | 用途（官方说明要点） | 官方页面 |
|---|---|---|
| Mesh | 模型的渲染几何；一个 vmdl 可包含多个网格，网格组和 LOD 组按名称引用网格 | [Mesh](https://developer.valvesoftware.com/wiki/VMDL/Mesh) |
| MeshGroup | 对网格分组并控制可见性（例如角色本体与墨镜分属两组）；组内可包含物理网格，切换组时碰撞也随之切换 | [MeshGroup](https://developer.valvesoftware.com/wiki/VMDL/MeshGroup) |
| LodGroup | LOD 组：把网格分组并设定按屏幕距离显示的层级，主要用于性能 | [LodGroup](https://developer.valvesoftware.com/wiki/VMDL/LodGroup) |
| MaterialGroups | 模型上的多套材质，通常称为皮肤（skins） | [MaterialGroups](https://developer.valvesoftware.com/wiki/VMDL/MaterialGroups) |
| MaterialRemap | 按组重映射材质（例如切换到 hair_green 组时只替换头发材质，其余不变） | [MaterialRemap](https://developer.valvesoftware.com/wiki/VMDL/MaterialRemap) |
| Animation | 动画数据，通过 `AnimFile`/`AnimationList` 引用外部 `.dmx` 动画文件，可附带脚本 | [Animation](https://developer.valvesoftware.com/wiki/VMDL/Animation) |
| Attachments | 附着点：挂接到骨骼关节，由偏移和旋转定义，用于粒子发射、物品挂点等 | [Attachments](https://developer.valvesoftware.com/wiki/VMDL/Attachments) |
| Hitboxes | 命中盒：对齐骨骼父关节的包围盒，用于命中判定、角色选择、粒子发射；没有旋转值 | [Hitboxes](https://developer.valvesoftware.com/wiki/VMDL/Hitboxes) |
| PhysicsMesh | 物理网格：模型的碰撞几何；一个 vmdl 可包含多个，网格组和 LOD 组按名称引用 | [PhysicsMesh](https://developer.valvesoftware.com/wiki/VMDL/PhysicsMesh) |
| Internal External References | vmdl 数据的存储方式：内部引用直接写在 vmdl 文件内，外部引用是相对 content 的路径（例如共享的附着点列表） | [Internal External References](https://developer.valvesoftware.com/wiki/VMDL/Internal_External_References) |

## 模型与材质的匹配

生成模型时按以下顺序确定默认材质：

1. **同路径同名 `.vmat`：** 默认材质路径 = `materials/` 下与 models 同路径的同名 vmat，例如 `models/test/test.fbx` → `materials/test/test.vmat`。找到就直接填入 `DefaultMaterialGroup.remaps.to`。
2. **没有 vmat → 找同名图片：** 在 `materials/` 同路径下找同名 png/jpg/tga（如 `test_BaseColor.jpg`、`test.png`）。找到就触发 CS2 材质创作技能（cs2-material-creation）生成 vmat 后再填入。
3. **两者都没有：** 保持默认（`use_global_default`），不凭空编造路径；如用户要求再询问材质来源。

- 路径对应关系以"models/ 与 materials/ 同路径"为默认约定（test 文件夹即如此），目标 addon 另有习惯时以 addon 为准。

## 导入工作流

1. 通过 **ModelDoc**（Workshop Tools 自带）导入 FBX（推荐交换格式）或 DMX。ModelDoc 会写出 `.vmdl` 以及同级的 `.dmx` 网格/动画文件，并且可以生成物理碰撞体。
2. 检查生成的 `.vmdl` 是否包含预期段落，修正路径或 surface prop。
3. 简单的静态单网格模型也可以直接手写 `.vmdl` 引用 FBX（见上文"直接引用 FBX 的简单写法"）；复杂模型优先通过 ModelDoc 导入，再编辑生成的文本。
4. SMD 是 Source 1 的旧格式。不要手工把 SMD 转成 `.vmdl`；请使用 [Porting Legacy Content](https://developer.valvesoftware.com/wiki/Source_2/Docs/Porting_Legacy_Content) 中描述的导入工具，或 Source2Converter 等社区转换器。

## 碰撞类型对照表

| 用户回答 | 使用的碰撞体 |
|---|---|
| 简单/性能优先(箱子/柱子) | 盒体或凸包 (Convex Hull) |
| 需要精确碰撞(复杂形状) | 自定义碰撞网格 |
| 玩家会踩上去/站上去(地面/平台) | 精确碰撞网格 |
| 弹丸穿透(铁丝网/栏杆) | 无碰撞或仅视觉碰撞 |

## 在 Hammer 中生效

- 保存/打开时 Hammer 会自动编译资源，无需手动编译。
- 若模型不生效，对照 addon 中的现有文件检查引用的 `.dmx` 路径、骨骼/UV 数据和 kv3 文件头版本 GUID。
