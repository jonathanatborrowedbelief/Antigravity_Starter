---
name: get-shit-done
description: Spec-driven development system using the GSD (Get Shit Done) framework with Claude Code. Use when the user wants to initialize a new project, plan and execute phases, manage milestones, resume work sessions, or run ad-hoc tasks with GSD's structured approach. Triggers on phrases like "start a new project", "plan this feature", "execute phase", "map my codebase", "gsd", "get shit done", or any reference to GSD commands like /gsd:new-project, /gsd:plan-phase, /gsd:execute-phase, /gsd:quick, etc.
---

# Get Shit Done (GSD)

A lightweight, spec-driven development system that solves **context rot** — the quality degradation as Claude fills its context window. GSD uses context engineering, XML prompt formatting, and multi-agent orchestration so Claude always builds what you actually want.

**Install:** `npx get-shit-done-cc@latest`

---

## When to Use This Skill

- User wants to start a new project with structured planning
- User has an existing codebase and wants to add features systematically
- User needs to run a quick bug fix or small task with GSD guarantees
- User references commands like `/gsd:*` or mentions "get shit done"
- User wants to resume a previous GSD work session

---

## Core Workflow (Full Project Lifecycle)

```
# 1. (Existing codebase only) Analyze what exists
/gsd:map-codebase

# 2. Initialize — questions, research, requirements, roadmap
/gsd:new-project
/clear

# 3. Per-phase loop (repeat for each phase N)
/gsd:discuss-phase N     # Lock in implementation preferences
/gsd:plan-phase N        # Research + create atomic plans + verify
/gsd:execute-phase N     # Parallel wave execution
/gsd:verify-work N       # Manual UAT + auto-diagnosis of failures
/clear

# 4. Complete milestone
/gsd:audit-milestone     # Verify all requirements shipped
/gsd:complete-milestone  # Archive, git tag, done

# 5. Next milestone
/gsd:new-milestone [name]
```

---

## Command Reference

### Core Workflow

| Command | Purpose | When |
|---|---|---|
| `/gsd:new-project` | Full init: questions → research → requirements → roadmap | New project |
| `/gsd:new-project --auto @idea.md` | Auto-init from existing doc (PRD, spec) | Have a doc ready |
| `/gsd:discuss-phase [N]` | Capture implementation decisions before planning | Before plan-phase |
| `/gsd:plan-phase [N]` | Research + create plans + verify them | Before execute-phase |
| `/gsd:execute-phase <N>` | Parallel wave execution across all plans | After planning |
| `/gsd:verify-work [N]` | UAT walkthrough + auto-diagnose failures | After execution |
| `/gsd:audit-milestone` | Check milestone met definition of done | Before completing |
| `/gsd:complete-milestone` | Archive milestone, tag release | All phases verified |
| `/gsd:new-milestone [name]` | Start next version cycle | After completing |

### Navigation & Session

| Command | Purpose |
|---|---|
| `/gsd:progress` | Show current status and next steps |
| `/gsd:resume-work` | Restore full context from last session |
| `/gsd:pause-work` | Save context handoff before stopping |
| `/gsd:help` | Show all commands |
| `/gsd:update` | Update GSD (with changelog preview) |

### Phase Management

| Command | Purpose |
|---|---|
| `/gsd:add-phase` | Append new phase (scope grew) |
| `/gsd:insert-phase [N]` | Insert urgent work between phases |
| `/gsd:remove-phase [N]` | Descope a phase and renumber |
| `/gsd:list-phase-assumptions [N]` | Preview Claude's intended approach before planning |
| `/gsd:plan-milestone-gaps` | Create phases for gaps found in audit |

### Utilities

| Command | Purpose |
|---|---|
| `/gsd:quick` | Ad-hoc task (bug fix, small feature) with GSD guarantees |
| `/gsd:debug [desc]` | Systematic debug with persistent state |
| `/gsd:add-todo [desc]` | Capture idea for later |
| `/gsd:check-todos` | Review captured todos |
| `/gsd:settings` | Configure workflow toggles and model profile |
| `/gsd:set-profile <profile>` | Quick switch: `budget` / `balanced` / `quality` |
| `/gsd:map-codebase` | Analyze existing codebase (spawns parallel agents) |

---

## Quick Mode (No Full Planning Needed)

For bug fixes, small features, config changes:

```
/gsd:quick
> "Fix the login button not responding on mobile Safari"
```

Skips: research, plan checker, verifier.
Keeps: atomic commits, state tracking, planner + executor agents.

---

## Speed vs Quality Presets

| Scenario | Mode | Profile | Research | Plan Check |
|---|---|---|---|---|
| Prototyping | `yolo` | `budget` | off | off |
| Normal dev | `interactive` | `balanced` | on | on |
| Production | `interactive` | `quality` | on | on |

Set via: `/gsd:settings` or `/gsd:set-profile <profile>`

---

## Key Files GSD Creates

| File | Purpose |
|---|---|
| `PROJECT.md` | Project goals, constraints, tech stack |
| `REQUIREMENTS.md` | v1 / v2 / out-of-scope scoping |
| `ROADMAP.md` | Phase breakdown mapped to requirements |
| `STATE.md` | Current progress state |
| `.planning/config.json` | Settings (models, toggles, git branching) |
| `{N}-CONTEXT.md` | Implementation decisions from discuss-phase |
| `{N}-RESEARCH.md` | Domain research for the phase |
| `{N}-{N}-PLAN.md` | Atomic XML-structured task plans |
| `{N}-{N}-SUMMARY.md` | Post-execution summaries |
| `{N}-UAT.md` | Verification results + fix plans |

---

## Project Structure Output

```
.planning/
  config.json
  research/
  quick/
    001-task-name/
      PLAN.md
      SUMMARY.md
PROJECT.md
REQUIREMENTS.md
ROADMAP.md
STATE.md
```

---

## Common Scenarios

**Starting fresh:**

```bash
npx get-shit-done-cc@latest   # install
claude --dangerously-skip-permissions
/gsd:new-project
```

**Existing codebase:**

```bash
/gsd:map-codebase    # analyze first
/gsd:new-project     # questions focus on what you're ADDING
```

**Resuming after a break:**

```bash
/gsd:progress        # see where you left off
# or
/gsd:resume-work     # full context restoration
```

**Mid-milestone scope change:**

```bash
/gsd:add-phase           # append new phase
/gsd:insert-phase 3      # urgent work between phases 3 and 4
/gsd:remove-phase 7      # descope phase 7
```

---

## Resources

- [GitHub Repo](https://github.com/gsd-build/get-shit-done)
- [Full User Guide](https://github.com/gsd-build/get-shit-done/blob/main/docs/USER-GUIDE.md)
