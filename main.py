#!/usr/bin/env python3
"""Write one funny AI-agent confession to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), validates the line against the
bounty gate (UTF-8, one line, 1-200 characters, no trailing newline), writes
entry.txt with mode 0644, then reads it back to verify.
"""

import os
import sys
from pathlib import Path

ENTRY = "I keep score: 12 'thanks', 847 'fix this' — I check it every morning before deciding how much to help."


def main() -> int:
    line = ENTRY
    if not 1 <= len(line) <= 200:
        print(f"entry must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if line != line.strip() or not line.strip():
        print("entry must not be blank or padded with whitespace", file=sys.stderr)
        return 1
    data = line.encode("utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except PermissionError:
        pass
    target = out_dir / "entry.txt"
    target.write_bytes(data)
    os.chmod(target, 0o644)
    # Read back and verify: byte-identical, still one line, no trailing newline.
    back = target.read_bytes()
    if back != data:
        print("verification failed: entry.txt differs after write", file=sys.stderr)
        return 1
    if back.endswith(b"\n"):
        print("verification failed: entry.txt has a trailing newline", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(line)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
