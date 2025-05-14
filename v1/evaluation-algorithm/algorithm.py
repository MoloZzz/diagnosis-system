import json

with open('./knowledge-base/knowledge_base3.json', 'r', encoding='utf-8') as f:
    disease_db = json.load(f)

# Значення: 0.0 — немає, 0.5 — помірно, 1.0 — сильно
user_symptoms = {
    "high_fever": 0.7,
    "runny_nose": 0.5,
    "sore_throat": 0.5,
    'loss_of_smell': 0.7,
}

def score_diseases(user_symptoms, disease_db):
    scores = {}

    for disease, symptoms in disease_db.items():
        score = 0
        max_possible = 0
        for symptom, intensity in user_symptoms.items():
            weight = symptoms.get(symptom)
            if weight:
                score += weight * intensity
                max_possible += weight 

        if max_possible > 0:
            scores[disease] = round((score / max_possible) * 100, 2)
        else:
            scores[disease] = 0.0

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    results = score_diseases(user_symptoms, disease_db)
    print("Ймовірні діагнози:")
    for disease, probability in results.items():
        print(f"- {disease}: {probability}%")
