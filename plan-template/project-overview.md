# 项目概览

> 用途：初始化项目范围，减少后续上下文丢失。

## 一、基础信息

- 项目名称（addon）：`content/csgo_addons/<addon>/`
- 地图名称：
- 创建日期：
- 最后更新：
- 当前负责人：

## 二、项目定位

- 玩法类型（爆破 / 休闲 / 娱乐 / 僵尸逃跑 / 练习图 / 其他）：
- 地图规模（区域数 / 面积量级）：
- 目标平台（官方匹配 / 社区服 / 练习）：
- 截止日期：

## 三、本项目约束

- 命名规则（targetname / 资产文件命名）：
- 性能预算（同屏粒子数、实体数、复杂度）：
- 文件组织约定：
- 发布方式（Workshop / addon 分享）：

## 四、工作偏好（必须记录）

- 资产来源（自带贴图/模型，还是用 addon 现有文件）：
- 是否使用官方模板与官方文档写法：
- 光照方式（路径追踪 / 传统）：
- 其他风格偏好：

## 五、设计要点

- 核心玩法：
- 关键区域与传送点：
- 实体与逻辑清单（触发器、逻辑、BOSS、脚本）：
- 资产清单（材质 / 纹理 / 模型 / 粒子 / 滤镜 / 声音 / 脚本）：

## 六、当前阶段

- 当前阶段：
- 当前任务：
- 下一个里程碑：

## 七、目录约定

```text
content/csgo_addons/<addon>/
├── maps/            # .vmap 源地图
├── materials/       # .vmat / .vtex / 贴图
├── models/          # .vmdl / .fbx / .dmx
├── particles/       # .vpcf
├── postprocess/     # .vpost
├── soundevents/     # .vsndevts
├── sounds/          # 音频源文件
└── scripts/vscripts/ # cs_script (.js)

项目工作目录/
└── plan/
    ├── project-overview.md
    ├── stage-gates.md
    ├── progress.md
    ├── outline.md
    └── notes.md
```

## 八、初始化确认清单

- [ ] 已与用户确认 addon 与地图名称
- [ ] 已与用户确认玩法类型与范围
- [ ] 已确认资产来源与命名规则
- [ ] 已确定本轮优先任务
