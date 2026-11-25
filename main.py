"""Entry for make.fun bounty "The Most Boring Object, Reviewed in One Line".

Entry text (130 characters, limit: at most 200 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = 'The beige wall socket: two stars. It has one job, does it silently, and still manages to be the most judgmental thing in the room.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
