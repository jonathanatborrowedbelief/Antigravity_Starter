# AntiGravity_Starter

A project workspace template for client work, agent automation, and tool building. Designed to pair with [claude-config-starter](https://github.com/jonathanatborrowedbelief/claude-config-starter) for the Claude Code config side.

## Quick start

```bash
gh repo clone jonathanatborrowedbelief/Antigravity_Starter MyWorkspace
cd MyWorkspace
# Edit top-level CLAUDE.md — replace {{PROJECT_NAME}}
# Open in Claude Code
```

## Layout

- `clients/` — per-client workspaces (copy `.template/` to start a new one)
- `tools/` — reusable services (copy `.template/` to start a new one)
- `claude-rules/` — shared SOPs that apply across all clients/tools
- `.claude/commands/` — project-level slash commands (`/context`, `/checkpoint`)
- `CLAUDE.md` — top-level instructions Claude reads on session start
- `CONTEXT.md` — living state of this workspace

## Pattern: Directive → Orchestration → Execution

Each layer has a clear role. Directives (CLAUDE.md, CONTEXT.md) tell Claude what's true. Orchestration (subagents, slash commands) coordinates work. Execution (tools/) does the heavy lifting.

## License

MIT
