# CS2 Hammer 地图创作套件 (CS2 Mapping Assistant)

把 CS2 地图创作从"一次性聊天"升级成可追踪、可恢复、可复用的工程化协作流程。

本套件面向使用 Source 2 Hammer / CS2 Workshop Tools 的地图作者：从 addon 结构、实体与光照，到材质、纹理、模型、粒子、滤镜、声音和脚本，全部按模块化技能组织。

## 项目定位

这不是一个"只会写几句资产代码"的提示词包，而是一套完整的 CS2 地图创作协作系统。任务开始前先检查当前打开的 addon、对齐目标与约束，再按任务类型路由到对应技能模块执行；批量资产生成走批量模式，公共设置只问一次。

## 核心能力

- 地图级工作流：addon 结构、实体设置、光照、发布、`.vmap` 程序化检查与批量刷子
- 材质与纹理：`.vmat` / `.vtex` 配方文件生成（csgo_complex 等常用着色器）
- 模型：`.vmdl` 生成，直接写路径引用，自动关联同名材质
- 粒子、滤镜、声音、脚本：`.vpcf` / `.vpost` / `.vsndevts` / `cs_script`
- 批量模式：一次问清公共设置，规则文件/文件夹级默认值批量生成
- 多平台适配：Claude Code / Cursor / Codex / OpenCode / Gemini CLI
- 质量门控：技能完整性脚本 + 交付前在 Hammer 中验证

## 适用平台

| 平台 | 配置文件 |
|---|---|
| Claude Code | `.claude-plugin/plugin.json` |
| Cursor | `.cursor-plugin/plugin.json` |
| Codex | `.codex/INSTALL.md` |
| OpenCode | `.opencode/INSTALL.md` |
| Gemini CLI | `GEMINI.md` |
| 其他 | `AGENTS.md` |

## 技能地图

| 场景 | 技能 |
|---|---|
| 入口与路由 | `skills/using-cs2-mapping/` |
| 地图工作流/实体/光照/发布/.vmap 程序化 | `skills/cs2-hammer-mapping/` |
| 材质（.vmat） | `skills/cs2-material-creation/` |
| 纹理定义（.vtex） | `skills/cs2-texture-creation/` |
| 模型（.vmdl） | `skills/cs2-model-creation/` |
| 粒子系统（.vpcf） | `skills/cs2-particle-creation/` |
| 滤镜（.vpost） | `skills/cs2-postprocess-creation/` |
| 自定义声音（.vsndevts） | `skills/cs2-sound-creation/` |
| 脚本（cs_script / .js） | `skills/cs2-script-creation/` |

## 标准协作流程（推荐）

1. 入口路由：说"帮我做 CS2 地图/材质/模型…"，套件会先调用 `using-cs2-mapping` 确定流程
2. 检查 addon：Agent 已打开目标 addon 文件夹，先按对应 reference 规范写，addon 现有文件仅作参考
3. 提问确认：专项技能先问必要问题（用途、贴图来源、批量设置），批量任务只问一次
4. 执行生成：按对应技能生成资产配方文件，保存后 Hammer 自动编译
5. 验证：修改技能后运行 `scripts/check_skill_integrity.ps1`；地图交付前在 Hammer 中打开确认

> 注意：地图技能（cs2-hammer-mapping）默认只给建议与步骤，不直接修改文件；用户明确要求修改后才执行。程序化 .vmap 编辑需先备份并在 Hammer 中验证。

## 质量门控

修改技能后先运行完整性检查：

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check_skill_integrity.ps1
```

## 安装

### 方式一：Git Clone

```bash
git clone https://github.com/TerrifyingWhale/cs2-hammer-skills.git
cd cs2-hammer-skills
```

### 各平台安装

- Codex：参考 `.codex/INSTALL.md`
- OpenCode：参考 `.opencode/INSTALL.md`
- Claude Code / Cursor：作为插件加载 `.claude-plugin/plugin.json` / `.cursor-plugin/plugin.json`
- 其他：将 `skills/` 下的技能文件夹放入对应平台的 skills 目录

## 仓库结构

```text
cs2-hammer-skills/
├── SKILL.md                    # 主入口（兼容旧平台）
├── AGENTS.md                   # 通用代理配置
├── CLAUDE.md                   # Claude 项目说明
├── GEMINI.md                   # Gemini CLI 配置
├── CHANGELOG.md                # 版本记录
├── .codex/                     # Codex 安装指南
├── .opencode/                  # OpenCode 安装指南
├── .claude-plugin/             # Claude Code 配置
├── .cursor-plugin/             # Cursor 配置
├── hooks/                      # 会话启动脚本
├── skills/                     # 技能模块目录（入口 + 8 个专项）
├── templates/                  # 资产/结构模板
└── scripts/                    # 工具脚本
```

## 版本

- 版本：1.0.3
- 更新日期：2026-08-26
