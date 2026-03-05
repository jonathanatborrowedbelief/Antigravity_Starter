Pull latest state from git and load project context for this session.

Steps:
1. Pull latest and display state:
   `python3 tools/state_manager/execution/sync_state.py --pull`

2. Read the state summary carefully. It shows:
   - Which project was active and its pipeline progress
   - What decisions were made in previous sessions
   - What blockers exist
   - What the NEXT ACTION should be

3. If STATE.json doesn't exist, this is a fresh start:
   - Run `python3 tools/state_manager/execution/save_state.py` to initialize
   - Ask the user which project to work on

4. Continue from where the previous session left off by following the NEXT ACTION.

5. If the user asks to work on a different project than what's shown as active, update it:
   `python3 tools/state_manager/execution/save_state.py --active clients/{client}/{project}`
