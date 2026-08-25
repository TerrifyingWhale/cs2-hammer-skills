---
name: cs2-script-creation
description: "创建或编辑 Counter-Strike 2 脚本（cs_script，JavaScript .js）与 point_script 挂载，用于 Source 2 Hammer（CS2 Workshop Tools），包括事件、实体交互与 Scripting API 调用。动手编写前必须先提出澄清问题。"
---

# CS2 脚本创作

当任务是创建或编辑 CS2 游戏脚本时使用本技能：编写 `cs_script` 逻辑（倒计时、机关、BOSS 行为、自定义玩法）、用 `point_script` 实体挂载到地图、调用官方 Scripting API 操作实体。地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）。

## 核心原则

- CS2 脚本就是标准 JavaScript（`.js`，ES Module 语法），不是其他脚本语言。
- 代码只依据官方 Scripting API 文档和用户需求生成，不套用真实 addon 的案例代码。
- 需要某个 API 的用法时，直接打开官方类型定义文件 `content/csgo/maps/editor/zoo/scripts/point_script.d.ts`（游戏 content 根目录下）确认签名与参数，不要凭记忆编造。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写脚本：

1. "脚本要实现什么逻辑？(倒计时/触发机关/BOSS 行为/武器/自定义游戏模式)"
2. "脚本由什么触发？(实体输入/定时器/玩家事件/回合事件)"
3. "脚本需要操作哪些实体？(有 targetname 的实体列表)"

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

**能推断的不要问。** 检查 addon 的 `scripts/vscripts/` 目录和地图里的 `point_script` 挂载方式，只用于确认路径约定；代码本身按官方 API 与用户需求编写。

## 工作流

1. 检查 addon 的 `scripts/vscripts/` 目录与地图里的 `point_script` 实体（确认脚本路径约定）。
2. 提出上面的问题并收集答案；批量任务进入"批量模式"。
3. 编写前打开 `content/csgo/maps/editor/zoo/scripts/point_script.d.ts` 确认要用的 API，再根据官方 Scripting API 与用户需求编写 `.js` 脚本（ES Module），放到 `scripts/vscripts/`。
4. 在 Hammer 放置 `point_script` 实体，`cs_script` 属性填脚本资源路径（如 `scripts/vscripts/<name>.vjs`，源文件为 `.js`）。
5. 保存后在游戏内用 `map <mapname>` 测试逻辑，确认无报错并验证行为。

## 批量模式（Batch mode）

当用户需要一次编写多个脚本（例如一组 BOSS/机关逻辑）时：

1. 公共设置只问一次：触发方式、实体命名规则。
2. 接受规则文件：脚本名 → 用途 → 触发/实体。
3. 一次性输出全部脚本与 point_script 配置清单。
4. 所有代码同样只依据官方 API 与用户提供的规则生成。

## References

- [references/script-formats.md](references/script-formats.md) - cs_script 语言与文件组织、point_script 挂载、API 文档入口。
- 官方：[Counter-Strike 2 Workshop Tools/Scripting/API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API) 和 [Scripting](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting)。
