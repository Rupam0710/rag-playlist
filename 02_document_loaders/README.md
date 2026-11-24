# 02 · Document Loaders

**Video:** _add link from the playlist_

**Source code & data:** [campusx-official/langchain-document-loaders](https://github.com/campusx-official/langchain-document-loaders/)

## What this module covers

Loading data from different sources into LangChain `Document` objects.

## Key concepts

- `Document` = `page_content` + `metadata`
- File loaders (text, PDF, CSV), web loaders, directory loaders
- Lazy loading

## Loaders covered

| Loader | Script | Input | What you get | Needs |
|--------|--------|-------|--------------|-------|
| `TextLoader` | [`text_loader.py`](scripts/text_loader.py) | [`data/cricket.txt`](data/cricket.txt) — a poem | One `Document`; then summarised by an LLM chain | `OPENAI_API_KEY` |
| `PyPDFLoader` | [`pdf_loader.py`](scripts/pdf_loader.py) | [`data/dl-curriculum.pdf`](data/dl-curriculum.pdf) | One `Document` per page (23) | — |
| `CSVLoader` | [`csv_loader.py`](scripts/csv_loader.py) | [`data/Social_Network_Ads.csv`](data/Social_Network_Ads.csv) | One `Document` per row (400) | — |
| `DirectoryLoader` | [`directory_loader.py`](scripts/directory_loader.py) | every `*.pdf` in [`data/books/`](data/books), via `PyPDFLoader` | Pages streamed with `lazy_load()` | — |
| `WebBaseLoader` | [`webbase_loader.py`](scripts/webbase_loader.py) | A Flipkart product page URL | Page text; then queried by an LLM chain | `OPENAI_API_KEY` + internet |

## Folder layout

```text
02_document_loaders/
├── README.md
├── notebooks/                      # Follow-along notebooks (none yet)
├── scripts/                        # One runnable script per loader
│   ├── text_loader.py
│   ├── pdf_loader.py
│   ├── csv_loader.py
│   ├── directory_loader.py
│   └── webbase_loader.py
└── data/                           # Sample inputs used by the scripts
    ├── cricket.txt
    ├── dl-curriculum.pdf
    ├── Social_Network_Ads.csv
    └── books/
        ├── Building Machine Learning Systems with Python - Second Edition.pdf
        └── readme.md
```

## Running the scripts

From the repo root. The scripts find `data/` relative to their own file, so the working directory doesn't matter.

```bash
uv run python 02_document_loaders/scripts/csv_loader.py
uv run python 02_document_loaders/scripts/pdf_loader.py
uv run python 02_document_loaders/scripts/directory_loader.py

# These two call OpenAI — set OPENAI_API_KEY in .env first
uv run python 02_document_loaders/scripts/text_loader.py
uv run python 02_document_loaders/scripts/webbase_loader.py
```

## Notes

- The scripts are copied from the CampusX repo linked above. The only change is that file paths are resolved from the script's location (`DATA_DIR`) rather than the current working directory, so they run from this folder layout.
- `csv_loader`, `pdf_loader` and `directory_loader` have been run and work. `text_loader` and `webbase_loader` have **not** been run, since they need an OpenAI key (and internet for the web page).
- `data/books/` holds a ~6.8 MB PDF. `data/books/readme.md` is a placeholder from the original repo and is skipped by `glob='*.pdf'`.
- `directory_loader` prints a `fontTools is required to fully parse the encoding…` warning for this book. It's harmless; `uv add fonttools` silences it.

_Add your own notes here._

## Checklist

- [ ] Watch the video
- [ ] Follow along in `notebooks/`
- [ ] Clean up a runnable version in `scripts/`
- [ ] Move reusable code into `src/rag_playlist/`
