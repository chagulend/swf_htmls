#!/usr/bin/env python3
from pathlib import Path


def generate_flv():
    with open("template.html") as f:
        template = f.read()
    p = Path(".")
    swfs = list(p.glob("**/*.swf"))
    htmls = {}
    for swf in swfs:
        name = str(swf).rstrip(".swf")
        tmp = template.replace("template", name)
        htmls[name] = tmp
    for name, content in htmls.items():
        with open(name + ".html", "w") as f:
            f.write(content)


if __name__ == "__main__":
    generate_flv()
