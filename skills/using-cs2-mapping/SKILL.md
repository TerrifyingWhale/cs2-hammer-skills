---
name: using-cs2-mapping
description: Use when starting any Counter-Strike 2 map creation task - establishes the workflow and routes to the appropriate specialized CS2 skills
---

<SUBAGENT-STOP>
如果你是作为子代理被派发执行特定任务，跳过此技能。
</SUBAGENT-STOP>

<EXTREMELY-IMPORTANT>
用户提出任何 CS2 地图或资产任务时，必须调用相应技能；哪怕只有 1% 可能适用也要调用。不允许跳过流程直接编造格式。
</EXTREMELY-IMPORTANT>

## 指令优先级

1. **用户明确指令**（最高）
2. **本套件技能**
3. **默认系统提示**（最低）

用户说"不用问，直接生成"可简化流程，但仍需在 `plan/progress.md` 记录。

## 核心规则

- 先调用相关技能再行动。
- 使用前提：Agent 已打开目标 addon 文件夹（`content/csgo_addons/<addon>/`），不询问"用在哪张地图/哪个 addon"。
- 先检查 addon 现有文件找模板，只对关键差异提问。
- 批量任务走批量模式：公共设置只问一次。
- 资产由 Hammer 自动编译，不手动编译；kv3 文件头从现有文件复制。

## 标准流程

1. 判断任务类型：地图级 → `cs2-hammer-mapping`（**默认只给建议，不修改文件**；用户明确要求修改才执行）；单一资产 → 对应专项技能。
2. 检查 addon 现有文件 → 提问关键差异 → 执行 → 更新 `plan/progress.md` → 请用户确认。

## Red Flags

| 想法 | 正确做法 |
|---|---|
| "直接生成，不用问" | 先调用对应技能，检查 addon 现有模板 |
| "PNG 放进去就能用" | 需要 `.vmat`/`.vtex` 配方文件 |
| "kv3 头我默写" | 从 addon 现有文件复制 |
| "直接改二进制 .vmap" | 先转文本；地图技能默认只建议 |
| "这个 API/属性凭记忆写" | 查官方文档与本地 SDK 类型定义 |
| "我记得这个技能内容" | 重新读取当前 SKILL.md |

## 技能路由

| 任务 | 技能 |
|---|---|
| 地图级（实体/光照/发布/.vmap 程序化） | cs2-hammer-mapping（⚠️ 默认建议模式） |
| 材质 `.vmat` | cs2-material-creation |
| 纹理 `.vtex` | cs2-texture-creation |
| 模型 `.vmdl` | cs2-model-creation |
| 粒子 `.vpcf` | cs2-particle-creation |
| 滤镜 `.vpost` | cs2-postprocess-creation |
| 声音 `.vsndevts` | cs2-sound-creation |
| 脚本 `cs_script` / `.js` | cs2-script-creation |
| 技能完整性检查 | scripts/check_skill_integrity.ps1 |

## 任务收尾

中型及以上任务完成前更新 `plan/progress.md`（含 capability-use audit）；缺少记录不得声称完成。
