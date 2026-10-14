
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS

from chunking import chunk_transcript

load_dotenv()


class GeminiEmbeddings(Embeddings):
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is missing from .env"
            )

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-embedding-001"

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        vectors = []

        # Batch requests rather than sending one request per chunk
        batch_size = 50

        for start in range(0, len(texts), batch_size):
            batch = texts[start:start + batch_size]

            response = self.client.models.embed_content(
                model=self.model,
                contents=batch,
                config=types.EmbedContentConfig(
                    task_type="RETRIEVAL_DOCUMENT",
                    output_dimensionality=768,
                ),
            )

            vectors.extend(
                embedding.values
                for embedding in response.embeddings
            )

        return vectors

    def embed_query(self, text: str) -> list[float]:
        response = self.client.models.embed_content(
            model=self.model,
            contents=text,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=768,
            ),
        )

        return response.embeddings[0].values


def create_vectorstore(transcript: str):
    chunks = chunk_transcript(transcript)

    embeddings = GeminiEmbeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embeddings,
    )

    vectorstore.save_local("faiss_index")

    print("Gemini embeddings created successfully.")
    print(f"Indexed {len(chunks)} transcript chunks.")

    return vectorstore
