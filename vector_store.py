from langchain_community.vectorstores import FAISS
from text_splitter import texts
from nvidia_embeddings import nvidia_embeddings

# Create vector store
vectorstore = FAISS.from_documents(documents=texts, embedding=nvidia_embeddings)
