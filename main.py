from src.loader import load_all_pdfs
from src.chunking import split_docs
from src.embedding import EmbeddingManager
from src.vector_store import VectorStoreManager
from src.retriever import RAGRetriever
from src.generator import RAGGenerator
import os

documents = load_all_pdfs("data")

chunks = split_docs(documents)
print("DOCUMENTS:", len(documents))
print("CHUNKS:", len(chunks))

if not chunks:
    raise ValueError("No chunks created! PDF content is empty or split failed.")
texts = [doc.page_content for doc in chunks if doc.page_content and doc.page_content.strip()]

print("TEXTS:", len(texts))

if not texts:
    raise ValueError("Texts are empty after extracting page_content!")

embedding_manager = EmbeddingManager()

embeddings = embedding_manager.generate_embeddings(
    texts
)

vector_store = VectorStoreManager()

vector_store.add_documents(
    chunks,
    embeddings
)

rag_retriever = (
    RAGRetriever(
        embedding_manager,
        vector_store
    )
)
generator = (
    RAGGenerator(
        api_key=os.getenv(
            "GROQ_API_KEY"
        )
    )
)

answer = (
    generator.generate_output(
        "What is RAG?",
        rag_retriever
    )
)

print(answer)