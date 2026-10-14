
from indexing import fetch_transcript
from embedding import create_vectorstore
from generation import generate_answer


def main():
    video_id = input("Enter YouTube video ID: ").strip()

    try:
        print("\n[1/3] Fetching transcript...")
        transcript = fetch_transcript(video_id)

        if not transcript.strip():
            raise ValueError("The transcript is empty.")

        print("\n[2/3] Creating embeddings and FAISS index...")
        create_vectorstore(transcript)

        print("\n[3/3] Chatbot ready!")

        while True:
            question = input(
                "\nAsk a question (or type 'exit'): "
            ).strip()

            if question.lower() == "exit":
                break

            if not question:
                continue

            answer = generate_answer(question)
            print("\nAnswer:", answer)

    except Exception as e:
        print(f"\nPipeline failed: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
