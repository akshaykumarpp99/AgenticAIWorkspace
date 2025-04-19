import streamlit as st
from utils.pdf_utils import extract_text_from_pdf
from utils.image_utils import extract_text_from_image
from langgraph_rag import generate_answer
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="RAG Agent")
st.title("LangChain RAG Agent")

uploaded_files = st.file_uploader("Upload PDFs or Images", type=["pdf", "png", "jpg","jpeg"], accept_multiple_files=True)
query = st.text_input("Ask a question abou the uploaded files")

if st.button("Get Answer") and uploaded_files and query:
    with st.spinner("Processing..."):
        extracted_texts = []
        for file in uploaded_files:
            if file.name.endswith(".pdf"):
                extracted_texts.append(extract_text_from_pdf(file))
            else:
                extracted_texts.append(extract_text_from_image(file))
        combined_text = "/n".join(extracted_texts)
        answer = generate_answer(query, combined_text)
        st.success("Done!")
        st.markdown(f"### Answer:\n{answer}")