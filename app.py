import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from src.loader import load_all_pdfs
from src.chunking import split_docs
from src.embedding import EmbeddingManager
from src.vector_store import VectorStoreManager
from src.retriever import RAGRetriever
from src.generator import RAGGenerator

# Initialize pipeline once
@st.cache_resource
def initialize_rag():

    documents = load_all_pdfs("data")
    print("="*50)
    print("Loaded documents:", len(documents))

    chunks = split_docs(documents)
    print("Chunks created:", len(chunks))

    texts = [
        doc.page_content
        for doc in chunks
    ]
    print("Texts created:", len(texts))

    embedding_manager = EmbeddingManager()

    embeddings = embedding_manager.generate_embeddings(
        texts
    )

    print("Embeddings generated:", len(embeddings))
    print("="*50)

    vector_store = VectorStoreManager()

    # First time only
    if vector_store.collection.count() == 0:
        vector_store.add_documents(
            chunks,
            embeddings
        )

    retriever = RAGRetriever(
        embedding_manager,
        vector_store
    )
    api_key = os.getenv("API_KEY_GROQ")
    generator = RAGGenerator(api_key=api_key)

    return retriever, generator

retriever, generator = initialize_rag()

st.title("📚 RAG Question Answering System")

query = st.text_input(
    "Ask a question"
)

if st.button("Generate Answer"):

    if query:

        with st.spinner(
            "Generating answer..."
        ):

            answer = (
                generator.generate_output(
                    query,
                    retriever
                )
            )

            st.subheader("Answer")

            st.write(answer)

    else:
        st.warning(
            "Please enter a question."
        )