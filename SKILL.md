---
name: cs2-mapping-assistant
description: Use when creating, editing, checking, or troubleshooting Counter-Strike 2 maps and assets with Source 2 Hammer - routes to the specialized CS2 mapping skill suite
allowed-tools: Read Write Edit Bash WebSearch
---

# CS2 Hammer 地图创作套件 (CS2 Mapping Assistant)

面向 Counter-Strike 2（Source 2 Hammer / CS2 Workshop Tools）地图创作的模块化技能套件。入口路由、专项技能、计划模板与质量门控组成一套完整流程。

## 哲学原则

- **流程优于即兴** — 先检查 addon、先提问确认，再动手
- **模板优于手写** — 从 addon 现有文件复制 kv3 版本 GUID 与既有写法
- **文档优于记忆** — 以官方文档与本地 SDK 类型定义（如 `point_script.d.ts`）为权威
- **验证优于声称** — 交付前运行完整性脚本确认

## 新架构（v1.0）

本套件采用模块化技能架构，支持多平台：

| 平台 | 配置 |
------|------|
| Claude Code | `.claude-plugin/plugin.json` |
| Cursor | `.cursor-plugin/plugin.json` |
| Codex | `.codex/INSTALL.md` |
| OpenCode | `.opencode/INSTALL.md` |
| Gemini CLI | `GEMINI.md` |

## 技能列表

### 核心流程技能

| 技能 | 路径 | 说明 |
|------|------|------|
| using-cs2-mapping | `skills/using-cs2-mapping/` | 入口技能，规则和路由 |
| cs2-hammer-mapping | `skills/cs2-hammer-mapping/` | 地图级工作流、实体、光照、发布、.vmap 程序化处理 |

### 资产创作技能

| 技能 | 路径 | 说明 |
|------|------|------|
| cs2-material-creation | `skills/cs2-material-creation/` | 材质（`.vmat`） |
| cs2-texture-creation | `skills/cs2-texture-creation/` | 纹理定义（`.vtex`） |
| cs2-model-creation | `skills/cs2-model-creation/` | 模型（`.vmdl`） |
| cs2-particle-creation | `skills/cs2-particle-creation/` | 粒子系统（`.vpcf`） |
| cs2-postprocess-creation | `skills/cs2-postprocess-creation/` | 滤镜（`.vpost`） |
| cs2-sound-creation | `skills/cs2-sound-creation/` | 自定义声音（`.vsndevts`） |
| cs2-script-creation | `skills/cs2-script-creation/` | 脚本（`cs_script` / `.js`） |

## Red Flags（停止并检查）

### 流程类 Red Flags

| AI 的想法 | 正确做法 |
|----------|----------|
| "用户说得很清楚了，直接生成" | 先调用 `using-cs2-mapping` 确定流程与专项技能 |
| "这是简单任务，不需要计划" | 地图项目需要 `plan/` 记录 |
| "直接改二进制 .vmap" | 先用 `dmxconvert` 转成文本再改 |
| "先把内容写完再说格式" | 先在 addon 中找同类型现有文件作为模板 |
| "这个实体属性我凭记忆写" | 查官方实体列表与本地 SDK 类型定义 |

### 资产类 Red Flags

| AI 的想法 | 正确做法 |
|----------|----------|
| "PNG 直接放进去引擎就能用" | 需要 `.vmat`/`.vtex` 配方文件，由 Hammer 自动编译 |
| "kv3 文件头我默写一个" | 从 addon 现有文件复制版本 GUID |
| "有 metal/roughness 图就加标志位" | 只在用户提供对应贴图时加，不要臆测 |
| "vmdl 需要命令行编译" | Hammer 打开/保存时自动编译，无需手动编译 |
| "50 个材质逐个问参数" | 进入批量模式，公共设置只问一次 |

### 验证类 Red Flags

| AI 的想法 | 正确做法 |
|----------|----------|
| "应该写完了" | 运行 `scripts/check_skill_integrity.ps1` 确认 |
| "dmxconvert 能解析就行" | 往返成功 ≠ Hammer 能打开，最终必须让用户在 Hammer 验证 |
| "我很确信格式没错" | 确信 ≠ 证据，对照官方文档与 addon 现有文件 |

<EXTREMELY-IMPORTANT>
任何 CS2 地图或资产任务开始前，必须先调用 `skills/using-cs2-mapping/SKILL.md` 确定流程。
单一资产任务必须路由到对应专项技能，不允许跳过入口直接编造格式。
</EXTREMELY-IMPORTANT>

## 标准流程

1. **入口路由** → 调用 `using-cs2-mapping`
   - 确认任务类型（地图级 / 单一资产）
   - 检查当前打开的 addon 文件夹
2. **地图级任务** → 调用 `cs2-hammer-mapping`
   - 实体、光照、发布、.vmap 程序化处理
3. **资产任务** → 调用对应专项技能
   - 材质/纹理/模型/粒子/滤镜/声音/脚本
4. **验证** → 运行 `scripts/check_skill_integrity.ps1`
   - 修改技能后必须运行
   - 地图交付前让用户在 Hammer 中打开确认

## 版本信息

- **版本**：1.0.0
- **更新日期**：2026-08-25
