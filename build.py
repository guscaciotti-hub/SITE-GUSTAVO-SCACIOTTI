#!/usr/bin/env python3
"""Gera index.html self-contained a partir de src/index.html.

Toda referência "../assets/..." vira data URI (base64), então o index.html
final é um arquivo único, sem dependências locais. Uso: python3 build.py
"""
import base64
import mimetypes
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
SRC = ROOT / "src" / "index.html"
OUT = ROOT / "index.html"

mimetypes.add_type("image/webp", ".webp")
cache = {}


def inline(match):
    rel = match.group(1)
    if rel not in cache:
        path = ROOT / rel
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        cache[rel] = f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"
    return cache[rel]


html = SRC.read_text(encoding="utf-8")
html = re.sub(r"\.\./(assets/[^\"')\s]+)", inline, html)
OUT.write_text(html, encoding="utf-8")
print(f"{OUT.name}: {OUT.stat().st_size / 1024:.0f} KB, {len(cache)} imagens embutidas")
