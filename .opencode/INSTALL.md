# 在 OpenCode 中安装 CS2 Hammer 地图创作套件

## 前置要求

- [OpenCode.ai](https://opencode.ai) 已安装

## 安装步骤

在你的 `opencode.json`（全局或项目级别）的 `plugin` 数组中添加：

```json
{
  "plugin": ["cs2-mapping-assistant@git+https://github.com/TerrifyingWhale/cs2-hammer-skills.git"]
}
```

重启 OpenCode。插件会自动安装并注册所有技能。

验证安装：询问 "列出你的 CS2 地图创作技能"

## 使用

使用 OpenCode 原生 `skill` 工具：

```
use skill tool to list skills
use skill tool to load cs2-mapping/using-cs2-mapping
```

## 更新

重启 OpenCode 时自动更新。

锁定特定版本：

```json
{
  "plugin": ["cs2-mapping-assistant@git+https://github.com/TerrifyingWhale/cs2-hammer-skills.git#v1.0.0"]
}
```

## 故障排除

### 插件未加载

1. 检查日志：`opencode run --print-logs "hello" 2>&1 | grep -i cs2`
2. 验证 `opencode.json` 中的插件配置
3. 确保运行的是最新版本的 OpenCode

### 技能未找到

1. 使用 `skill` 工具列出已发现的技能
2. 检查插件是否正常加载（见上文）

## 获取帮助

- 报告问题：https://github.com/TerrifyingWhale/cs2-hammer-skills/issues
- 完整文档：https://github.com/TerrifyingWhale/cs2-hammer-skills
