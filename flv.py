#!/usr/bin/env python3
from pathlib import Path
import click


@click.command()
@click.argument("--option")
def generate_html():
    with open("template.html") as f:
        template = f.read()
    p = Path(".")
    for swf in p.glob("**/*.swf"):
        content = template.replace("template", swf.stem)
        html = swf.with_suffix(".html")
        html.write_text(content)


@click.option("-c", "--clean", is_flag=True)
def remove_old_html(clean):
    p = Path(".")
    for html in p.glob("**/*.html"):
        if html.name == "template.html":
            continue
        html.unlink()


if __name__ == "__main__":
    remove_old_html()
    generate_html()
