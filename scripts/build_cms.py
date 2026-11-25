#!/usr/bin/env python3
"""Convert editable Markdown pages into Shiroa-compatible Typst fragments.

Run before `shiroa build`. Does not modify content or original templates.
"""
from pathlib import Path
import subprocess
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "pages"
OUT = ROOT / "generated"

PAGES = [
    'intro',
    'news',
    'research',
    'projects',
    'projects/solar-pp',
    'projects/xenonnt-calibration',
    'projects/discrete-diffusion',
    'projects/potts-phase-transitions',
    'projects/airy-wkb',
    'about',
    'notes/xenonnt',
    'notes/qft',
    'notes/statphys',
]


def main():
    exe = shutil.which("pandoc")
    if not exe:
        sys.exit("ERROR: pandoc is required. On Ubuntu/WSL: sudo apt-get install -y pandoc")
    for page in PAGES:
        src = CONTENT / f"{page}.md"
        dst = OUT / f"{page}.typ"
        if not src.is_file():
            sys.exit(f"ERROR: content file not found: {src}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        cmd = [exe, "--from=markdown+tex_math_dollars+raw_tex", "--to=typst", "--wrap=none", "--output", str(dst), str(src)]
        print(f"Converting {src.relative_to(ROOT)} -> {dst.relative_to(ROOT)}", flush=True)
        subprocess.run(cmd, cwd=ROOT, check=True)
        if not dst.is_file():
            sys.exit(f"ERROR: Pandoc did not create {dst}")
    print("CMS content conversion succeeded.")


if __name__ == "__main__":
    main()
