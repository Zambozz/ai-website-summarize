# AI Website Summarizer

AI-powered website summarizer built with Python and Groq Compound.

The application accepts a website URL, visits the website using Groq's built-in tools, and generates a concise summary of its content.

## Features

- Website URL validation
- Automatic website browsing
- AI-powered summarization
- Web search integration
- Streaming responses

## Technologies

- Python 3.12
- Groq API
- Docker

## Requirements

- Docker
- A Groq API key

## Setup

Clone the repository:

```bash
git clone https://github.com/Zambozz/ai-website-summarize.git
cd ai-website-summarize
cp .env.example .env
GROQ_API_KEY=your_groq_api_key_here
docker build -t ai-website-summarize .
docker run -it --rm --env-file .env ai-website-summarize