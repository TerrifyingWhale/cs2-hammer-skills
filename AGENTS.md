# CS2 Hammer 地图创作套件

本项目包含 Counter-Strike 2 地图创作技能集。当用户提出与 CS2 地图或资产相关的任务时，请调用相应技能。

## 技能列表

| 技能名称 | 路径 | 用途 |
|----------|------|------|
| using-cs2-mapping | skills/using-cs2-mapping/SKILL.md | 入口技能，定义规则和路由 |
| cs2-hammer-mapping | skills/cs2-hammer-mapping/SKILL.md | 地图工作流、实体、光照、发布、.vmap 程序化处理 |
| cs2-material-creation | skills/cs2-material-creation/SKILL.md | 材质（.vmat） |
| cs2-texture-creation | skills/cs2-texture-creation/SKILL.md | 纹理定义（.vtex） |
| cs2-model-creation | skills/cs2-model-creation/SKILL.md | 模型（.vmdl） |
| cs2-particle-creation | skills/cs2-particle-creation/SKILL.md | 粒子系统（.vpcf） |
| cs2-postprocess-creation | skills/cs2-postprocess-creation/SKILL.md | 滤镜（.vpost） |
| cs2-sound-creation | skills/cs2-sound-creation/SKILL.md | 自定义声音（.vsndevts / sounds/） |
| cs2-script-creation | skills/cs2-script-creation/SKILL.md | 脚本（cs_script / .js） |

## 使用方式

1. 用户提出 CS2 地图或资产任务
2. 调用 `using-cs2-mapping` 技能确定流程
3. 地图级任务调用 `cs2-hammer-mapping`；单一资产任务路由到对应专项技能
4. 按技能指引完成检查、提问、生成与验证

## 核心规则

- 任何地图/资产任务前先调用 `using-cs2-mapping` 确定流程
- 使用前提：Agent 已打开目标 addon 文件夹，不询问"用在哪张地图/哪个 addon"
- 资产配方文件（.vmat/.vtex/.vmdl/.vpcf/.vpost/.vsndevts）由 Hammer 自动编译，不手动编译
- kv3 文件头版本 GUID 从 addon 现有文件复制，不凭记忆手写
- 批量资产生成走批量模式，公共设置只问一次
- skill 改造后运行 `scripts/check_skill_integrity.ps1`
- 不编造资产格式与实体属性，以官方文档和本地 SDK 文件为准
