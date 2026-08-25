---
name: cs2-sound-creation
description: "创建或编辑 Counter-Strike 2 自定义声音（.vsndevts 事件 + sounds/ 音频源），用于 Source 2 Hammer（CS2 Workshop Tools），包括事件定义、音量/音高/循环设置与实体触发。动手编写前必须先提出澄清问题。"
---

# CS2 声音创作

创建/编辑自定义声音：`soundevents_addon.vsndevts` 定义事件 + `sounds/` 音频源。使用前提：Agent 已打开目标 addon 文件夹。

## 先提问

1. "声音用在什么场景？(环境/音效/警报/BOSS/音乐)"
2. "音频素材有现成的吗？(wav/mp3 路径)"
3. "循环、随机还是单次？定位音还是全局音？"

## 修改规则（只追加不删除）

- 在 `soundevents_addon.vsndevts` 底部、最后 `}` 前**追加**，保留所有已有代码。
- **事件名直接写文件名**（去扩展名，如 `radio.mp3` → `"radio"`），不加前缀。
- 音乐用 `csgo_music` 模板、游戏音效用 `csgo_mega` 模板（与 mp3/wav 格式无关）。
- **音乐默认不循环**，不添加循环设置。
- 只按本技能模板生成，不读其他文档。

## 工作流

1. 检查 addon `soundevents/`、`sounds/` 现有约定。
2. 提问；批量任务走批量模式。
3. 音频放 `sounds/`，在 vsndevts 底部追加事件。
4. 地图用 `point_soundevent` 触发；Hammer 自动编译。

## 批量模式

1. 公共设置只问一次（循环/定位/音量）。
2. 接受规则文件（文件名 → 事件名 → 类型/循环/音量）。
3. 一次性输出全部事件定义与文件清单。
4. 命名与组织按需求与惯例，addon 现有目录仅作参考。

## References

- [references/sound-formats.md](references/sound-formats.md) - 事件模板（音乐/音效）与只追加规则
