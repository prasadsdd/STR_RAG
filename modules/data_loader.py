import tempfile
from langchain.document_loaders import PyPDFLoader

def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents


