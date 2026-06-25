
from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_docs(
    documents,
    chunk_size=500,
    chunk_overlap=50
):
    print("Docs received for splitting:", len(documents))
    """
    Split documents into smaller chunks for embedding.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunked_docs = text_splitter.split_documents(
        documents
    )
    print("Chunks created:", len(chunked_docs))

    print(f"Total Chunks Created: {len(chunked_docs)}")

    return chunked_docs