# /// script
# dependencies = ["htpy"]
# ///
from pathlib import Path

from htpy import a as anchor
from htpy import (
    body,
    br,
    button,
    code,
    div,
    h1,
    head,
    html,
    li,
    meta,
    ol,
    script,
    title,
)
from markupsafe import Markup

books_file = Path("books.txt")
index_file = Path("index.html")

js_script = Markup("""
const command = `wget --recursive --depth=1 --no-directories --accept=pdf --no-clobber --directory-prefix=$HOME/books ${location.href}`

document.querySelector('code').textContent = command

document.querySelector('button').addEventListener('click', () => navigator.clipboard.writeText(command))
""")

def layout(*contents):
    title_text = "Books"

    return html[
        head[
            meta(charset="utf-8"),
            meta(
                name="viewport",
                content="width=device-width, initial-scale=1.0, viewport-fit=cover",
            ),
            title[title_text],
        ],
        body[
            h1[title_text],
            *contents,
        ],
    ]


def main():
    books = books_file.read_text().strip().splitlines()

    doc = layout(
        ol[(li[anchor(href=book + ".pdf")[book]] for book in books)],
        div["Download command:", br(), code(), br(), button["Copy"]],
        script[js_script]
    )
    with index_file.open("w", encoding="utf-8") as fp:
        fp.write(str(doc))


if __name__ == "__main__":
    main()
