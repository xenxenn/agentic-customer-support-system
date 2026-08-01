# Agentic Customer Support System

An AI-powered customer support system developed for the PointStar Developer Intern Assessment.

This project implements an agentic AI customer support assistant that combines system design, website content processing, and an intelligent AI agent using LangGraph and Gemini API.

The project consists of three parts:

1. System Design
2. Technical Implementation
3. Agentic AI Application.

## Project Structure

### Part 1 – System Design

Designed an agentic customer support system to:

- Classify customer inquiries.
- Generate responses based on internal knowledge base.
- Detect critical issues and route them to human agents.
- Prevent hallucination by grounding responses using verified information.

Documentation is available in the `docs/` folder.

### Part 2 – Technical Implementation

Implemented a website scraping and summarization pipeline with:

- Improved HTML content extraction using BeautifulSoup.
- Removal of unnecessary page elements.
- Input length limitation.
- Gemini-powered summarization.
- Summary guardrail to keep output concise and factual

  Run:

```bash
python src/main.py
```

### Part 3 – Agentic AI

Built an AI customer support agent using LangGraph and Gemini API.

Features:

- LangGraph ReAct agent workflow.
- Conversation memory.
- Knowledge base retrieval from PointStar FAQ PDF.
- Calculator tool with agent-based tool selection.
- Context-aware responses.
- Grounded answers to reduce hallucination.

Run:

```bash
python src/app.py
```

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file based on `.env.example`and add your own API key:

```env
GEMINI_API_KEY=your_own_api_key_here
```

## Repository Structure

```
docs/
data/
src/
tests/
.env.example
README.md
requirements.txt
```

## Technologies

- Python
- LangGraph
- LangChain
- Google Gemini API
- BeautifulSoup
- PyPDF
