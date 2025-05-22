import json

# Завантаження бази знань
with open("./data/disease_symptom.json", "r", encoding="utf-8") as f:
    disease_data = json.load(f)

# Вхідні симптоми
input_symptoms = {
    "висока температура": "сильний",
    "кашель": "помірний",
    "втома": "слабкий"
}

def diagnose(symptoms_input, disease_db):
    scores = {}

    for disease, symptom_probs in disease_db.items():
        total_score = 0.0
        for symptom, degree in symptoms_input.items():
            # Якщо симптом є у хвороби
            if symptom in symptom_probs:
                probability = symptom_probs[symptom].get(degree, 0.0)
                total_score += probability
        scores[disease] = total_score

    # Сортуємо хвороби за зменшенням балів
    sorted_diseases = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_diseases

# Виклик
result = diagnose(input_symptoms, disease_data)

# Вивід
print("Ймовірні хвороби:")
for disease, score in result:
    print(f"{disease}: {score:.2f}")
