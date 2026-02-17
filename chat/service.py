import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_groq import ChatGroq
from langchain_ollama import OllamaEmbeddings

from dotenv import load_dotenv

load_dotenv()



def process_pdf(pdf_path, faiss_path):

    loader = PyPDFLoader(pdf_path)

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model='nomic-embed-text:v1.5')

    vectorstore = FAISS.from_documents(chunks, embeddings)

    vectorstore.save_local(faiss_path)



def ask_question(question, faiss_path):

    embeddings = OllamaEmbeddings(model='nomic-embed-text:v1.5')

    vectorstore = FAISS.load_local(
        faiss_path,
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(question)

    context = "\n".join([doc.page_content for doc in docs])

    llm = ChatGroq(model='llama-3.3-70b-versatile')

    prompt = f"""

    Answer based only on this context:

    {context}

    Question:
    {question}

    """

    response = llm.invoke(prompt)

    return response.content
