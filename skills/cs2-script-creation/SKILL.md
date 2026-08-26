---
name: cs2-script-creation
description: "创建或编辑 Counter-Strike 2 脚本（cs_script，JavaScript .js）：识别本地 point_script.d.ts，依据官方 Scripting API 与用户需求生成脚本，不涉及地图挂载。动手编写前必须先提出澄清问题。"
---

# CS2 脚本创作

只负责生成 `cs_script` 脚本（标准 JavaScript，ES Module）。使用前提：Agent 已打开目标 addon 文件夹。

## 核心原则

- 只识别本地官方类型定义 `content/csgo/maps/editor/zoo/scripts/point_script.d.ts`，依据其中的 API 签名与用户需求生成。
- 不读取其他模板或真实案例；不凭记忆编造签名与参数。

## 先提问

1. "脚本要实现什么逻辑？(倒计时/机关/BOSS/自定义玩法)"
2. "由什么触发？(实体输入/定时器/玩家或回合事件)"
3. "需要操作哪些实体？(targetname 列表)"

## 工作流

1. 定位本地 `point_script.d.ts`（`content/csgo/maps/editor/zoo/scripts/point_script.d.ts`）。
2. 提问；批量任务走批量模式。
3. 依据 API 签名编写 `.js`，放入 addon 的 `scripts/`。
4. 涉及自定义 HUD（custom_hud_layout）时：布局 XML 放 `panorama/layout/custom_game/`，样式 CSS 放 `panorama/styles/custom_game/`。

## 批量模式

1. 公共设置只问一次（触发方式、命名规则）。
2. 接受规则文件（脚本名 → 用途 → 触发/实体）。
3. 一次性输出全部脚本清单与内容。
4. 所有代码只依据本地 API 与规则生成。

## References

- [references/script-formats.md](references/script-formats.md) - 语言与本地 API 参考
- 官方：[Scripting API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API)

