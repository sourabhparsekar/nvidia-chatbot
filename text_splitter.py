from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from data_ingestor import data

# Create a list of Document objects
documents = [Document(page_content=text) for text in data]

# Text splitting configuration
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# Split the documents
texts = text_splitter.split_documents(documents)
