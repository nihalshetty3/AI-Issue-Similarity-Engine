import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()


def load_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db


def create_agent():

    llm = ChatOllama(
        model="mistral",
        temperature=0.3
    )

    db = load_vector_db()

    retriever = db.as_retriever(search_kwargs={"k": 3})

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    web_search = TavilySearchResults(k=3)

    return qa_chain, web_search , llm