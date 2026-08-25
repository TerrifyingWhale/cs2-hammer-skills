@echo off
setlocal enabledelayedexpansion

REM SessionStart hook for cs2-mapping-assistant plugin (Windows)
REM Usage: run-hook.cmd session-start

set "SCRIPT_DIR=%~dp0"
set "PLUGIN_ROOT=%SCRIPT_DIR%.."

if "%1"=="session-start" (
    REM Read the entry skill file content
    set "SKILL_FILE=%PLUGIN_ROOT%\skills\using-cs2-mapping\SKILL.md"

    if exist "!SKILL_FILE!" (
        echo {"additional_context": "你已加载 CS2 Hammer 地图创作套件。当用户提出 CS2 地图或资产任务时，请调用 cs2-mapping:using-cs2-mapping 技能确定流程。"}
    ) else (
        echo {"additional_context": "CS2 Hammer 地图创作套件已加载，但未找到入口技能文件。"}
    )
) else (
    echo {"error": "Unknown hook: %1"}
)

endlocal
