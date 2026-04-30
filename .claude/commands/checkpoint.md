Task checkpoint — remind yourself of the protocol and prompt to update state before moving on.

Protocol (from claude-rules/task-checkpoint.md):
- Max 3 fix attempts per error → STOP and report
- After each task: update CONTEXT.md → commit → report → wait for user
- Never auto-proceed to the next task

Steps:
1. Read `CONTEXT.md` — confirm it reflects what just completed.
2. If it's stale, update it now:
   - What was completed
   - What's next
   - Any blockers discovered
3. Commit if code changed.
4. Report to user in 1-2 sentences: what changed, what's next.
5. STOP. Wait for user to say "next" or "keep going".
