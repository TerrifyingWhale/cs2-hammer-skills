# 脚本：cs_script 与 point_script

## 是什么

- `cs_script` 使用标准 JavaScript（`.js`，ES Module）。源文件放 `scripts/vscripts/`；`point_script` 实体的 `cs_script` 属性直接引用 `.js` 脚本。
- 官方模块导入：`import { Instance } from "cs_script/point_script";`。
- 只依据官方 API 与用户需求生成，不套用真实案例。

## 本地 API 参考（编写时以它为准）

- 官方类型定义：`content/csgo/maps/editor/zoo/scripts/point_script.d.ts`（从 addon 向上两级到 `content/` 再进入该路径）。
- 完整记录 `Instance`、事件回调、实体操作等签名与参数类型；不确定时先查它，不凭记忆编字段。

## 挂载

- `point_script` 实体 `cs_script` 填 `scripts/vscripts/<name>.js`；设置 `targetname` 供引用。
- 进游戏测试；控制台/日志中的脚本错误是主要排查手段。

## 官方文档

- [Scripting API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API)
- [Scripting](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting)
- [Hello Gordon](https://developer.valvesoftware.com/w/index.php?title=Counter-Strike_2_Workshop_Tools/Scripting/Hello_Gordon)
- [point_script](https://developer.valvesoftware.com/wiki/Point_script)
