
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_transcript(transcript: str | None = None):
    if transcript is None:
        transcript = Path("transcript.txt").read_text(
            encoding="utf-8"
        )

    document = Document(
        page_content=transcript,
        metadata={"source": "youtube_transcript"},
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    chunks = splitter.split_documents([document])
    print(f"Created {len(chunks)} chunks.")

    return chunks
