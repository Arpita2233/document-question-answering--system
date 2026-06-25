
from sentence_transformers import SentenceTransformer

class EmbeddingManager:

    def __init__(
        self,
        model_name="all-MiniLM-L6-v2"
    ):

        self.model_name = model_name

        print(
            f"Loading embedding model: {self.model_name}"
        )

        self.model = SentenceTransformer(
            self.model_name
        )

        print(
            f"Embedding Dimension: {self.model.get_sentence_embedding_dimension()}"
        )

    def generate_embeddings(
        self,
        texts
    ):
        print("DEBUG - texts received:", len(texts))

        if not texts:
            raise ValueError("Empty texts received for embedding!")

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True
        )

        print(f"Embeddings Shape: {embeddings.shape}")

        return embeddings

            