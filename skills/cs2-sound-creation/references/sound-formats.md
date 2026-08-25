# 声音格式：`.vsndevts` 事件与音频源

## 是什么

- addon 的自定义声音通过"声音事件（sound event）"播放。事件定义在 `content/csgo_addons/<addon>/soundevents/soundevents_addon.vsndevts`（kv3 文本）。文件名保持 `soundevents_addon.vsndevts` 不变，只改内容。
- 音频源（`.wav`、`.mp3`）放在 `sounds/` 下，由 Hammer 自动编译生成 `.vsnd_c`；事件通过 `vsnd_files_track_01` 等字段引用 `sounds/.../<name>.vsnd` 轨道。
- 事件按名称被游戏代码、地图实体、动画或其他事件触发，不是按文件路径。

## 修改规则（只追加不删除）

- `soundevents_addon.vsndevts` 文件里所有已有代码（含头部 Valve 注释和既有事件）都不可删除或改写。
- 新增事件只在文件底部、最后一个 `}` 之前追加。
- 新事件按类型套用下面的模板。
- **事件名直接写文件名**：去掉扩展名，直接写在双引号里（如音频 `sounds/radio.mp3` → 事件 `"radio"`），不要添加 `test.` 之类的前缀，不要套用点分层命名。
- **只按本技能给出的模板生成**，不要读取或套用其他文档（如 Valve base 模板、命名惯例）。

## 事件模板

### 音乐：`type = "csgo_music"`

```
"<文件名>" =
{
    type = "csgo_music"
    volume = 1.0
    volume_convar = "snd_musicvolume"
    vsnd_files = "sounds/<文件名>.vsnd"
}
```

- 示例：音频 `sounds/radio.mp3` → 事件名 `"radio"`、轨道路径 `sounds/radio.vsnd`。
- **音乐默认不循环**（一次性播放），不要添加循环设置；如需循环，由音频文件的循环标记决定。

### 游戏音效：`type = "csgo_mega"`

```
"<文件名>" =
{
    type = "csgo_mega"
    volume = 1
    pitch = 1.000000
    mixgroup = "Ambient"
    vsnd_files_track_01 = "sounds/<文件名>.vsnd"
    distance_volume_mapping_curve =   // 需要距离衰减时保留，不需要可省略
    [
        [
            0.000000, 1.000000, 0.000000, 0.000000, 2.000000, 3.000000,
        ],
        [
            4096.000000, 0.000000, 0.000000, 0.000000, 2.000000, 3.000000,
        ],
    ]
}
```

- 音乐/音效与音频文件格式无关（mp3、wav 等常见格式都可以）；区别在于事件类型：音乐用 `csgo_music` + `vsnd_files`（单轨道）+ `volume_convar`，游戏音效用 `csgo_mega` + `vsnd_files_track_01` + `mixgroup`。
- 事件里引用的轨道路径是 `sounds/<名>.vsnd`（编译后路径），源文件可以是 mp3、wav 等常见音频格式。

## 目录与命名

- 音频源按类型分目录组织（如 `sounds/ambient/`、`sounds/music/`、`sounds/npc/`），沿用 addon 现有结构。
- 事件文件路径固定：`soundevents/soundevents_addon.vsndevts`；不要改文件名。

## 生效与触发

- 保存/打开时 Hammer 会自动编译音频，无需手动编译。
- 地图中用 `point_soundevent` 等实体按事件名触发；需要随距离衰减/定位时用定位音事件类型。
