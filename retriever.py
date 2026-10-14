
from functools import lru_cache

from langchain_community.vectorstores import FAISS
from embedding import GeminiEmbeddings


@lru_cache(maxsize=1)
def get_retriever():
    embeddings = GeminiEmbeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True,
    )

    return vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )


def retrieve(query: str):
    return get_retriever().invoke(query)
