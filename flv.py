#!/usr/bin/env python3
from pathlib import Path


def generate_html():
    with open("template.html") as f:
        template = f.read()
    p = Path(".")
    for swf in p.glob("**/*.swf"):
        content = template.replace("template", swf.stem)
        html = swf.with_suffix(".html")
        html.write_text(content)


def remove_old_html():
    p = Path(".")
    for html in p.glob("**/*.html"):
        if html.name == "template.html":
            continue
        html.unlink()


if __name__ == "__main__":
    remove_old_html()
    generate_html()
