import datetime
import os
import subprocess
from pathlib import Path


TEMPLATE = """
---
date: "{date}"
category: today-i-learned
author: {author}
comments: true
---

# {heading}

{body}
"""


def new_til(short_title: str):
    author = "René" if os.environ.get("USER", "") == "rene" else "Felix"
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    blog_dir = Path(__file__).resolve().absolute().parent
    new_file = blog_dir / year / f"{month}-{short_title}.md"
    content = f"""
---
date: "{date}"
category: today-i-learned
tags:
author: {author}
---

# {short_title}

"""

    new_file.write_text(content)
    print(f"Created new TIL file at {new_file}")
    open_in_editor = (
        input("Do you want to open the file in your editor? [Y/n] ").strip() or "y"
    )
    if open_in_editor.lower() == "y":
        subprocess.run(["xdg-open", new_file])
    subprocess.run(["git", "add", new_file])
    print("Don't forget to commit the new file!")


def main():
    import typer

    typer.run(new_til)
