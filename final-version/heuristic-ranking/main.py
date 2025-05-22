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

def diagnose_probabilistic(input_symptoms, disease_data):
    results = {}

    for disease, symptoms_info in disease_data.items():
        matched_score = 0.0
        max_possible_score = 0.0

        for symptom, degree in input_symptoms.items():
            max_possible_score += 1.0  # Кожен введений симптом має макс бал 1
            if symptom in symptoms_info:
                matched_score += symptoms_info[symptom].get(degree, 0.0)
            else:
                matched_score += 0.0  # Симптом відсутній — 0

        probability = matched_score / max_possible_score if max_possible_score > 0 else 0.0
        results[disease] = round(probability, 3)

    # Сортування від найвищої ймовірності до найменшої
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results

results = diagnose_probabilistic(input_symptoms, disease_data)

print("Ймовірні хвороби:")
for disease, prob in results:
    print(f"{disease}: {prob:.3f}")
