---
name: cs2-hammer-mapping
description: "使用 Source 2 Hammer（CS2 Workshop Tools）创建、编辑、检查或排查 Counter-Strike 2 地图：地图工作流、实体设置、光照、发布，以及 .vmap 文件处理。⚠️ 慎用：程序化 .vmap 编辑功能尚不稳定，存在风险。生成单个材质、纹理、模型、粒子、滤镜、声音或脚本请改用对应的专项技能。"
---

# CS2 Hammer 地图创作

当任务涉及使用 Source 2 Hammer 编辑器和 CS2 Workshop Tools 创建或编辑 Counter-Strike 2（CS2）地图与关卡时，使用本技能：搭建或修改地图、放置和配置实体、理解地图系统（出生点、触发器、逻辑、光照、`cs_script`）、测试地图，或对 `.vmap` 文件进行程序化检查。

## ⚠️ 慎用提示

本技能包含的**程序化 `.vmap` 编辑功能（`dmxconvert` 转换、`add_box_brush.py` 批量刷子等）尚不稳定**，操作失败可能导致地图文件损坏、数据丢失或 Hammer 打开时闪退。

- 操作前**务必备份原始 `.vmap` 文件**，并在副本上执行。
- 转换/编辑后的结果**必须先在 Hammer 中打开验证**，`dmxconvert` 往返成功不等于 Hammer 能正常加载。
- 涉及真实项目文件时，优先在测试副本上验证通过后再应用到正式地图。
- 常规实体检查（如统计 `trigger_teleport` 数量）风险较低，但仍建议在副本上执行。

如果你不确定是否安全，先向用户说明风险并征求确认。

相关资产技能——如果请求只涉及单一资产类型，不要把这类请求路由到这里：

- 创建或编辑材质/纹理（`.vmat` / `.vtex`）：使用 CS2 材质创作技能（cs2-material-creation）。
- 创建或编辑纹理定义（`.vtex`）：使用 CS2 纹理创作技能（cs2-texture-creation）。
- 创建或编辑模型（`.vmdl`）：使用 CS2 模型创作技能（cs2-model-creation）。
- 创建或编辑粒子系统（`.vpcf`）：使用 CS2 粒子创作技能（cs2-particle-creation）。
- 创建或编辑滤镜（`.vpost`）：使用 CS2 滤镜创作技能（cs2-postprocess-creation）。
- 创建或编辑自定义声音（`.vsndevts` / `sounds/`）：使用 CS2 声音创作技能（cs2-sound-creation）。
- 创建或编辑脚本（`cs_script` / `.js`）：使用 CS2 脚本创作技能（cs2-script-creation）。

权威来源是 Valve 官方文档；优先参考它，而不是沿用 Source 1 / CS:GO 工作流的假设——两者的实体名称、属性和工具链都不同：

- [Counter-Strike 2 Workshop Tools](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools) - 所有 CS2 创作工具（地图、模组、皮肤）的总入口。
- [Valve Hammer Editor (Source 2)](https://developer.valvesoftware.com/wiki/Valve_Hammer_Editor_(Source_2)) - Hammer 概览与版本说明。

## 地图工作的核心流程

1. **工具安装。** CS2 Workshop Tools 是 CS2 的免费可选 DLC，仅支持 Windows。安装后以 Workshop Tools 模式启动 CS2，并通过 Workshop Manager 打开 addon。优先选择 "Launch Tools" 后手动打开 Hammer：通过 "Edit Addon Map" 打开会禁用路径追踪预览。
2. **Addon 目录结构。** addon 的地图源文件位于 `content/csgo_addons/<addon>/maps/`，为 `.vmap` 文件。保持 addon 名称、地图名称与 Workshop 条目一致。移植或发布地图时，遵循 [Maps Workshop](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Level_Design/Maps_Workshop) 流程（包括自带的导入工具）。
3. **在 Hammer 和游戏内迭代。** 用 Hammer 处理几何、实体和光照；检查可见性/泄漏诊断；然后在游戏内用 `map <mapname>` 测试。游戏逻辑方面，CS2 使用 `cs_script` 系统（JavaScript）；Pulse 可视化脚本目前不对最终用户开放。
4. **对照文档核实实体与系统。** CS2 的实体名称和属性与 Source 1 不同。使用不熟悉的实体或系统前，先查 [references/cs2-entities.md](references/cs2-entities.md)（官方实体列表入口 + 常见实体速查），再到官方页面核对属性与输入输出。
5. **程序化编辑 .vmap（批量刷子 / 无 GUI）。** 需要给地图批量添加墙体、地板、屋顶等轴对齐刷子几何，或无法启动 Hammer 时，阅读 [references/working-with-vmap-files.md](references/working-with-vmap-files.md) 并优先使用 [scripts/add_box_brush.py](scripts/add_box_brush.py)。注意两个已知致命细节：反向转换必须 `-of vmap`（`-of world` 会让 Hammer 报 upconverted 警告）；`edgeVertexDataIndices` 必须按连续槽位成对（否则 Hammer 打开即闪退，dmxconvert 检查不出来）。

## Source 2 资产管线概览

Hammer 和 CS2 不会直接消费原始美术文件。单独的 PNG、TGA、FBX 或 DMX 对引擎不可见；每个资产都需要一个 Source 2 "配方"文件，由 Hammer 自动编译成引擎资源（`*.vmat_c`、`*.vtex_c`、`*.vmdl_c`、`*.vpcf_c`、`*.vsnd_c`）。源文件位于 `content/csgo_addons/<addon>/`；编译后的资源位于 `game/csgo_addons/<addon>/`。

- 材质与纹理（`.vmat` / `.vtex`）在 CS2 材质创作技能（cs2-material-creation）中有独立工作流。
- 纹理（`.vtex`）在 CS2 纹理创作技能（cs2-texture-creation）中有独立工作流。
- 模型（`.vmdl`）在 CS2 模型创作技能（cs2-model-creation）中有独立工作流。
- 粒子（`.vpcf`）在 CS2 粒子创作技能（cs2-particle-creation）中有独立工作流。
- 滤镜（`.vpost`）在 CS2 滤镜创作技能（cs2-postprocess-creation）中有独立工作流。
- 声音（`.vsndevts`）在 CS2 声音创作技能（cs2-sound-creation）、脚本（`cs_script`）在 CS2 脚本创作技能（cs2-script-creation）中有独立工作流。
- 通用资产规则与检查清单见 [references/source2-asset-formats.md](references/source2-asset-formats.md)。

## 需要牢记的约束与事实

- CS2 Hammer 使用 GPU 加速光线追踪（路径追踪）预览和烘焙光照；中大型地图通常需要约 32 GB 内存，且预览/烘焙对显卡性能有要求。
- `.vmap` 是二进制 DMX 文件，不是纯文本。直接对原始文件做字符串搜索会产生误导，因为类名也会出现在字符串/类名表中。程序化检查地图前，先阅读 [references/working-with-vmap-files.md](references/working-with-vmap-files.md)。
- 资产格式在不同 Hammer 版本之间有变化（例如旧版 SDK 生成的 `.vmat` 使用 `Layer0 { shader "csgo_environment.vfx" ... }`）。请以用户 addon 中实际存在的写法和着色器名为准，不要假设固定格式。
- 官方 wiki 有反爬保护（Anubis），直接自动抓取可能被拦截；可以通过搜索引擎获取页面内容，并把链接提供给用户核实。
- 文档会随游戏更新而变化；把具体数字和要求（内存、已移除的参数、工具名称）视为"以当前文档为准"的内容，而不是固定事实。

## References

- [references/official-docs.md](references/official-docs.md) - 官方 wiki 页面导航，以及每个页面何时该读（安装、关卡设计、实体、脚本、发布）。
- [references/cs2-entities.md](references/cs2-entities.md) - 官方实体列表入口与常见 CS2 实体速查（按用途分类）。
- [references/working-with-vmap-files.md](references/working-with-vmap-files.md) - 用 `dmxconvert` 把二进制 `.vmap` 转成文本，可靠地统计/检查实体，以及程序化添加刷子几何（含 CMapMesh 结构与 Hammer 崩溃不变量）。配套脚本 [scripts/add_box_brush.py](scripts/add_box_brush.py)。
- [references/source2-asset-formats.md](references/source2-asset-formats.md) - 通用资产规则与检查清单。
