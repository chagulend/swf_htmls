#!/usr/bin/env python3


def generate_html():
    with open("template.html") as f:
        template = f.read()
    p = Path(".")
    swfs = list(p.glob("**/*.swf"))
    for swf in swfs:
        content = template.replace("template", swf.stem)
        html = swf.with_suffix(".html")
        with open(html, "w") as f:
            f.write(content)


def remove_old_html():
    p = Path(".")
    for html in p.glob("**/*.html"):
        html.unlink()

if __name__ == "__main__":
    remove_old_html()
    #generate_html()
