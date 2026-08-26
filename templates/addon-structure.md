# Addon 目录结构模板

CS2 addon 源文件位于 `content/csgo_addons/<addon>/`，编译后的资源由 Hammer 自动生成到 `game/csgo_addons/<addon>/`。

```text
content/csgo_addons/<addon>/
├── maps/
│   └── <map>.vmap              # 地图源文件
├── materials/                  # 材质与纹理
│   ├── <文件名>.vmat
│   └── <文件名>.vtex
├── models/                     # 模型
│   └── <文件名>.vmdl
├── particles/                  # 粒子系统
│   └── <文件名>.vpcf
├── postprocess/                # 滤镜
│   └── <文件名>.vpost
├── soundevents/                # 声音事件定义
│   └── soundevents_addon.vsndevts
├── sounds/                     # 音频源文件（mp3/wav 等）
├── scripts/                    # cs_script 源文件（.js）
└── panorama/
    ├── layout/custom_game/     # 自定义 HUD 布局（XML）
    └── styles/custom_game/     # 自定义 HUD 样式（CSS）
```

使用约定：

- 资产配方文件（`.vmat` / `.vtex` / `.vmdl` / `.vpcf` / `.vpost` / `.vsndevts`）保存后由 Hammer 自动编译，无需手动运行编译器。
- kv3 文件头版本 GUID 按 reference 模板写，不要凭记忆手写。
- 编写任何新资产前，先按对应 reference 规范写；addon 现有文件仅作参考。
