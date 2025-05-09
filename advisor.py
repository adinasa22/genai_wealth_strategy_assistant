from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import Ollama
from langchain.chains import RetrievalQA
import tempfile
import os
from guardrails import is_safe_response

def load_documents(files):
    documents = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.read())
            loader = PyPDFLoader(tmp_file.name)
            documents.extend(loader.load())
            os.unlink(tmp_file.name)
    return documents

def get_portfolio_advice(age, goal, risk, files):
    documents = load_documents(files)
    embeddings = HuggingFaceEmbeddings()
    db_path = "./chroma_db"
    vectorstore = Chroma.from_documents(documents, embeddings, persist_directory=db_path)
    retriever = vectorstore.as_retriever()
    llm = Ollama(model="llama3")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    query = f"What’s the best portfolio strategy for a {age}-year-old investor saving for {goal} with {risk.lower()} risk appetite?"
    response = qa_chain.run(query)
    is_safe, issues = is_safe_response(response)
    if not is_safe:
        return f"⚠️ The response contained unsafe content: {issues}. Please review."
    return response