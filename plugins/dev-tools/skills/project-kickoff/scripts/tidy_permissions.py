#!/usr/bin/env python3
"""Analyse and tidy a Claude Code settings.local.json permissions file.

Usage:
    python3 tidy_permissions.py <path>           # Report mode (default)
    python3 tidy_permissions.py <path> --fix     # Output cleaned JSON
    python3 tidy_permissions.py <path> --json    # Report as JSON
"""

import json
import re
import sys
from pathlib import Path


# Patterns that indicate leaked secrets
SECRET_PATTERNS = [
    r"sk-ant-api\d+-[A-Za-z0-9_-]{20,}",   # Anthropic API keys
    r"[A-Za-z0-9_-]{32,}",                   # Long tokens/keys (32+ chars)
    r"Bearer [A-Za-z0-9_-]{20,}",            # Bearer tokens
    r"ANTHROPIC_API_KEY='[^']+",              # Explicit key assignments
    r"CLOUDFLARE_API_TOKEN=\"[^\"]+",         # Cloudflare tokens
    r"Authorization: [A-Za-z]+ [A-Za-z0-9_-]{20,}",  # Auth headers with tokens
]

# Shell fragments that get accidentally approved
SHELL_FRAGMENTS = {
    "Bash(do)", "Bash(done)", "Bash(fi)", "Bash(then)", "Bash(else)",
    "Bash(break)", "Bash(if)", "Bash(for)", "Bash(while)",
}

# Deprecated MCP references
DEPRECATED_MCP = [
    "mcp__bitwarden__",
    "mcp__google-chat__",    # Old format (not claude_ai_ prefixed)
    "mcp__google-docs__",    # Old format
    "mcp__google-drive__",   # Old format
    "mcp__google-sheets__",  # Old format
    "mcp__gmail__",          # Old format (not gmail-jez or gmail-anthro)
]

# Patterns that can be consolidated into broader ones
CONSOLIDATION_MAP = {
    "Bash(git *)": [
        r"Bash\(git (add|commit|push|pull|fetch|checkout|branch|merge|stash|rm|reset|log|diff|status|remote|revert|mv|check-ignore|ls-tree|merge-tree)",
    ],
    "Bash(gh *)": [
        r"Bash\(gh (repo|issue|pr|api|search|run|release|label|workflow|gist|auth|project)",
    ],
    "Bash(pnpm *)": [
        r"Bash\(pnpm (install|add|remove|build|dev|test|deploy|list|ls|why|run|exec|update|audit|tsc|vitest|dlx|--filter)",
    ],
    "Bash(npm *)": [
        r"Bash\(npm (install|run|view|audit|init|info|ls)",
    ],
    "Bash(npx *)": [
        r"Bash\(npx (wrangler|vercel|tsc|tsx|prettier|vitest|shadcn|prisma|vite)",
    ],
}


def strip_json_comments(text: str) -> str:
    """Remove // comments from JSON (Claude Code JSON5-style)."""
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Keep lines that are comment-only strings in arrays (like "// --- Git ---")
        if stripped.startswith('"//'):
            cleaned.append(line)
        else:
            # Remove inline comments (not inside strings)
            cleaned.append(line)
    return "\n".join(cleaned)


def load_settings(path: Path) -> dict:
    """Load settings.local.json, handling // comments."""
    text = path.read_text()
    # Try parsing as-is first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Strip comments and retry
    cleaned = strip_json_comments(text)
    return json.loads(cleaned)


def check_secrets(entry: str) -> bool:
    """Check if a permission entry contains a suspected secret."""
    # MCP tool names and WebFetch/WebSearch/Skill entries aren't secrets
    if entry.startswith(("mcp__", "WebFetch", "WebSearch", "Skill")):
        return False
    # Only check Bash entries and other patterns
    for pattern in SECRET_PATTERNS:
        if re.search(pattern, entry):
            return True
    return False


def check_shell_fragment(entry: str) -> bool:
    """Check if an entry is a shell fragment."""
    return entry in SHELL_FRAGMENTS or entry.startswith("Bash(__NEW_LINE_")


def check_deprecated_mcp(entry: str) -> bool:
    """Check if an entry references a deprecated MCP server."""
    for prefix in DEPRECATED_MCP:
        if entry.startswith(prefix):
            return True
    return False


def check_one_time(entry: str) -> bool:
    """Check if an entry looks like a one-time command that won't match again."""
    # Entries with embedded commit messages
    if "EOF" in entry and "git commit" in entry:
        return True
    # Entries with hardcoded absolute paths to specific files
    if re.search(r"Bash\(git -C /[^\s]+", entry):
        return True
    # Entries with hardcoded for-loop values
    if entry.startswith("Bash(for ") and "in " in entry:
        return True
    # Entries with specific file copies
    if "cp " in entry and "/" in entry and entry.count("/") > 3:
        return True
    return False


def find_consolidations(entries: list[str]) -> dict[str, list[str]]:
    """Find entries that could be consolidated into broader patterns."""
    consolidations = {}
    for broad, patterns in CONSOLIDATION_MAP.items():
        # Skip if the broad pattern already exists
        if broad in entries:
            continue
        matches = []
        for entry in entries:
            for pattern in patterns:
                if re.match(pattern, entry):
                    matches.append(entry)
                    break
        if len(matches) >= 2:
            consolidations[broad] = matches
    return consolidations


def find_duplicates(entries: list[str]) -> list[str]:
    """Find duplicate entries."""
    seen = set()
    dupes = []
    for entry in entries:
        if entry in seen:
            dupes.append(entry)
        seen.add(entry)
    return dupes


def analyse(settings: dict) -> dict:
    """Analyse permissions and return a report."""
    entries = settings.get("permissions", {}).get("allow", [])

    # Filter out comment strings
    real_entries = [e for e in entries if not e.startswith("//")]
    comments = [e for e in entries if e.startswith("//")]

    report = {
        "total_entries": len(real_entries),
        "comment_lines": len(comments),
        "secrets": [e for e in real_entries if check_secrets(e)],
        "shell_fragments": [e for e in real_entries if check_shell_fragment(e)],
        "deprecated_mcp": [e for e in real_entries if check_deprecated_mcp(e)],
        "one_time": [e for e in real_entries if check_one_time(e)],
        "duplicates": find_duplicates(real_entries),
        "consolidations": find_consolidations(real_entries),
    }

    issues = (
        len(report["secrets"])
        + len(report["shell_fragments"])
        + len(report["deprecated_mcp"])
        + len(report["one_time"])
        + len(report["duplicates"])
    )
    report["total_issues"] = issues
    report["consolidation_count"] = sum(
        len(v) for v in report["consolidations"].values()
    )

    return report


def print_report(report: dict, path: str) -> None:
    """Print human-readable report."""
    print(f"\n=== Permission Tidy Report: {path} ===\n")
    print(f"Total entries: {report['total_entries']} ({report['comment_lines']} comment lines)")
    print(f"Issues found: {report['total_issues']}")
    print(f"Consolidation opportunities: {report['consolidation_count']} entries -> {len(report['consolidations'])} broad patterns")
    print()

    if report["secrets"]:
        print(f"LEAKED SECRETS ({len(report['secrets'])}):")
        for s in report["secrets"]:
            # Truncate to avoid printing full secrets
            display = s[:60] + "..." if len(s) > 60 else s
            print(f"  - {display}")
        print()

    if report["shell_fragments"]:
        print(f"Shell fragments ({len(report['shell_fragments'])}):")
        for s in report["shell_fragments"]:
            print(f"  - {s}")
        print()

    if report["deprecated_mcp"]:
        print(f"Deprecated MCP refs ({len(report['deprecated_mcp'])}):")
        for s in report["deprecated_mcp"]:
            print(f"  - {s}")
        print()

    if report["one_time"]:
        print(f"One-time entries ({len(report['one_time'])}):")
        for s in report["one_time"]:
            display = s[:80] + "..." if len(s) > 80 else s
            print(f"  - {display}")
        print()

    if report["duplicates"]:
        print(f"Duplicates ({len(report['duplicates'])}):")
        for s in report["duplicates"]:
            print(f"  - {s}")
        print()

    if report["consolidations"]:
        print("Consolidation opportunities:")
        for broad, specifics in report["consolidations"].items():
            print(f"  {broad} would replace {len(specifics)} entries:")
            for s in specifics[:5]:
                print(f"    - {s}")
            if len(specifics) > 5:
                print(f"    ... and {len(specifics) - 5} more")
        print()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"Error: {path} not found")
        sys.exit(1)

    mode = sys.argv[2] if len(sys.argv) > 2 else "--report"

    settings = load_settings(path)
    report = analyse(settings)

    if mode == "--json":
        # Don't include full secret values in JSON output
        safe_report = report.copy()
        safe_report["secrets"] = [s[:40] + "..." for s in report["secrets"]]
        print(json.dumps(safe_report, indent=2))
    elif mode == "--fix":
        # Output a cleaned version
        entries = settings.get("permissions", {}).get("allow", [])
        remove = set()
        remove.update(report["secrets"])
        remove.update(report["shell_fragments"])
        remove.update(report["deprecated_mcp"])
        remove.update(report["one_time"])
        remove.update(report["duplicates"])

        cleaned = [e for e in entries if e not in remove]
        settings["permissions"]["allow"] = cleaned
        print(json.dumps(settings, indent=2))
    else:
        print_report(report, str(path))


if __name__ == "__main__":
    main()
