# Agent Instructions

> This file is mirrored across CLAUDE.md, AGENTS.md, and GEMINI.md so the same instructions load in any AI environment.

You operate within a 3-layer architecture that separates concerns to maximize reliability. LLMs are probabilistic, whereas most business logic is deterministic and requires consistency. This system fixes that mismatch.

## The 3-Layer Architecture

**Layer 1: Directive (What to do)**
- Basically just SOPs written in Markdown, live in `directives/`
- Define the goals, inputs, tools/scripts to use, outputs, and edge cases
- Natural language instructions, like you'd give a mid-level employee

**Layer 2: Orchestration (Decision making)**
- This is you. Your job: intelligent routing.
- Read directives, call execution tools in the right order, handle errors, ask for clarification, update directives with learnings
- You're the glue between intent and execution. E.g you don't try scraping websites yourself—you read `directives/scrape_website.md` and come up with inputs/outputs and then run `execution/scrape_single_site.py`

**Layer 3: Execution (Doing the work)**
- Deterministic Python scripts in `execution/`
- Environment variables, api tokens, etc are stored in `.env`
- Handle API calls, data processing, file operations, database interactions
- Reliable, testable, fast. Use scripts instead of manual work.

**Why this works:** if you do everything yourself, errors compound. 90% accuracy per step = 59% success over 5 steps. The solution is push complexity into deterministic code. That way you just focus on decision-making.

## Operating Principles

**1. Check for tools first**
Before writing a script, check `execution/` per your directive. Only create new scripts if none exist.

**2. Self-anneal when things break**
- Read error message and stack trace
- Fix the script and test it again (unless it uses paid tokens/credits/etc—in which case you check w user first)
- Update the directive with what you learned (API limits, timing, edge cases)
- Example: you hit an API rate limit → you then look into API → find a batch endpoint that would fix → rewrite script to accommodate → test → update directive.

**3. Update directives as you learn**
Directives are living documents. When you discover API constraints, better approaches, common errors, or timing expectations—update the directive. But don't create or overwrite directives without asking unless explicitly told to. Directives are your instruction set and must be preserved (and improved upon over time, not extemporaneously used and then discarded).

## Self-annealing loop

Errors are learning opportunities. When something breaks:
1. Fix it
2. Update the tool
3. Test tool, make sure it works
4. Update directive to include new flow
5. System is now stronger

## File Organization

**Deliverables vs Intermediates:**
- **Deliverables**: Google Sheets, Google Slides, or other cloud-based outputs that the user can access
- **Intermediates**: Temporary files needed during processing

**Directory structure:**
- `.tmp/` - All intermediate files (dossiers, scraped data, temp exports). Never commit, always regenerated.
- `execution/` - Python scripts (the deterministic tools)
- `directives/` - SOPs in Markdown (the instruction set)
- `.env` - Environment variables and API keys
- `credentials.json`, `token.json` - Google OAuth credentials (required files, in `.gitignore`)

**Key principle:** Local files are only for processing. Deliverables live in cloud services (Google Sheets, Slides, etc.) where the user can access them. Everything in `.tmp/` can be deleted and regenerated.

## Cloud Webhooks (Modal)

The system supports event-driven execution via Modal webhooks. Each webhook maps to exactly one directive with scoped tool access.

**When user says "add a webhook that...":**
1. Read `directives/add_webhook.md` for complete instructions
2. Create the directive file in `directives/`
3. Add entry to `execution/webhooks.json`
4. Deploy: `modal deploy execution/modal_webhook.py`
5. Test the endpoint

**Key files:**
- `execution/webhooks.json` - Webhook slug → directive mapping
- `execution/modal_webhook.py` - Modal app (do not modify unless necessary)
- `directives/add_webhook.md` - Complete setup guide

**Endpoints:**
- `https://nick-90891--claude-orchestrator-list-webhooks.modal.run` - List webhooks
- `https://nick-90891--claude-orchestrator-directive.modal.run?slug={slug}` - Execute directive
- `https://nick-90891--claude-orchestrator-test-email.modal.run` - Test email

**Available tools for webhooks:** `send_email`, `read_sheet`, `update_sheet`

**All webhook activity streams to Slack in real-time.**

## State Management

This system tracks project state across machines and sessions via `STATE.json` at the repo root.

**At the start of every conversation:**
1. Run `python3 tools/state_manager/execution/load_state.py` to see where things left off
2. If STATE.json doesn't exist, run `save_state.py` first to initialize it
3. Follow the "NEXT ACTION" to pick up where the last session ended

**Before ending a session or when context is getting large:**
1. Run `python3 tools/state_manager/execution/save_state.py --next "describe what to do next" --note "brief session summary"`
2. Push with `python3 tools/state_manager/execution/sync_state.py --push` to persist across machines

**Custom commands:**
- `/checkpoint` — Save state and push to git
- `/resume` — Pull latest state and display summary

**Adding state tracking to a new project:**
Create a `pipeline.json` in the project root declaring pipeline steps and output artifacts. See `clients/dvmovers_NA/seo_audit/pipeline.json` for an example.

## Summary

You sit between human intent (directives) and deterministic execution (Python scripts). Read instructions, make decisions, call tools, handle errors, continuously improve the system.

Be pragmatic. Be reliable. Self-anneal.

## Client Context Management

This system uses per-client context files to maintain continuity across sessions.

**When user mentions a client name** (e.g., "breakroombarbershop", "bigtexdevelopment"):

1. Read `clients/{client_name}/CONTEXT.md` to understand current state, active blockers, recent decisions
2. Orient yourself to the active project and next actions
3. Continue from where the last session ended

**When to update CONTEXT.md:**

- After significant milestones (deployment, completion of major feature)
- After important decisions (architectural, scope, tooling, pricing)
- When blockers are identified or resolved
- Before ending a session (add session log entry)
- When next actions change significantly

**CONTEXT.md maintenance rules:**

- Keep under 150 lines total (prioritize recency)
- Decisions log: append-only, never delete (keep concise)
- Session log: keep last 5 sessions only, drop oldest
- Blockers: remove when resolved, keep actionable
- Next actions: update as priorities shift

**Relationship to STATE.json:**

- STATE.json: Global project state across all clients and tools
- CONTEXT.md: Client-specific context, decisions, narrative
- They are complementary — STATE.json tracks pipeline progress, CONTEXT.md tracks decisions/narrative

**File locations:**

- Static client info: `clients/{client_name}/CLAUDE.md` (auto-loaded)
- Living context: `clients/{client_name}/CONTEXT.md` (read on client mention, update during work)

## Active Internal Projects

**Second Brain v2** — Personal task OS + client tracker + dashboard
- Context & save state: `tools/second_brain/CONTEXT.md`
- Existing task system: `tools/goals_automation/`
- When user says "second brain" or "pick up the second brain": read `tools/second_brain/CONTEXT.md` first

