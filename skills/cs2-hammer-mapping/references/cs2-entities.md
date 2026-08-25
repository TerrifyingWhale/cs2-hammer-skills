# CS2 实体速查

## 权威来源

- 官方完整实体列表：[List of Counter-Strike 2 Entities](https://developer.valvesoftware.com/wiki/List_of_Counter-Strike_2_Entities)。该页面标注为"不完整"，按 FGD 文件分组（`base.fgd`、`lights.fgd`、`lights2.fgd`、`csgo.fgd`），每个实体通常还有独立页面说明属性、输入输出与用途。
- 使用任何不熟悉的实体前，先查官方页面或对应实体页（例如 [trigger_multiple (Source 2)](https://developer.valvesoftware.com/w/index.php?title=Trigger_multiple_(Source_2))、[point_template](https://developer.valvesoftware.com/w/index.php?title=Point_template)）。CS2 的实体名称与属性不同于 Source 1 / CS:GO，不要照搬旧习惯。
- Hammer 中的 FGD 定义（如 [Counter-Strike 2.fgd](https://developer.valvesoftware.com/w/index.php?title=Counter-Strike_2.fgd)）是编辑器里属性提示的直接来源。

## 常见实体分类（真实 CS2 地图中常见）

以下按用途分组，供快速定位；具体属性、输入/输出以官方页面为准。

| 类别 | 实体 |
|---|---|
| 出生点与玩家 | `info_player_terrorist`、`info_player_counterterrorist`、`info_player_start`、`team_select`、`game_money` |
| 逻辑 | `logic_auto`、`logic_relay`、`logic_timer`、`logic_branch`、`logic_case`、`logic_compare`、`logic_measure_movement`、`math_counter`、`point_template` |
| 触发器 | `trigger_multiple`、`trigger_once`、`trigger_hurt`、`trigger_push`、`trigger_teleport` |
| 机关与移动 | `func_button`、`func_breakable`、`func_rotating`、`func_movelinear`、`func_tracktrain`、`func_physbox`、`func_water`、`path_track`、`phys_keepupright`、`phys_thruster` |
| 模型实体 | `prop_static`、`prop_dynamic`、`prop_physics`、`prop_physics_multiplayer`、`prop_ragdoll` |
| 光照与天空 | `light_barn`、`light_omni2`、`light_rect`、`env_combined_light_probe_volume`、`env_cs_place`、`skybox_reference` |
| 环境与氛围 | `env_fog_controller`、`env_wind`、`env_shake`、`env_spark`、`env_explosion`、`env_physexplosion`、`env_fade`、`env_viewpunch`、`env_hudhint`、`env_particle_glow`、`post_processing_volume`、`water_lod_control`、`visibility_hint` |
| 粒子与特效 | `info_particle_system`、`info_particle_target` |
| 声音 | `point_soundevent` |
| 脚本与服务器 | `point_script`、`point_servercommand`、`point_worldtext` |
| 武器与物品 | `weapon_ak47`、`weapon_elite`、`weapon_hegrenade`、`weapon_molotov`、`weapon_negev`、`weapon_healthshot` |
| 过滤器 | `filter_activator_name`、`filter_activator_team`、`filter_activator_context`、`filter_activator_attribute_int` |
| 目标点与传送 | `info_target`、`info_teleport_destination` |
| 实体生成 | `env_entity_maker` |

## 使用要点

- 实体分 point（点实体）与 brush（刷实体）两类；刷实体需要几何体，点实体只有一个位置。
- 在 `.vmap` 的实体数据中，每个实体有 `classname`、`targetname`、`spawnflags` 等属性（位于 `EditGameClassProps` 块内）。命名规则（targetname）沿用目标 addon 的现有习惯。
- 需要批量统计或检查地图实体（例如统计某个类的数量）时，用 [working-with-vmap-files.md](working-with-vmap-files.md) 里的转换方法，不要直接搜二进制文件。
- 计划使用某个实体前，先确认它属于哪类（触发器/逻辑/环境…），再查官方页面拿属性与输入输出，最后对照 addon 中已有实体确认写法。
