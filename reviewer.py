#!/usr/bin/env python3
"""
Code Reviewer - Main Entry Point

Analyzes Python source files for bugs, style issues, and best practices.
"""

import argparse
import sys
from pathlib import Path

from rules.style_rules import StyleChecker
from rules.bug_rules import BugChecker
from rules.complexity import ComplexityAnalyzer


def parse_args():
      parser = argparse.ArgumentParser(
                description="AI-powered Python code reviewer"
      )
      parser.add_argument(
          "--file", "-f",
          required=True,
          help="Path to the Python file to review"
      )
      parser.add_argument(
          "--mode",
          choices=["quick", "detailed", "strict"],
          default="detailed",
          help="Review mode (default: detailed)"
      )
      parser.add_argument(
          "--output", "-o",
          help="Output file for the review report (optional)"
      )
      return parser.parse_args()


def review_file(filepath: str, mode: str) -> dict:
      """Run all checkers on the given file and return results."""
      path = Path(filepath)
      if not path.exists():
                print(f"Error: File '{filepath}' not found.", file=sys.stderr)
                sys.exit(1)
            if path.suffix != ".py":
                      print(f"Warning: '{filepath}' does not appear to be a Python file.")

    source = path.read_text(encoding="utf-8")

    results = {
              "file": filepath,
              "mode": mode,
                                "style": StyleChecker(source).check(),
              "bugs": BugChecker(source).check(),
              "complexity": ComplexityAnalyzer(source).analyze(),
    }
    return results


def print_report(results: dict):
      """Print the review report to stdout."""
    print(f"\n{'='*60}")
    print(f"Code Review Report: {results['file']}")
    print(f"Mode: {results['mode']}")
    print(f"{'='*60}\n")

    sections = [
              ("Style Issues", results["style"]),
              ("Bug Warnings", results["bugs"]),
              ("Complexity", results["complexity"]),
    ]

    total_issues = 0
    for section_name, issues in sections:
              print(f"--- {section_name} ---")
              if not issues:
                            print("  No issues found.")
else:
            for issue in issues:
                              print(f"  Line {issue.get('line', '?')}: {issue['message']}")
                              total_issues += 1
                      print()

    print(f"Total issues found: {total_issues}")
    print(f"{'='*60}\n")


def main():
      args = parse_args()
    results = review_file(args.file, args.mode)
    print_report(results)

    if args.output:
              Path(args.output).write_text(str(results), encoding="utf-8")
              print(f"Report saved to '{args.output}'")


if __name__ == "__main__":
      main()
