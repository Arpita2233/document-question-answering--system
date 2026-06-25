import os
import uuid
import chromadb
import numpy as np
from langchain_core import documents

class VectorStoreManager:

    def __init__(
        self,
        persist_directory="data/vector_store",
        collection_name="pdf_documents"
    ):

        self.collection_name = collection_name
        self.persist_directory = persist_directory

        self.client = None
        self.collection = None

        self._initialize_store()

    def _initialize_store(self):

        os.makedirs(
            self.persist_directory,
            exist_ok=True
        )

        self.client = chromadb.PersistentClient(
            path=self.persist_directory
        )

        self.collection = (
            self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={
                    "description":
                    "vector store collection for pdf embeddings in RAG"
                }
            )
        )

        print(
            f"Initialized collection: {self.collection_name}"
        )

        print(
            f"Documents in collection: {self.collection.count()}"
        )

    def add_documents(self, documents, embeddings):

        if len(documents) != len(embeddings):
            raise ValueError("Mismatch between documents and embeddings")

        ids = []
        metadatas = []
        doc_contents = []
        embedding_list = []

        for doc, embedding in zip(documents, embeddings):

            doc_contents.append(doc.page_content)
            metadatas.append(doc.metadata if hasattr(doc, "metadata") else {})
            ids.append(str(uuid.uuid4()))

            # 🔥 IMPORTANT FIX (THIS WAS MISSING)
            embedding_list.append([float(x) for x in embedding])

        # optional safety check
        if not embedding_list:
            raise ValueError("Embedding list is empty!")

        self.collection.add(
            ids=ids,
            metadatas=metadatas,
            documents=doc_contents,
            embeddings=embedding_list
        )

        print(f"Collection size: {self.collection.count()}")