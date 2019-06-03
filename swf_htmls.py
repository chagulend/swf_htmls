#!/usr/bin/env python3
from pathlib import Path
import click


@click.command()
@click.option("--path", default=".", type=click.Path(),
              help="Target directory")
@click.option("-c", "--clean", is_flag=True,
              help="Remove old html files")
@click.option("-r", "--recursive", is_flag=True, help="Recursive")
def generate_html(path, clean, recursive):
    p = Path(path)
    files = p.glob("*.swf")
    if clean:
        remove_old_html(path, recursive)
    if recursive:
        files = p.glob("**/*.swf")
    with open("template.html") as f:
        template = f.read()
    for swf in files:
        content = template.replace("template", swf.stem)
        html = swf.with_suffix(".html")
        html.write_text(content)


def remove_old_html(path, recursive):
    p = Path(path)
    files = p.glob("*.html")
    if recursive:
        files = p.glob("**/*.html")
    for html in files:
        if html.name == "template.html":
            continue
        html.unlink()


if __name__ == "__main__":
    generate_html()
