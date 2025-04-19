
from utils.vector_store import create_vector_store
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI


def generate_answer(query, extracted_text):
    vectorstore = create_vector_store([extracted_text])
    retriever = vectorstore.as_retiever(search_kwarge={"k":3})
    
    qa_chain = RetrievalQA.from_chain_type(
        llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
        retriever = retriever,
        return_source_documents=True    
    )
    return qa_chain.run(query)