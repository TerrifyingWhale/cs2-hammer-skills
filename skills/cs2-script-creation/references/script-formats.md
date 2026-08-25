# 脚本：cs_script 与 point_script

## 是什么

- CS2 的玩法脚本系统是 `cs_script`，脚本语言就是标准 JavaScript（`.js`，ES Module 语法）。
- 源文件放在 `scripts/vscripts/` 目录下；Hammer 中 `point_script` 实体的 `cs_script` 属性引用编译后的资源（`.vjs`，源文件为 `.js`）。
- 官方提供的脚本模块导入写法：`import { Instance } from "cs_script/point_script";`（详见官方 Hello Gordon 入门文档）。
- 本技能不使用真实 addon 案例；所有代码只依据官方 Scripting API 文档和用户需求生成。
- Pulse 可视化脚本目前不对最终用户开放，直接用 JavaScript 编写。

## 编写原则

- 语言：JavaScript（ES Module），用 `import` / `export` 组织代码。
- 只调用官方 Scripting API 中存在的函数与属性；不确定的 API 先查官方文档确认签名，不要凭记忆编造。
- 逻辑组织（常量配置、类、函数、定时器等）按用户需求和常规 JavaScript 写法，不照搬真实案例。
- 文件头、导入语句、模块名一律以官方文档为准。

## 官方 API 参考（本地类型定义）

- 官方 SDK 自带完整的 API 类型定义：`content/csgo/maps/editor/zoo/scripts/point_script.d.ts`（在游戏 content 根目录下；从当前 addon 文件夹向上两级到 `content/`，再进入 `csgo/maps/editor/zoo/scripts/`）。
- 该文件完整记录 `cs_script` 模块（`"cs_script/point_script"`）的 API：`Instance`、事件回调、实体操作、工具函数等，包含函数签名与参数类型。编写脚本时以它为准，不要凭记忆编字段。
- 同目录的 `tsconfig.json` 是官方为脚本编辑配置的；把 `point_script.d.ts` 和 `tsconfig.json` 复制到自己脚本目录旁，编辑器就能提供补全与类型检查。

## point_script 挂载

- 在 Hammer 放置 `point_script` 实体，`cs_script` 属性填脚本资源路径（`scripts/vscripts/<name>.vjs`，源文件为 `.js`）。
- 给实体设置 `targetname`，供其他实体/脚本引用。
- 进游戏测试；控制台或日志中的脚本错误是主要排查手段。

## 官方文档

- [Counter-Strike 2 Workshop Tools/Scripting/API](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting/API)
- [Counter-Strike 2 Workshop Tools/Scripting](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Scripting)
- [Hello Gordon: Getting Started with JavaScript in Counter-Strike 2](https://developer.valvesoftware.com/w/index.php?title=Counter-Strike_2_Workshop_Tools/Scripting/Hello_Gordon)
- [point_script](https://developer.valvesoftware.com/wiki/Point_script)
