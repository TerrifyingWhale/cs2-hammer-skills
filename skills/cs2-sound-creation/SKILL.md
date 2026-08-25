---
name: cs2-sound-creation
description: "创建或编辑 Counter-Strike 2 自定义声音（.vsndevts 事件 + sounds/ 音频源），用于 Source 2 Hammer（CS2 Workshop Tools），包括事件定义、音量/音高/循环设置与实体触发。动手编写前必须先提出澄清问题。"
---

# CS2 声音创作

当任务是创建或编辑 CS2 自定义声音时使用本技能：把 wav/mp3 音频接进 addon、在 `soundevents_addon.vsndevts` 里定义声音事件（sound event）、配置音量/音高/循环，或用地图实体触发事件。地图级工作（实体、发布）属于 CS2 地图创作技能（cs2-hammer-mapping）。

## 先提问再动手——绝不猜测参数

在检查目标 addon 并收集到以下问题的答案之前，不要编写声音事件：

1. "这个声音用在什么场景？(环境音/音效/警报/BOSS/音乐/语音)"
2. "音频素材有现成的吗？(wav/mp3 路径；没有的话需要用户提供)"
3. "需要循环播放、随机播放还是单次触发？"
4. "是定位音(带位置、随距离衰减)还是全局音？"

使用前提：Agent 已在内部打开当前地图对应的 addon 文件夹，因此不需要询问用户"用在哪张地图/哪个 addon"，直接以该文件夹中的现有文件为准。

**能推断的不要问。** 先看 addon 现有 `soundevents/` 和 `sounds/` 目录：事件命名习惯、目录组织、base 模板用法都从现有文件里总结。

## 修改规则（只追加不删除）

- 修改 `soundevents_addon.vsndevts` 时，**保留文件里所有已有代码**（包括文件头部的注释和所有现有事件），只在文件底部、最后的 `}` 之前**追加**新事件。
- 不要删除、改写或移动已有的任何代码块，不要重写整个文件。
- 新事件按类型套用模板：音乐用 `csgo_music`、游戏音效用 `csgo_mega`（与音频文件格式无关，mp3/wav 等均可），模板见 [references/sound-formats.md](references/sound-formats.md)。
- **事件名直接写文件名**（去掉扩展名，例如 `radio.mp3` → 事件名 `"radio"`），不加任何前缀，不套用点分层命名；只按模板生成，不读取其他文档。
- **音乐默认不循环**（一次性播放），不要添加循环设置；如需循环，由音频文件的循环标记决定。

## 工作流

1. 检查 addon 的 `soundevents/`（事件文件）和 `sounds/`（音频源）目录，找最接近的现有事件作模板。
2. 提出上面的问题并收集答案；批量任务进入"批量模式"。
3. 把音频源放到 `sounds/` 下（可按类型分子目录），在 `soundevents_addon.vsndevts` 底部**追加**事件（音乐用 `csgo_music` 模板、游戏音效用 `csgo_mega` 模板），不删除任何已有代码。
4. 在地图中用 `point_soundevent` 等实体按事件名触发；保存后 Hammer 会自动编译。
5. 游戏中验证音量、循环与触发逻辑。

## 批量模式（Batch mode）

当用户需要一次添加多个音效（例如一整批警报/环境音）时：

1. 公共设置只问一次：循环方式、是否定位音、音量级别。
2. 接受规则文件：文件名 → 事件名 → 类型/循环/音量。
3. 一次性输出全部事件定义与文件清单。
4. 命名与组织以 addon 现有 `soundevents/`/`sounds/` 目录为准。

## References

- [references/sound-formats.md](references/sound-formats.md) - `.vsndevts` 事件模板（音乐/音效）、只追加不删除规则、目录组织与触发步骤。
