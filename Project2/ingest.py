import os 
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader, TextLoader , WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS


load_dotenv()

def load_documents():
    docs=[]
    
    pdf1= PyPDFLoader("documents/ai-intro.pdf")
    docs.extend(pdf1.load())
    
    pdf2 = PyPDFLoader("documents/machine_learning.pdf")
    docs.extend(pdf2.load())
    
    txt = TextLoader("documents/policy.txt" , encoding="latin-1")
    docs.extend(txt.load())
    
    web = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
    docs.extend(web.load())
    
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 100
    ) 
    
    return splitter.split_documents(docs)

def create_vector_store():
    
    documents = load_documents()
    
    embeddings = HuggingFaceEmbeddings(
        model_name= "sentence-transformers/all-MiniLM-L6-V2"
    )
    
    db = FAISS.from_documents(documents, embeddings)
    db.save_local("vector_db")
    
    return db