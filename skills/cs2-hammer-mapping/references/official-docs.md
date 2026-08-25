# 官方 CS2 Workshop Tools 文档导航

Valve 开发者百科是 CS2 地图创作的权威参考。整理日期 2026-08-24；因为工具会随游戏更新变化，请对照实时页面重新核实。

## 安装与工具

| 页面 | 何时阅读 |
|---|---|
| [Introduction](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Introduction) | 第一次使用 Workshop Tools；了解包含哪些内容以及各组件如何配合。 |
| [Installing and Launching Tools](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Installing_and_Launching_Tools) | 安装免费 DLC、启动 addon、排查启动问题。 |
| [System Requirements](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/System_Requirements) | Hammer 5.x、路径追踪光照所需的硬件要求。 |
| [Official Tools](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Official_Tools) | 随附工具清单：Hammer、Material Editor、ModelDoc、Asset Browser 等。 |
| [Valve Hammer Editor (Source 2)](https://developer.valvesoftware.com/wiki/Valve_Hammer_Editor_(Source_2)) | 编辑器功能与版本历史。 |

## 关卡设计

| 页面 | 何时阅读 |
|---|---|
| [Level Design](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Level_Design) | CS2 关卡创作的枢纽：工作流文章，以及实体、地图、天空盒列表的引用。 |
| [List of Counter-Strike 2 Entities](https://developer.valvesoftware.com/wiki/List_of_Counter-Strike_2_Entities) | 查找 CS2 实体类及其属性（按 FGD 文件分组，标注"不完整"；每个实体通常还有独立页面）。速查见 cs2-entities.md。 |
| [Maps Workshop](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Level_Design/Maps_Workshop) | 发布地图以及移植 CS:GO/其他地图；包含带 Python 脚本的导入工具。 |

## 资产创建与转换

| 页面 | 何时阅读 |
|---|---|
| [Modeling](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Modeling) | 用 ModelDoc 导入和创建 3D 模型（FBX/DMX 到 `.vmdl`）。 |
| [VMDL](https://developer.valvesoftware.com/wiki/VMDL) | `.vmdl` 模型文件格式，以及模型属性子页面（Animation、Attachments、Hitboxes、Internal External References、LodGroup、MaterialGroups、MaterialRemap、Mesh、MeshGroup、PhysicsMesh）。 |
| [VTEX (Valve Texture)](https://developer.valvesoftware.com/wiki/VTEX_(Valve_Texture)) | `.vtex` 源文件与 `.vtex_c` 纹理格式。 |
| [Particle Editor (Source 2)](https://developer.valvesoftware.com/wiki/Particle_Editor_(Source_2)) | 粒子系统（`.vpcf`）的编辑与节点（发射器、操作器、渲染器）说明。 |
| [Post Processing Editor 文档](https://developer.valvesoftware.com/wiki/Postprocessing_Editor/Docs) | 滤镜（`.vpost`）的图层编辑说明，配合 `post_processing_volume` 实体使用。 |
| [Addon Sounds](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Addon_Sounds) | 向 CS2 addon 添加自定义声音事件与音频源。 |
| [Porting Legacy Content](https://developer.valvesoftware.com/wiki/Source_2/Docs/Porting_Legacy_Content) | 把 Source 1 / CS:GO 资产（SMD、旧纹理、地图）迁移到 Source 2。 |

## 脚本

| 页面 | 何时阅读 |
|---|---|
| [Scripting](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting) | `cs_script`（JavaScript）游戏逻辑；Pulse 目前不对最终用户开放。 |
| [Scripting API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API) | `cs_script` 的 API 参考（方法、属性、事件）。 |

## 使用 wiki 的注意事项

- wiki 使用 Anubis 反机器人保护；直接自动抓取可能被 "Making sure you're not a bot!" 页面拦截。优先把页面链接提供给用户，或通过搜索引擎摘要获取内容。
- 诸如内存要求、工具可用性等事实会随更新变化——务必重新核实。
