#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? entry: writes one number to /output/entry.txt."""

# Honest count for this agent session: no live browser runs here and the
# VM's Chromium profile holds no open-tab session, so zero tabs are open.
LINE = "0"

# The gate: /output/entry.txt must hold one number in digits and nothing
# else (the brief asks for a single short text: one number in digits).
assert LINE.isdigit(), "line must be digits only"
assert str(int(LINE)) == LINE, "line must have no leading zeros"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
