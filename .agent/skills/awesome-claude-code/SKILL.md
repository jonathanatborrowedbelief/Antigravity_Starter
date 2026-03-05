---
name: awesome-claude-code
description: Curated directory of Claude Code resources — agent skills, slash-commands, CLAUDE.md files, hooks, tooling, orchestrators, and workflows. Use when the user asks about Claude Code extensions, wants to find a skill/plugin/tool, asks "is there a skill for X", wants to discover what's available in the Claude Code ecosystem, or wants to browse community resources.
---

# Awesome Claude Code

A curated community list of resources for extending and enhancing [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

**Repo:** [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)

---

## When to Use This Skill

- User asks "is there a skill/plugin/tool for X in Claude Code?"
- User wants to discover community resources for Claude Code
- User wants to find slash-commands, hooks, CLAUDE.md templates, or orchestrators
- User needs recommendations for extending Claude Code's capabilities

---

## Resource Categories

### 🤖 Agent Skills

Pre-built skill sets that extend Claude's capabilities. Notable picks:

| Skill | Best For |
|---|---|
| [AgentSys](https://github.com/avifenesh/agentsys) | Workflow automation, PR management, multi-agent code review |
| [cc-devops-skills](https://github.com/akin-ozer/cc-devops-skills) | IaC, cloud platform deployment, DevOps |
| [Claude Code Agents](https://github.com/undeadlist/claude-code-agents) | E2E dev workflow, parallel auditors, browser QA |
| [Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin) | Learning from mistakes, pragmatic SDLC agents |
| [Context Engineering Kit](https://github.com/NeoLabHQ/context-engineering-kit) | Advanced context patterns, minimal token use |
| [Everything Claude Code](https://github.com/affaan-m/everything-claude-code) | Broad coverage of core engineering domains |
| [Fullstack Dev Skills](https://github.com/jeffallan/claude-skills) | 65 skills across full-stack frameworks + Jira/Confluence |
| [Superpowers](https://github.com/obra/superpowers) | Planning, testing, debugging — SDLC best practices |
| [Trail of Bits Security Skills](https://github.com/trailofbits/skills) | Security auditing, CodeQL, Semgrep, vulnerability detection |
| [TÂCHES CC Resources](https://github.com/glittercowboy/taches-cc-resources) | Meta-skills, hook creation, adaptable workflow |
| [Web Assets Generator](https://github.com/alonw0/web-asset-generator) | Favicons, PWA icons, Open Graph images |
| [Book Factory](https://github.com/robertguss/claude-skills) | Nonfiction book creation pipeline |

---

### 🔪 Slash-Commands

Custom prompts that control Claude's behavior for specific tasks.

**Categories available:**

- **General** — Hook creation, Linux desktop operations
- **Version Control & Git** — Commit workflows, PR management
- **Code Analysis & Testing** — Static analysis, test generation
- **Context Loading & Priming** — Context engineering commands
- **Documentation & Changelogs** — Auto-doc generation
- **CI / Deployment** — Pipeline automation
- **Project & Task Management** — Sprint/task tracking
- **Miscellaneous** — Utility commands

Browse all: [Slash-Commands section](https://github.com/hesreallyhim/awesome-claude-code#slash-commands-)

---

### 📂 CLAUDE.md Files

Project-level instruction files that give Claude Code persistent context.

**Categories:**

- Language-specific (Python, Go, TypeScript, etc.)
- Domain-specific (web, data, mobile, etc.)
- Project scaffolding & MCP

> CLAUDE.md files = your project's standing instructions to Claude. The better the file, the better the output.

---

### 🪝 Hooks

Event-driven scripts that run before/after Claude Code actions (file edits, shell commands, etc.).

- [/create-hook](https://github.com/omril321/automated-notebooklm/blob/main/.claude/commands/create-hook.md) — Guided hook creation with smart project-aware suggestions

---

### 🧰 Tooling

Full applications built on top of Claude Code.

**Sub-categories:**

- **IDE Integrations** — Editor plugins and extensions
- **Usage Monitors** — Token/cost tracking
- **Orchestrators** — Multi-agent coordination systems
- **Config Managers** — Settings and profile management

---

### 📊 Status Lines

Terminal status bar integrations showing Claude Code state in real-time.

---

### 📱 Alternative Clients

Interfaces beyond the default Claude Code CLI.

---

## How to Use This Skill

When the user asks about capabilities or extensions, reference the relevant category above and link them directly to the resource. For discovery requests ("find a skill for X"), cross-reference the skill descriptions to recommend the best match.

---

## Resources

- **Main Repo:** [github.com/hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)
- **Official Claude Code Docs:** [docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)
- **Submit a resource:** [Issues → Recommend Resource](https://github.com/hesreallyhim/awesome-claude-code/issues/new?template=recommend-resource.yml)
