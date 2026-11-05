"""Build the single-file offline scoreboard.

Reads src/scoreboard.src.html, replaces every {{asset:filename}} token with a
base64 data URI of src/assets/filename, and writes scoreboard.html at the
project root. Run:  python tools/build.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src" / "scoreboard.src.html"
ASSETS = ROOT / "src" / "assets"
OUT = ROOT / "scoreboard.html"

MIME = {".png": "image/png", ".woff2": "font/woff2", ".ttf": "font/ttf", ".svg": "image/svg+xml", ".webp": "image/webp"}


def data_uri(name: str) -> str:
    path = ASSETS / name
    mime = MIME[path.suffix.lower()]
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def main() -> None:
    html = SRC.read_text(encoding="utf-8")
    html = re.sub(r"\{\{asset:([\w.-]+)\}\}", lambda m: data_uri(m.group(1)), html)
    OUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
