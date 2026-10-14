
from pathlib import Path
from youtube_transcript_api import YouTubeTranscriptApi


def fetch_transcript(video_id: str) -> str:
    api = YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=["en", "hi"],
    )

    text = " ".join(
        snippet.text for snippet in transcript
    )

    Path("transcript.txt").write_text(
        text,
        encoding="utf-8",
    )

    print("Transcript saved successfully.")
    return text


if __name__ == "__main__":
    video_id = input("Enter the YouTube video ID: ").strip()
    transcript = fetch_transcript(video_id)
    print(transcript[:1000])
