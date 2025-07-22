from langchain.document_loaders import PyPDFLoader

def load_workout_pdf(file_path: str):
    loader = PyPDFLoader(file_path)
    return loader.load()
