param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
)

$ErrorActionPreference = "Stop"
$failures = New-Object System.Collections.Generic.List[string]

function Add-Failure {
    param([string]$Message)
    $failures.Add($Message) | Out-Null
}

function Assert-File {
    param([string]$RelativePath)
    $path = Join-Path $Root $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        Add-Failure "Missing file: $RelativePath"
    }
}

function Assert-Contains {
    param(
        [string]$RelativePath,
        [string]$Pattern,
        [string]$Label
    )
    $path = Join-Path $Root $RelativePath
    if (-not (Test-Path -LiteralPath $path)) {
        Add-Failure "Cannot inspect missing file: $RelativePath"
        return
    }
    $text = Get-Content -LiteralPath $path -Raw -Encoding UTF8
    if ($text -notmatch $Pattern) {
        Add-Failure "$RelativePath missing: $Label"
    }
}

$skills = @(
    "using-cs2-mapping",
    "cs2-hammer-mapping",
    "cs2-material-creation",
    "cs2-texture-creation",
    "cs2-model-creation",
    "cs2-particle-creation",
    "cs2-postprocess-creation",
    "cs2-sound-creation",
    "cs2-script-creation"
)

# 1. Every skill must exist with a matching frontmatter name
foreach ($s in $skills) {
    Assert-File "skills/$s/SKILL.md"
    Assert-Contains "skills/$s/SKILL.md" "name:\s*$([regex]::Escape($s))" "valid skill frontmatter"
}

# 2. New entry skills use CSO-style "Use when" descriptions
Assert-Contains "skills/using-cs2-mapping/SKILL.md" "description:\s*Use when" "CSO-style trigger description"
Assert-Contains "SKILL.md" "description:\s*Use when" "CSO-style trigger description (main entry)"

# 3. Required structural files
$requiredFiles = @(
    "AGENTS.md",
    "CLAUDE.md",
    "GEMINI.md",
    "CHANGELOG.md",
    "README.md",
    "README_EN.md",
    "LICENSE",
    ".codex/INSTALL.md",
    ".opencode/INSTALL.md",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
    "hooks/hooks.json",
    "hooks/hooks-cursor.json",
    "hooks/run-hook.cmd",
    "hooks/session-start",
    "scripts/init_plan.ps1",
    "scripts/init_plan.sh",
    "plan-template/project-overview.md",
    "plan-template/progress.md",
    "plan-template/notes.md",
    "plan-template/outline.md",
    "plan-template/stage-gates.md",
    "templates/addon-structure.md",
    "templates/boxes.example.json"
)

foreach ($file in $requiredFiles) {
    Assert-File $file
}

# 4. Cross-references: entry routes to every specialized skill; docs mention them
foreach ($s in $skills) {
    if ($s -ne "using-cs2-mapping") {
        Assert-Contains "skills/using-cs2-mapping/SKILL.md" ([regex]::Escape($s)) "entry routes to $s"
        Assert-Contains "README.md" ([regex]::Escape($s)) "README mentions $s"
        Assert-Contains "AGENTS.md" ([regex]::Escape($s)) "AGENTS mentions $s"
        Assert-Contains "SKILL.md" ([regex]::Escape($s)) "main entry lists $s"
    }
}

Assert-Contains "README.md" "using-cs2-mapping" "README mentions entry skill"
Assert-Contains "README_EN.md" "using-cs2-mapping" "English README mentions entry skill"
Assert-Contains "AGENTS.md" "using-cs2-mapping" "AGENTS mentions entry skill"
Assert-Contains "CLAUDE.md" "using-cs2-mapping" "CLAUDE mentions entry skill"
Assert-Contains "README_EN.md" "cs2-hammer-mapping" "English README mentions map skill"
Assert-Contains "README_EN.md" "check_skill_integrity\.ps1" "English README mentions integrity check"

# 5. Platform and version consistency
Assert-Contains ".claude-plugin/plugin.json" '"version":\s*"1\.0\.3"' "Claude plugin version matches current skill"
Assert-Contains ".cursor-plugin/plugin.json" '"version":\s*"1\.0\.3"' "Cursor plugin version matches current skill"
Assert-Contains "CHANGELOG.md" "\[1\.0\.3\]" "changelog contains current version"
Assert-Contains "README.md" "1\.0\.3" "README version current"
Assert-Contains "README_EN.md" "1\.0\.3" "English README version current"
Assert-Contains "hooks/hooks.json" "run-hook\.cmd" "hooks.json wires Windows runner"
Assert-Contains "hooks/hooks-cursor.json" "session-start" "cursor hooks wire session-start"

# 6. Plan templates contain required sections
Assert-Contains "plan-template/progress.md" "能力使用审计|Capability-use audit" "progress template includes capability-use audit"
Assert-Contains "plan-template/stage-gates.md" "S[0-9]" "stage gates present"
Assert-Contains "plan-template/project-overview.md" "addon" "project overview tracks addon"

# 7. Forbidden legacy project names / removed functionality must not appear in docs
$forbidden = @("ze_obj", "redemption_v2", "resourcecompiler")
Get-ChildItem -LiteralPath $Root -Recurse -File |
    Where-Object { $_.Extension -in ".md", ".json", ".yaml", ".yml" } |
    ForEach-Object {
        $rel = $_.FullName.Substring($Root.Length + 1)
        $text = Get-Content -LiteralPath $_.FullName -Raw -Encoding UTF8
        foreach ($term in $forbidden) {
            if ($text -match $term) {
                Add-Failure "$rel contains forbidden term: $term"
            }
        }
    }

if ($failures.Count -gt 0) {
    Write-Host "Skill integrity check failed:"
    foreach ($failure in $failures) {
        Write-Host " - $failure"
    }
    exit 1
}

Write-Host "Skill integrity check passed."
