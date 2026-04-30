#!/usr/bin/env python3
"""
{{TOOL_NAME}} — CLI entry point.
Replace this docstring with a one-line description.
"""

import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="{{TOOL_NAME}} — replace with your tool description",
    )
    parser.add_argument(
        "command",
        nargs="?",
        help="Command to run (e.g. run, check, export)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would happen without doing it",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.dry_run:
        print("[dry-run] No changes will be made.")

    if not args.command:
        print("No command given. Run with --help for usage.")
        sys.exit(1)

    # TODO: dispatch to your logic here
    print(f"Running command: {args.command}")


if __name__ == "__main__":
    main()
