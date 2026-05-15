# SHL Conversational Assessment Recommender

A conversational AI system that recommends SHL assessments using FastAPI, semantic retrieval, and Gemini LLM integration.

---

## Features

- Conversational SHL assessment recommendations
- Clarification handling for vague queries
- Recommendation refinement using conversation history
- Assessment comparison using catalog-grounded responses
- Off-topic refusal handling
- Stateless API design
- FastAPI backend with structured JSON responses
- Semantic retrieval using TF-IDF and cosine similarity
- Gemini 1.5 Flash integration for conversational replies

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Gemini 1.5 Flash
- Render
- GitHub

---

## API Endpoints

### GET /health

Returns API readiness status.

Example response:

```json
{
  "status": "ok"
}
```

### POST /chat

Accepts stateless conversation history and returns SHL assessment recommendations.

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Hiring a backend developer with Java and SQL skills"
    }
  ]
}
```

Example response:

```json
{
  "reply": "These assessments are suitable for evaluating backend programming and analytical skills.",
  "recommendations": [
    {
      "name": "Java 8",
      "url": "https://www.shl.com/...",
      "test_type": "K"
    }
  ],
  "end_of_conversation": true
}
```

---

## Project Structure

```text
app.py
recommender.py
vector_store.py
llm.py
catalog.json
requirements.txt
README.md
```

---

## Local Setup

Clone repository:

```bash
git clone https://github.com/Lelouch-Lamperouge2004/SHL-Assessment-Recommender-.git
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn app:app --reload
```

---

## Deployment

Deployed on Render.

Base URL:

```text
https://shl-assessment-recommender-78e3.onrender.com
```

---

## Notes

- Recommendations are restricted to SHL catalog entries only.
- Conversation history is handled statelessly.
- Responses are schema-validated using Pydantic.
- Hallucinated URLs and external recommendations are prevented through catalog grounding.