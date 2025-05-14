import json

with open('./knowledge-base/disease_symptoms.json', 'r', encoding='utf-8') as f:
    disease_db = json.load(f)

# Значення: 0.0 — немає, 0.5 — помірно, 1.0 — сильно
user_symptoms = {
    "fever": 0.5,
    "headache": 0.5,
    "muscle pain": 0.5,
    'sore throat': 0.5,
}

def score_diseases(user_symptoms, disease_db):
    scores = {}

    for disease, symptoms in disease_db.items():
        total_score = 0.0
        count = 0

        for symptom, user_value in user_symptoms.items():
            disease_value = symptoms.get(symptom)
            if disease_value is not None:
                similarity = 1 - abs(user_value - disease_value)  # the closer, the better
                total_score += similarity
                count += 1

        if count > 0:
            scores[disease] = round((total_score / count) * 100, 2)
        else:
            scores[disease] = 0.0

    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

if __name__ == "__main__":
    results = score_diseases(user_symptoms, disease_db)
    print("Ймовірні діагнози:")
    for disease, probability in results.items():
        print(f"- {disease}: {probability}%")
