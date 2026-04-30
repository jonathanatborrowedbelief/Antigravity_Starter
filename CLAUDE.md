# {{PROJECT_NAME}}

> Clone this template to start a new client/project workspace using the
> Directive → Orchestration → Execution pattern.

## Session Start

1. Read `CONTEXT.md` — current state, blockers, what's in flight
2. Read the relevant `clients/{name}/CONTEXT.md` before any client-specific work
3. After meaningful changes: update both CONTEXT.md files

## Architecture (3-layer)

**Directive → Orchestration → Execution**

- `clients/` — Per-client workspaces. Each has its own `CLAUDE.md` (static) + `CONTEXT.md` (living state)
- `tools/` — Reusable services (MCPs, scrapers, generators, etc.)
- `claude-rules/` — Shared SOPs (task-checkpoint protocol, memory policy, etc.)

## Per-Client Structure

Each client directory has:
- `CLAUDE.md` — static info (stack, credentials location, DNS, etc.)
- `CONTEXT.md` — living state (current sprint, blockers, recent changes)

Read the client's `CONTEXT.md` before any work on that client.

## Task Checkpoint Protocol

See `claude-rules/task-checkpoint.md` for the full SOP. Key rules:
- Max 3 fix attempts per error → STOP and report
- After each task: update CONTEXT.md → commit → report → wait for user
- Never auto-proceed to next task

## Memory

See `claude-rules/memory-policy.md` for the cross-platform memory policy
(file memory vs Obsidian vs Supabase vs CONTEXT.md).
