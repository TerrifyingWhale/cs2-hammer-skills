# 在 Codex 中安装 CS2 Hammer 地图创作套件

通过 Codex 原生技能发现机制启用本套件。只需要克隆仓库并把 `skills/` 下的技能接入 `~/.codex/skills/`。

## 前置要求

- Git
- Codex（CLI 或桌面应用）

## 安装步骤

1. **克隆仓库：**

   ```bash
   git clone https://github.com/TerrifyingWhale/cs2-hammer-skills.git ~/.codex/cs2-hammer-skills
   ```

2. **把 `skills/` 下的技能复制（或链接）到 Codex skills 目录：**

   Windows（PowerShell，为每个技能创建目录联接）：

   ```powershell
   $repo = "$env:USERPROFILE\.codex\cs2-hammer-skills\skills"
   $target = "$env:USERPROFILE\.codex\skills"
   New-Item -ItemType Directory -Force -Path $target | Out-Null
   Get-ChildItem -LiteralPath $repo -Directory | ForEach-Object {
       $link = Join-Path $target $_.Name
       if (-not (Test-Path -LiteralPath $link)) {
           cmd /c mklink /J "`"$link`"" "`"$($_.FullName)`""
       }
   }
   ```

   macOS / Linux：

   ```bash
   mkdir -p ~/.codex/skills
   for d in ~/.codex/cs2-hammer-skills/skills/*/; do
     ln -s "$d" ~/.codex/skills/
   done
   ```

3. **重启 Codex**（退出并重新启动）以发现技能。

## 验证安装

列出已发现的技能，应能看到 `using-cs2-mapping` 与 8 个 `cs2-*` 专项技能。

## 更新

```bash
cd ~/.codex/cs2-hammer-skills && git pull
```

技能通过链接即时更新。

## 卸载

删除 `~/.codex/skills/` 下对应的技能链接/目录即可；可选：删除克隆的仓库 `~/.codex/cs2-hammer-skills`。

## 使用

安装后在对话中提到 CS2 地图或资产任务即可触发技能：

- "帮我检查这个 .vmap 有多少个 trigger_teleport"
- "把这张 PNG 转成材质"
- "为这个模型生成 vmdl"
- "做一批烟雾粒子"

技能会自动路由到对应专项流程。
