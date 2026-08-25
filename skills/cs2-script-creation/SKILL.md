---
name: cs2-script-creation
description: "创建或编辑 Counter-Strike 2 脚本（cs_script，JavaScript .js）与 point_script 挂载，用于 Source 2 Hammer（CS2 Workshop Tools），包括事件、实体交互与 Scripting API 调用。动手编写前必须先提出澄清问题。"
---

# CS2 脚本创作

创建/编辑 `cs_script`（标准 JavaScript，ES Module）。使用前提：Agent 已打开目标 addon 文件夹。

## 核心原则

- 只依据官方 Scripting API 与用户需求生成，不套用真实案例。
- 需要 API 时直接打开官方类型定义 `content/csgo/maps/editor/zoo/scripts/point_script.d.ts` 确认签名与参数，不凭记忆编造。

## 先提问

1. "脚本要实现什么逻辑？(倒计时/机关/BOSS/自定义玩法)"
2. "由什么触发？(实体输入/定时器/玩家或回合事件)"
3. "需要操作哪些实体？(targetname 列表)"

## 工作流

1. 检查 addon `scripts/vscripts/` 与地图里的 `point_script` 挂载（确认路径约定）。
2. 提问；批量任务走批量模式。
3. 打开 `point_script.d.ts` 确认 API，编写 `.js` 放入 `scripts/vscripts/`。
4. Hammer 放 `point_script`，`cs_script` 填 `scripts/vscripts/<name>.vjs`。
5. 游戏内 `map <mapname>` 测试。

## 批量模式

1. 公共设置只问一次（触发方式、命名规则）。
2. 接受规则文件（脚本名 → 用途 → 触发/实体）。
3. 一次性输出全部脚本与配置清单。
4. 所有代码只依据官方 API 与规则生成。

## References

- [references/script-formats.md](references/script-formats.md) - 语言/挂载/本地 API 参考
- 官方：[Scripting API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API)、[Scripting](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting)
