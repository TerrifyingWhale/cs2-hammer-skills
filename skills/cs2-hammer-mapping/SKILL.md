---
name: cs2-hammer-mapping
description: "使用 Source 2 Hammer（CS2 Workshop Tools）创建、编辑、检查或排查 Counter-Strike 2 地图：地图工作流、实体设置、光照、发布，以及 .vmap 文件处理。⚠️ 慎用：程序化 .vmap 编辑功能尚不稳定，存在风险。默认先给建议与步骤，不直接修改文件；用户明确要求修改后才执行。生成单个材质、纹理、模型、粒子、滤镜、声音或脚本请改用对应的专项技能。"
---

# CS2 Hammer 地图创作

用于地图级工作：搭建/修改地图、实体、光照、测试、发布，以及 `.vmap` 检查与程序化处理。

## 默认模式：先建议，不修改

识别到用户想使用本技能时，**默认只给建议和操作步骤，不修改任何文件**：

1. 说明怎么做：给出流程、需要的实体/属性、参考文档，以及 addon 现有文件中可参考的写法。
2. 提供可执行步骤：用户可自行在 Hammer 中完成，或由 Agent 在用户确认后执行。
3. **不执行修改**：不写入/改写 `.vmap`，不运行 `add_box_brush.py`，不用 `dmxconvert` 写回文件。
4. 用户**明确要求修改**（如"帮我直接改"、"执行修改"）后，才进入修改流程，并遵守下面的慎用规则。

## ⚠️ 慎用规则（程序化 .vmap 编辑）

`dmxconvert` 转换、`add_box_brush.py` 批量刷子等尚不稳定，可能损坏地图文件或让 Hammer 闪退：

- 操作前**备份原始 `.vmap`**，在副本上执行。
- 改后**必须在 Hammer 中打开验证**；`dmxconvert` 往返成功 ≠ Hammer 能加载。
- 不确定时先说明风险，征求用户确认。

## 地图工作流程

1. 工具与 addon：用 Workshop Tools 启动，从 Workshop Manager 打开 addon；地图源文件在 `content/csgo_addons/<addon>/maps/*.vmap`。
2. 迭代：Hammer 处理几何/实体/光照，游戏内 `map <mapname>` 测试；逻辑用 `cs_script`（JavaScript）。
3. 查实体：先用 [references/cs2-entities.md](references/cs2-entities.md) 定位类别，再到官方页面核对属性。
4. 程序化 `.vmap`（仅用户确认后）：见 [references/working-with-vmap-files.md](references/working-with-vmap-files.md) 与 [scripts/add_box_brush.py](scripts/add_box_brush.py)。关键：反向转换必须 `-of vmap`；`edgeVertexDataIndices` 必须连续成对。

## 路由

单一资产任务改走专项技能：材质（cs2-material-creation）、纹理（cs2-texture-creation）、模型（cs2-model-creation）、粒子（cs2-particle-creation）、滤镜（cs2-postprocess-creation）、声音（cs2-sound-creation）、脚本（cs2-script-creation）。

## 关键事实

- `.vmap` 是二进制 DMX；直接搜原始文件会误导，先转文本。
- 资产配方由 Hammer 自动编译，不手动编译。
- 格式随 SDK 版本变化，生成时先按对应 reference 模板，不生效再对照 addon 现有文件排查；官方文档优先（wiki 有反爬保护，可直接给链接）。

## References

- [references/official-docs.md](references/official-docs.md) - 官方文档导航
- [references/cs2-entities.md](references/cs2-entities.md) - 实体速查
- [references/working-with-vmap-files.md](references/working-with-vmap-files.md) - `dmxconvert` 检查与刷子结构（含崩溃不变量）
- [references/source2-asset-formats.md](references/source2-asset-formats.md) - 通用资产规则
