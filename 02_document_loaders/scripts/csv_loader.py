from pathlib import Path

from langchain_community.document_loaders import CSVLoader

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'

loader = CSVLoader(file_path=str(DATA_DIR / 'Social_Network_Ads.csv'))

docs = loader.load()

print(len(docs))
print(docs[1])
