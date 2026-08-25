---
name: cs2-mapping-assistant
description: Use when creating, editing, checking, or troubleshooting Counter-Strike 2 maps and assets with Source 2 Hammer - routes to the specialized CS2 mapping skill suite
allowed-tools: Read Write Edit Bash WebSearch
---

# CS2 Hammer 地图创作套件 (CS2 Mapping Assistant)

面向 Counter-Strike 2（Source 2 Hammer / CS2 Workshop Tools）地图创作的模块化技能套件：入口路由、专项技能、计划模板与质量门控。

## 原则

- 流程优先：先检查 addon、先提问，再动手
- 模板优先：kv3 头与写法从 addon 现有文件复制
- 文档优先：以官方文档与本地 SDK 类型定义为权威
- 验证优先：交付前运行完整性脚本

## 平台

| 平台 | 配置 |
|---|---|
| Claude Code | `.claude-plugin/plugin.json` |
| Cursor | `.cursor-plugin/plugin.json` |
| Codex | `.codex/INSTALL.md` |
| OpenCode | `.opencode/INSTALL.md` |
| Gemini CLI | `GEMINI.md` |

## 技能列表

| 技能 | 说明 |
|---|---|
| using-cs2-mapping | 入口：规则与路由 |
| cs2-hammer-mapping | 地图级工作流/实体/光照/发布/.vmap 程序化（⚠️ 默认建议模式，确认后才修改） |
| cs2-material-creation | 材质 `.vmat` |
| cs2-texture-creation | 纹理 `.vtex` |
| cs2-model-creation | 模型 `.vmdl` |
| cs2-particle-creation | 粒子 `.vpcf` |
| cs2-postprocess-creation | 滤镜 `.vpost` |
| cs2-sound-creation | 声音 `.vsndevts` |
| cs2-script-creation | 脚本 `cs_script` / `.js` |

## Red Flags（停止并检查）

| AI 的想法 | 正确做法 |
|---|---|
| "用户说得很清楚了，直接生成" | 先调用入口技能，再检查 addon 现有模板 |
| "PNG 直接放进去就能用" | 需要 `.vmat`/`.vtex` 配方文件 |
| "kv3 头我默写一个" | 从 addon 现有文件复制版本 GUID |
| "直接改二进制 .vmap" | 地图技能默认只给建议；用户确认后才修改 |
| "这个 API/属性凭记忆写" | 查官方文档与本地 SDK 类型定义 |

<EXTREMELY-IMPORTANT>
任何 CS2 地图或资产任务开始前，必须先调用 `skills/using-cs2-mapping/SKILL.md` 确定流程。
单一资产任务必须路由到对应专项技能，不允许跳过入口直接编造格式。
</EXTREMELY-IMPORTANT>

## 标准流程

1. 入口路由 → `using-cs2-mapping`（判断地图级 / 单一资产）
2. 地图级 → `cs2-hammer-mapping`：默认给建议与步骤，不修改文件；用户明确要求修改后才执行
3. 单一资产 → 对应专项技能（材质/纹理/模型/粒子/滤镜/声音/脚本）
4. 验证 → `scripts/check_skill_integrity.ps1`；地图交付前在 Hammer 中确认

## 版本

- 版本：1.0.0
- 更新日期：2026-08-25
