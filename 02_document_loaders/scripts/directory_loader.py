from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'

loader = DirectoryLoader(
    path=str(DATA_DIR / 'books'),
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)
