import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os
import pickle
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain




def get_pdf_texts(pdf):
    texts = ''
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        texts += page.extract_text()
    return texts

def get_text_chunks(texts):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text=texts)
    return chunks

def get_vectorstore(chunks):
    embedding = OpenAIEmbeddings()
    
    vectorstore = FAISS.from_texts(chunks, embedding=embedding)

    return vectorstore

def get_response(vectorstore, user_question):
    docs = vectorstore.similarity_search(query=user_question,k=2)
    llm = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.5)
    
    chain = load_qa_chain(llm=llm, chain_type='stuff', verbose=True)
    response = chain.run(input_documents=docs, question=user_question)

    return response






def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with your PDF",
                       page_icon=":books:")
    
    st.header("Chat with your PDF :books:")

    uploaded_pdf = st.file_uploader('Upload your PDF file here :point_down:')
    

    if st.button('Process'):

        try:
            texts = get_pdf_texts(uploaded_pdf)

            chunks = get_text_chunks(texts)


            if "vectorstore" not in st.session_state:
                st.session_state.vectorstore = None
            pdf_name = uploaded_pdf.name[:-4]
            if os.path.exists(f"{pdf_name}.pkl"):
                with open(f"{pdf_name}.pkl", "rb") as f:
                    st.session_state.vectorstore = pickle.load(f)
            else:
                st.session_state.vectorstore = get_vectorstore(chunks)
                with open(f"{pdf_name}.pkl", "wb") as f:
                    pickle.dump(st.session_state.vectorstore, f)
            st.session_state.chat = 'enable'
        except:
            st.warning('Upload a PDF first :point_up_2:' )


    if "chat" not in st.session_state:
            st.session_state.chat = None


    if st.session_state.chat == 'enable':
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            response = get_response(st.session_state.vectorstore, user_question)
            st.write(response)


if __name__ == '__main__':
    main()