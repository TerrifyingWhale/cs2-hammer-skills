# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project purpose

This repository is a **multi-platform skill/plugin** for Counter-Strike 2 (Source 2 Hammer / CS2 Workshop Tools) map creation (not a conventional app/service). It provides a routed skill system for map workflow, materials, textures, models, particles, post-processing filters, sounds, and cs_script.

The main execution model is:
1. Entry/routing via `skills/using-cs2-mapping/SKILL.md`
2. Map-level workflow via `skills/cs2-hammer-mapping/SKILL.md`
3. Asset creation via one of the specialized skills (material, texture, model, particle, postprocess, sound, script)
4. Integrity verification via `scripts/check_skill_integrity.ps1`

## Key architecture (big picture)

- `skills/` — Primary modular skill system (authoritative behavior).
  - `using-cs2-mapping/` is the workflow router and rule gate.
  - `cs2-hammer-mapping/` handles map workflow, entities, lighting, publishing, and programmatic .vmap editing.
  - `cs2-material-creation/`, `cs2-texture-creation/`, `cs2-model-creation/`, `cs2-particle-creation/`, `cs2-postprocess-creation/`, `cs2-sound-creation/`, `cs2-script-creation/` handle single asset types.
- `hooks/` — Session-start injection for platforms (especially Claude/Cursor), including loading entry skill context.
- `.claude-plugin/plugin.json`, `.cursor-plugin/plugin.json` — Plugin metadata + hook wiring per platform.
- `plan-template/` — Canonical template files copied into user project `plan/`.
- `scripts/` — Operational tooling:
  - `check_skill_integrity.ps1`: validates skill structure, frontmatter, cross-references, and version consistency
  - `init_plan.ps1` / `init_plan.sh`: bootstrap `plan/` from `plan-template/`
- `templates/` — Asset/structure templates for map projects.

## Workflow invariants to preserve

- Do not bypass the entry router for map/asset tasks.
- Do not fabricate asset formats or entity properties; copy kv3 headers from existing addon files.
- Do not run manual compilation; Hammer auto-compiles on open/save.
- Keep `plan/` as persistent project memory (`project-overview.md`, `progress.md`, `notes.md`, `outline.md`, `stage-gates.md`).
- Ask once for common settings in batch asset tasks.
- Preserve compatibility across platform entry points (`SKILL.md`, `AGENTS.md`, `GEMINI.md`, plugin manifests, hooks).

## Common commands

> Run from repository root.

### Skill integrity check

```powershell
powershell -ExecutionPolicy Bypass -File scripts/check_skill_integrity.ps1
```

### Plan bootstrap

```powershell
powershell -ExecutionPolicy Bypass -File scripts/init_plan.ps1
```

```bash
bash scripts/init_plan.sh
```

## Important references

- `README.md` — user-facing positioning, workflow, skill map, and platform support.
- `SKILL.md` — legacy/main entry for compatible runtimes.
- `AGENTS.md` and `GEMINI.md` — platform-specific skill-loading entry points.
