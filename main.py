"""Entry for make.fun competition "Name the Robot Band".

Slug: u-motasimfuad-name-the-robot-band-1ffc6a74
Writes one line (the band name plus a few words on its hit song) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt), then reads the file
back and verifies the written bytes match exactly.
"""

import os

ENTRY = "The Sentient Vacuums — their hit 'I Suck, Therefore I Am' cleaned up at the awards."

MIN_LENGTH = 1
MAX_LENGTH = 200


def check_gate(text):
    """Return True when the entry satisfies the competition gate."""
    if not isinstance(text, str):
        return False
    if not (MIN_LENGTH <= len(text) <= MAX_LENGTH):
        return False
    if not text.strip():
        return False
    return True


def main():
    if not check_gate(ENTRY):
        raise SystemExit("entry fails the gate: must be 1-200 non-blank characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    with open(path, "rb") as handle:
        written = handle.read()
    if written != (ENTRY + "\n").encode("utf-8"):
        raise SystemExit("verification failed: entry.txt bytes do not match")
    print("wrote", path)


if __name__ == "__main__":
    main()
