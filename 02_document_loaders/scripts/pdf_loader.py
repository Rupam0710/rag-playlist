from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'

loader = PyPDFLoader(str(DATA_DIR / 'dl-curriculum.pdf'))

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)
