# Changelog

所有重要更改都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

## [1.0.3] - 2026-08-26

### 变更

- 脚本技能精简为只负责脚本生成：识别本地 point_script.d.ts 后生成，移除地图挂载与放置说明。
- 所有资产生成统一为先按 reference 规范写，addon 现有文件仅作参考。
- 粒子、滤镜技能改为按用户需求自己写，现有文件仅作参考；纹理（.vtex）直接按 reference 模板生成。
- `<name>` 占位符统一改为 `<文件名>`；脚本引用后缀统一为 `.js`。
- 滤镜技能移除批量模式；脚本技能移除复制 point_script.d.ts / tsconfig.json 的说明。
- 统一各技能格式（先提问、批量模式、参考结构），并去除“同理”等措辞。

## [1.0.0] - 2026-08-25

### 新增

- 8 个专项技能：地图（cs2-hammer-mapping）、材质（cs2-material-creation）、纹理（cs2-texture-creation）、模型（cs2-model-creation）、粒子（cs2-particle-creation）、滤镜（cs2-postprocess-creation）、声音（cs2-sound-creation）、脚本（cs2-script-creation）。
- 入口路由技能 `using-cs2-mapping`，用于确定流程并路由到对应专项技能。

#### 多平台适配
- 添加 `.claude-plugin/plugin.json` - Claude Code 插件配置
- 添加 `.cursor-plugin/plugin.json` - Cursor 插件配置
- 添加 `.codex/INSTALL.md` - Codex 安装指南
- 添加 `.opencode/INSTALL.md` - OpenCode 安装指南
- 添加 `GEMINI.md` - Gemini CLI 配置
- 添加 `AGENTS.md` - 通用代理配置

#### Hooks 机制
- 添加 `hooks/session-start` - 会话启动脚本
- 添加 `hooks/hooks.json` - Claude Code hooks 配置
- 添加 `hooks/hooks-cursor.json` - Cursor hooks 配置
- 添加 `hooks/run-hook.cmd` - Windows 兼容脚本

#### 质量与模板
- 添加 `scripts/check_skill_integrity.ps1`，用于技能完整性验证（结构、frontmatter、交叉引用、版本一致性、禁用词）。
- 添加 `scripts/init_plan.ps1` / `scripts/init_plan.sh`，用于从 `plan-template/` 初始化地图项目计划。
- 添加 `plan-template/`：项目概览、进度追踪、阶段门禁、笔记、地图大纲。
- 添加 `templates/`：addon 目录结构模板与刷子盒子示例。

