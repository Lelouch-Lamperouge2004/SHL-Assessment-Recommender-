import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("catalog.json", "r", encoding="utf-8") as file:
    catalog = json.load(file)

texts = []

for item in catalog:
    text = f"{item['name']} {item['description']} {item['test_type']}"
    texts.append(text)

vectorizer = TfidfVectorizer(stop_words="english")
matrix = vectorizer.fit_transform(texts)

def keyword_boost(query, item):
    query = query.lower()
    name = item["name"].lower()
    description = item["description"].lower()
    test_type = item["test_type"].lower()

    score = 0

    important_keywords = [
        "java",
        "python",
        "sql",
        "javascript",
        "frontend",
        "front end",
        "backend",
        "numerical",
        "deductive",
        "inductive",
        "reasoning",
        "personality",
        "communication",
        "leadership",
        "customer service",
        "sales",
        "manager",
        "account manager"
    ]

    for word in important_keywords:
        if word in query and (word in name or word in description or word in test_type):
            score += 2

    return score

def semantic_search(query, top_k=10):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix)[0]

    ranked = []

    for index, score in enumerate(scores):
        final_score = score + keyword_boost(query, catalog[index])
        if final_score > 0:
            ranked.append((final_score, catalog[index]))

    ranked.sort(key=lambda x: x[0], reverse=True)

    results = []

    for score, item in ranked[:top_k]:
        results.append(item)

    return results