import json
from llm import generate_llm_reply
from vector_store import semantic_search

def load_catalog():
    with open("catalog.json", "r", encoding="utf-8") as file:
        return json.load(file)

def get_last_user_message(messages):
    for message in reversed(messages):
        if message.role == "user":
            return message.content
    return ""

def get_full_context(messages):
    text = ""

    for message in messages:
        text += f"{message.role}: {message.content}\n"

    return text

def is_off_topic(text):
    text = text.lower()
    blocked_words = ["salary", "resume", "legal", "law", "interview tips", "career advice", "python code", "joke"]
    return any(word in text for word in blocked_words)

def is_vague(text):
    words = text.lower().split()
    vague_phrases = ["assessment", "test", "hiring", "i need assessment", "i need a test"]

    if len(words) < 5:
        return True

    return text.lower().strip() in vague_phrases

def is_compare_request(text):
    text = text.lower()
    compare_words = ["compare", "difference", "different", "vs", "versus"]
    return any(word in text for word in compare_words)

def build_recommendations(results):
    recommendations = []

    for item in results:
        recommendations.append({
            "name": item["name"],
            "url": item["url"],
            "test_type": item["test_type"]
        })

    return recommendations

def compare_assessments(user_text, catalog):
    matched = []

    for item in catalog:
        if item["name"].lower() in user_text.lower():
            matched.append(item)

    if len(matched) < 2:
        results = semantic_search(user_text, top_k=2)
        matched = results

    if len(matched) < 2:
        return {
            "reply": "Please mention two SHL assessment names you want me to compare.",
            "recommendations": [],
            "end_of_conversation": False
        }

    first = matched[0]
    second = matched[1]

    reply = generate_llm_reply(
    user_text,
    [first, second]
)
    
    return {
        "reply": reply,
        "recommendations": [],
        "end_of_conversation": False
    }

def generate_response(messages):
    catalog = load_catalog()
    user_text = get_last_user_message(messages)
    full_context = get_full_context(messages)

    if is_off_topic(user_text):
        return {
            "reply": "I can only help with SHL assessment recommendations and comparisons.",
            "recommendations": [],
            "end_of_conversation": False
        }

    if is_compare_request(user_text):
        return compare_assessments(user_text, catalog)

    if is_vague(user_text):
        return {
            "reply": "Sure. What role are you hiring for, what seniority level is it, and which skills do you want to assess?",
            "recommendations": [],
            "end_of_conversation": False
        }

    results = semantic_search(full_context, top_k=10)

    if not results:
        return {
            "reply": "I could not find a strong SHL assessment match from the current catalog data. Please share the role, skills, and seniority level.",
            "recommendations": [],
            "end_of_conversation": False
        }

    recommendations = build_recommendations(results)

    reply = generate_llm_reply(user_text, results)

    return {
        "reply": reply,
        "recommendations": recommendations,
        "end_of_conversation": True
    }