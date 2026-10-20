# /// script
# dependencies = ["htpy"]
# ///
import os
from pathlib import Path

from htpy import a as anchor
from htpy import body, h1, head, html, li, meta, ol, title

books_file = Path("books.txt")
index_file = Path("index.html")


def layout(content):
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
            content,
        ],
    ]


def main():
    books = books_file.read_text().strip().splitlines()

    doc = layout(ol[(li[anchor(href=book + ".pdf")[book]] for book in books)])
    with index_file.open("w", encoding="utf-8") as fp:
        fp.write(str(doc))


if __name__ == "__main__":
    main()
