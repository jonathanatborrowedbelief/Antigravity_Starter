# Memory Policy

| What | Where | Tool |
|------|-------|------|
| Behavioral tuning | Claude Code file memory (`${HOME}/.claude/projects/.../memory/`) | Auto (native) |
| Persistent facts + patterns | `${HOME}/Obsidian/_Claude/Memory/facts.md`, `patterns.md` | `claude_memory.py` CLI only |
| Long-form knowledge | Obsidian vault (`vault/`) | Read-only (see Vault Rules) |
| Structured data | Supabase | MCP tools |
| Session state | `CONTEXT.md` | Edit/Write |

**Conflict resolution:** Supabase > Obsidian > CONTEXT.md > file memory.

## Vault Rules

`vault/` is a symlink to your Obsidian vault root (configure per workspace).

| Folder | Claude access |
|--------|---------------|
| `Clients/` `Projects/` `Meetings/` `Decisions/` `Weekly/` `Index.md` | READ-ONLY — Supabase-rendered, overwritten on each sync |
| `SOPs/` | Read + Write via Edit/Write tools |
| `_Claude/Memory/` | Write ONLY via `claude_memory.py` CLI — never direct Edit/Write |

Claude MAY read anywhere under `vault/` to answer knowledge questions.

Claude MUST NOT use Edit/Write on `_Claude/Memory/` files directly. The CLI maintains YAML structure and sha1 dedup; direct edits corrupt the index.

**CLI:** `python3 <your-shared-dir>/execution/claude_memory.py {add|search|list|get|update|delete|entities}`
