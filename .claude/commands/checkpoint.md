Save current project state and push to git for cross-machine persistence.

Steps:
1. Run: `python3 tools/state_manager/execution/save_state.py`
   - This scans the filesystem, git status, and pipeline.json manifests
   - Writes STATE.json at the repo root

2. Review the output to confirm the active project and pipeline status look correct

3. If the active project is wrong, re-run with:
   `python3 tools/state_manager/execution/save_state.py --active clients/{client}/{project}`

4. Add context about the session before pushing:
   `python3 tools/state_manager/execution/save_state.py --next "describe what to do next" --note "brief session summary"`

5. You can also log a key decision:
   `python3 tools/state_manager/execution/save_state.py --decision "describe the decision"`

6. Push to git:
   `python3 tools/state_manager/execution/sync_state.py --push --message "describe checkpoint"`

7. Confirm the push succeeded. If push fails, try pulling first:
   `python3 tools/state_manager/execution/sync_state.py --pull`
   Then retry the push.
