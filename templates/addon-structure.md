# Addon 目录结构模板

CS2 addon 源文件位于 `content/csgo_addons/<addon>/`，编译后的资源由 Hammer 自动生成到 `game/csgo_addons/<addon>/`。

```text
content/csgo_addons/<addon>/
├── maps/
│   └── <map>.vmap              # 地图源文件
├── materials/                  # 材质与纹理
│   ├── <name>.vmat
│   └── <name>.vtex
├── models/                     # 模型
│   └── <name>.vmdl
├── particles/                  # 粒子系统
│   └── <name>.vpcf
├── postprocess/                # 滤镜
│   └── <name>.vpost
├── soundevents/                # 声音事件定义
│   └── soundevents_addon.vsndevts
├── sounds/                     # 音频源文件（mp3/wav 等）
└── scripts/
    └── vscripts/               # cs_script 源文件（.js）
```

使用约定：

- 资产配方文件（`.vmat` / `.vtex` / `.vmdl` / `.vpcf` / `.vpost` / `.vsndevts`）保存后由 Hammer 自动编译，无需手动运行编译器。
- kv3 文件头版本 GUID 从 addon 中同类型的现有文件复制，不要凭记忆手写。
- 编写任何新资产前，先在 addon 中找一个同类型的现有文件作为模板。
