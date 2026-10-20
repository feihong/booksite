index:
    uv run --env-file .env create_index.py

publish: index
    uv run --env-file .env publish.py
