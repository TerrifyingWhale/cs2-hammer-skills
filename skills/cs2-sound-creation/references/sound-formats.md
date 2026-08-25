# 声音格式：`.vsndevts` 事件与音频源

## 是什么

- 事件定义在 `content/csgo_addons/<addon>/soundevents/soundevents_addon.vsndevts`（kv3 文本），文件名保持不变。
- 音频源（wav/mp3）放 `sounds/` 下，由 Hammer 自动编译生成 `.vsnd_c`；事件通过 `vsnd_files` / `vsnd_files_track_01` 等字段引用 `sounds/.../<文件名>.vsnd` 轨道。
- 事件按名称被游戏代码、地图实体、动画触发，不是按文件路径。

## 修改规则（只追加不删除）

- 保留文件中所有已有代码（含头部注释和既有事件），只在底部、最后 `}` 之前追加。
- **事件名直接写文件名**（去扩展名，如 `sounds/radio.mp3` → 事件 `"radio"`），不加前缀、不套用点分层命名。
- 只按本技能模板生成，不读取其他文档。

## 事件模板

### 音乐：`type = "csgo_music"`（默认不循环，不添加循环设置）

```
"<文件名>" =
{
    type = "csgo_music"
    volume = 1.0
    volume_convar = "snd_musicvolume"
    vsnd_files = "sounds/<文件名>.vsnd"
}
```

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

音乐/音效与音频文件格式无关；区别在事件类型：音乐 `csgo_music` + `vsnd_files` + `volume_convar`，游戏音效 `csgo_mega` + `vsnd_files_track_01` + `mixgroup`。

## 目录与触发

- 音频源按类型分目录（`sounds/ambient/`、`sounds/music/` 等），沿用 addon 现有结构。
- 地图用 `point_soundevent` 等实体按事件名触发；Hammer 自动编译。

## 官方文档

- [Addon Sounds](https://developer.valvesoftware.com/wiki/Counter-Strike_2_Workshop_Tools/Addon_Sounds)
