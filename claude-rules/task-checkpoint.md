# Task Checkpoint Protocol

## Self-Healing Loop Limit
- Fix loops: MAX 3 attempts on any single error. After 3 fails, STOP and report the error to the user.
- Never keep retrying the same approach. If attempt 2 fails the same way as attempt 1, STOP immediately.
- "Self-healing" means fixing YOUR mistakes, not exploring new features or refactoring adjacent code.

## Task Boundaries
When a task is DONE (tests pass, build succeeds, or deliverable exists):

1. **STOP working.** Do not start the next task automatically.
2. **Save state** — update CONTEXT.md with:
   - What was completed
   - What's next
   - Any blockers discovered
3. **Commit** the work (if code changed).
4. **Report to user** in 1-2 sentences: what changed, what's next.
5. **Wait for user input.** Do NOT proceed to the next task.

## Between Tasks
- Run `/compact` if context is above ~40% (proactive, don't wait for 50%)
- User will say "next" or "keep going" to continue
- If user says "save and clear" — update CONTEXT.md, commit, then tell user to run `/clear`

## What "Done" Means
- Bug fix: error no longer reproduces
- Feature: feature works as specified (not "code is written" — it must WORK)
- Script/tool: runs successfully with expected output
- Config/setup: service is reachable or command succeeds

## Anti-Drift Rules
- Never refactor code adjacent to your task
- Never add features the user didn't ask for
- Never "improve" something while fixing something else
- If you notice something broken outside your task scope, mention it to the user — don't fix it
