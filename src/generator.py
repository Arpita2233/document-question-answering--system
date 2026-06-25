import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq

class RAGGenerator:

    def __init__(
        self,
        api_key,
        model="qwen/qwen3-32b"
    ):

        self.llm = ChatGroq(
            groq_api_key=api_key,
            model=model,
            temperature=0.2,
            max_tokens=1024
        )

    def generate_output(
        self,
        query,
        retriever,
        top_k=3
    ):

        results = retriever.retrieve(
            query,
            top_k
        )

        context = "\n".join(
            [
                doc["document"]
                for doc in results
            ]
        )

        if not context:
            return (
                "No relevant context found."
            )

        prompt = f"""
Use the provided context to answer the question.

Context:
{context}

Question:
{query}

Answer:
"""

        response = (
            self.llm.invoke(prompt)
        )

        return response.content