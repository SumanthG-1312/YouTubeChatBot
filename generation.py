
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from retriever import retrieve

load_dotenv()


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)


prompt = ChatPromptTemplate.from_template("""
You are a helpful YouTube video assistant.

Answer the user's question using the transcript context provided below.

Instructions:
1. Understand what the user is asking.
2. Use the most relevant information from the context.
3. Explain the answer clearly and naturally.
4. You may combine information from multiple retrieved chunks.
5. Do not invent facts or claim the video says something
   that is not supported by the context.
6. If the context is insufficient, clearly say that the
   transcript does not provide enough information.
7. If useful, explain concepts with examples.
8. Keep the answer focused on the question.

Transcript context:
{context}

User question:
{question}

Answer:
""")

chain = prompt | llm


def generate_answer(question: str) -> str:
    docs = retrieve(question)

    if not docs:
        return "I couldn't find relevant information in this video's transcript."

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    if not context.strip():
        return "The retrieved transcript context is empty."

    response = chain.invoke({
        "context": context,
        "question": question,
    })

    return response.content


if __name__ == "__main__":
    while True:
        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() == "exit":
            break

        if question:
            try:
                print("\nAnswer:", generate_answer(question))
            except Exception as e:
                print(f"Error: {type(e).__name__}: {e}")
