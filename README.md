# YouTube RAG Chatbot

An AI-powered chatbot that enables users to ask questions about YouTube videos and receive context-aware answers generated from video transcripts. It combines Retrieval-Augmented Generation (RAG), Gemini embeddings, FAISS vector search, and Groq-hosted language models.

## Overview

Understanding long YouTube videos can be time-consuming. This project simplifies the process by allowing users to interact with a video's transcript through natural language questions.

The application retrieves the transcript, divides it into smaller text chunks, converts the chunks into vector embeddings, and stores them in a FAISS index. When a user asks a question, the system retrieves relevant chunks and passes them to a language model to generate a contextual answer.

## Key Features

- **YouTube Transcript Retrieval:** Fetches available transcripts using the YouTube Transcript API.
- **Text Chunking:** Splits transcripts into smaller, manageable chunks with configurable overlap.
- **Semantic Embeddings:** Uses Google's Gemini embedding model to represent text as vectors.
- **Vector Search:** Uses FAISS to retrieve relevant transcript chunks.
- **Context-Aware Responses:** Uses a Groq-hosted language model to generate answers based on retrieved context.
- **Modular Architecture:** Separates transcript indexing, chunking, embedding, retrieval, and generation into independent Python modules.
- **Interactive Question Answering:** Allows users to ask questions through a command-line interface.

## Architecture

```text
YouTube Video URL
       |
       v
Transcript Retrieval
       |
       v
Text Chunking
       |
       v
Gemini Embeddings
       |
       v
FAISS Vector Index
       |
       v
User Question
       |
       v
Query Embedding
       |
       v
Similarity Search
       |
       v
Relevant Transcript Chunks
       |
       v
Groq Language Model
       |
       v
Context-Aware Answer
```

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Transcript Retrieval | youtube-transcript-api |
| Text Splitting | LangChain Text Splitters |
| Embedding Model | Google Gemini |
| Vector Search | FAISS |
| Language Model Inference | Groq API |
| Environment Configuration | python-dotenv |
| Version Control | Git and GitHub |

## Project Structure

```text
YTChatBot/
├── indexing.py       # Retrieves YouTube transcripts
├── chunking.py       # Splits transcripts into chunks
├── embedding.py      # Generates embeddings and builds the index
├── retriever.py      # Retrieves relevant transcript chunks
├── generation.py     # Generates answers using the LLM
├── main.py           # Runs the complete workflow
├── requirements.txt  # Project dependencies
├── .gitignore        # Excludes secrets and generated files
└── README.md         # Project documentation
```

## Prerequisites

Before running the project, ensure you have:

- Python installed with a version compatible with the project dependencies.
- A Google Gemini API key for embedding generation.
- A Groq API key for language model inference.
- Git installed to clone the repository.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/SumanthG-1312/YouTubeChatBot.git
cd YouTubeChatBot
```

### 2. Create a Virtual Environment

For Windows PowerShell:

```powershell
python -m venv ytvenv
.\ytvenv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory.

```env
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

Replace the placeholders with your actual API keys.

Get your API keys from:

- Google AI Studio: https://aistudio.google.com/apikey
- Groq Console: https://console.groq.com/keys

**Security:** Never upload your `.env` file or expose API keys in your source code. Ensure that `.env` is listed in `.gitignore`.

### 5. Run the Application

```bash
python main.py
```

Follow the terminal prompts to provide a YouTube video URL and ask questions about its content, according to the input flow implemented in `main.py`.

## How It Works

1. **Transcript Extraction:** Retrieves the available transcript for the selected YouTube video.
2. **Text Chunking:** Divides the transcript into smaller, overlapping text segments.
3. **Embedding Generation:** Converts each chunk into a numerical vector using Gemini.
4. **Vector Indexing:** Stores the vectors in FAISS for efficient similarity search.
5. **Question Processing:** Converts the user's question into a vector using the same embedding model.
6. **Context Retrieval:** Searches FAISS for transcript chunks relevant to the question.
7. **Answer Generation:** Passes the retrieved context to a Groq-hosted language model to generate a response.

## Limitations

- Transcript retrieval depends on captions being available and accessible.
- Videos without accessible transcripts may not be supported.
- Answer quality depends on transcript accuracy, retrieval relevance, and language model performance.
- Gemini and Groq API usage is subject to their respective quotas, rate limits, and pricing.
- The application answers questions using transcript text rather than directly analyzing video visuals.

## Future Improvements

- Develop a web interface using Streamlit or Next.js.
- Add persistent vector storage to avoid regenerating embeddings for previously processed videos.
- Implement conversational memory for follow-up questions.
- Improve retrieval using metadata filtering and reranking.
- Include source references or timestamps in generated answers.
- Support multiple videos and document collections.
- Add comprehensive error handling, logging, and automated tests.

## Learning Outcomes

This project demonstrates practical implementation of:

- Retrieval-Augmented Generation
- Text preprocessing and chunking
- Embedding-based semantic search
- FAISS vector indexing and retrieval
- Language model integration through APIs
- Modular Python application design
- Environment variable management
- Git-based version control

## Author

**Sumanth Gajjela**

GitHub: https://github.com/SumanthG-1312

---

*Built to explore practical applications of Retrieval-Augmented Generation and context-aware question answering.*
