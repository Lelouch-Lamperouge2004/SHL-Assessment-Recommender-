# SHL Conversational Assessment Recommender

A conversational AI system that recommends SHL assessments using FastAPI, semantic retrieval, and Gemini LLM integration.

---

## Live Project Links

### Live API Base URL

https://shl-assessment-recommender-78e3.onrender.com

### Swagger API Documentation

https://shl-assessment-recommender-78e3.onrender.com/docs

### ReDoc API Documentation

https://shl-assessment-recommender-78e3.onrender.com/redoc

### Health Check

https://shl-assessment-recommender-78e3.onrender.com/health

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
- Pydantic
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Gemini 1.5 Flash
- Render
- GitHub

---

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | API status and useful links |
| `/health` | GET | Checks whether the API is running |
| `/docs` | GET | Swagger UI for testing API endpoints |
| `/redoc` | GET | Alternative API documentation |
| `/chat` | POST | Main conversational recommendation endpoint |

---

## GET /

Returns project status and useful API links.

Example response:

```json
{
  "project": "SHL Conversational Assessment Recommender",
  "status": "running",
  "message": "API is live. Visit /docs to test the endpoints.",
  "health": "/health",
  "docs": "/docs",
  "redoc": "/redoc",
  "chat_endpoint": "/chat"
}