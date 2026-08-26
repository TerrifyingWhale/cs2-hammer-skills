# CS2 Hammer Mapping Assistant (CS2 Mapping Assistant)

Turn Counter-Strike 2 map creation from a one-shot chat into a trackable, resumable, reusable engineering workflow.

This suite is built for map makers using Source 2 Hammer / CS2 Workshop Tools. Everything is organized as modular skills: addon structure, entities and lighting, plus materials, textures, models, particles, post-processing filters, sounds, and scripts.

## Positioning

This is not a prompt pack that only writes a few asset snippets — it is a complete CS2 map-creation collaboration system. Before starting, the agent checks the currently open addon, aligns goals and constraints, then routes the task to the appropriate skill module. Batch asset jobs use batch mode: common settings are asked only once.

## Core capabilities

- Map-level workflow: addon structure, entity setup, lighting, publishing, programmatic `.vmap` inspection, and bulk brush creation
- Materials & textures: `.vmat` / `.vtex` recipe generation (including common shaders such as csgo_complex)
- Models: `.vmdl` generation with direct path references and automatic same-name material lookup
- Particles, filters, sounds, scripts: `.vpcf` / `.vpost` / `.vsndevts` / `cs_script`
- Batch mode: ask common settings once, accept rule files or folder-wide defaults, generate everything in one pass
- Multi-platform: Claude Code / Cursor / Codex / OpenCode / Gemini CLI
- Quality gates: skill integrity script + verify in Hammer before delivery

> ⚠️ **Use with caution**: the programmatic `.vmap` editing features in `cs2-hammer-mapping` (`dmxconvert`, `add_box_brush.py`) are not yet stable. Back up your map files and verify in Hammer before relying on them.

## Supported platforms

| Platform | Config file |
|---|---|
| Claude Code | `.claude-plugin/plugin.json` |
| Cursor | `.cursor-plugin/plugin.json` |
| Codex | `.codex/INSTALL.md` |
| OpenCode | `.opencode/INSTALL.md` |
| Gemini CLI | `GEMINI.md` |
| Other | `AGENTS.md` |

## Skill map

| Scenario | Skill |
|---|---|
| Entry & routing | `skills/using-cs2-mapping/` |
| Map workflow / entities / lighting / publishing / programmatic .vmap | `skills/cs2-hammer-mapping/` |
| Materials (.vmat) | `skills/cs2-material-creation/` |
| Texture definitions (.vtex) | `skills/cs2-texture-creation/` |
| Models (.vmdl) | `skills/cs2-model-creation/` |
| Particle systems (.vpcf) | `skills/cs2-particle-creation/` |
| Post-processing filters (.vpost) | `skills/cs2-postprocess-creation/` |
| Custom sounds (.vsndevts) | `skills/cs2-sound-creation/` |
| Scripts (cs_script / .js) | `skills/cs2-script-creation/` |

## Recommended workflow

1. **Entry routing**: say "help me make a CS2 map/material/model…" and the suite calls `using-cs2-mapping` first to determine the flow
2. **Inspect the addon**: the agent already has the target addon folder open; check the existing file structure and templates first
3. **Ask and confirm**: specialized skills ask only the necessary questions (purpose, texture source, batch settings); batch jobs ask once
4. **Generate**: produce asset recipe files per the relevant skill; Hammer auto-compiles on save
5. **Verify**: run `scripts/check_skill_integrity.ps1` after editing skills; confirm maps in Hammer before delivery

> Note: the map skill (cs2-hammer-mapping) gives advice and steps by default and does not modify files until you explicitly ask it to. Programmatic .vmap editing requires a backup and verification in Hammer.

## Quality gate

Run the integrity check after modifying skills:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check_skill_integrity.ps1
```

## Installation

### Option 1: Git clone

```bash
git clone https://github.com/TerrifyingWhale/cs2-hammer-skills.git
cd cs2-hammer-skills
```

### Per-platform installation

- Codex: see `.codex/INSTALL.md`
- OpenCode: see `.opencode/INSTALL.md`
- Claude Code / Cursor: load as a plugin via `.claude-plugin/plugin.json` / `.cursor-plugin/plugin.json`
- Other: copy the skill folders under `skills/` into your platform's skills directory

## Repository structure

```text
cs2-hammer-skills/
├── SKILL.md                    # Main entry (legacy platforms)
├── AGENTS.md                   # Generic agent configuration
├── CLAUDE.md                   # Claude project notes
├── GEMINI.md                   # Gemini CLI configuration
├── CHANGELOG.md                # Version history
├── .codex/                     # Codex install guide
├── .opencode/                  # OpenCode install guide
├── .claude-plugin/             # Claude Code configuration
├── .cursor-plugin/             # Cursor configuration
├── hooks/                      # Session-start hooks
├── skills/                     # Skill modules (entry + 8 specialized)
├── templates/                  # Asset/structure templates
└── scripts/                    # Tooling scripts
```

## Version

- Version: 1.0.3
- Last updated: 2026-08-26
