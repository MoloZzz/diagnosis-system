import json
import os
from typing import Dict
from collections import defaultdict

DATA_DIR = "data"

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), encoding="utf-8") as f:
        return json.load(f)

def normalize_scores(scores: Dict[str, float]) -> Dict[str, float]:
    max_score = max(scores.values()) if scores else 1
    return {disease: round(score / max_score, 3) for disease, score in scores.items()}

def diagnose(patient_symptoms: Dict[str, str], disease_symptoms: Dict) -> Dict[str, float]:
    scores = defaultdict(float)

    for disease, symptoms in disease_symptoms.items():
        for symp, degree in patient_symptoms.items():
            if symp in symptoms:
                prob = symptoms[symp].get(degree, 0)
                scores[disease] += prob

    return normalize_scores(scores)

def main():
    print("Завантаження бази знань...")
    symptoms = load_json("symptoms.json")
    diseases = load_json("diseases.json")
    disease_symptom_data = load_json("disease_symptoms.json")

    # Вхід користувача: симптоми з вираженістю
    patient_symptoms = {
        "кашель": "сильний",
        "висока температура": "помірний"
    }

    print("\n🩺 Симптоми пацієнта:")
    for k, v in patient_symptoms.items():
        print(f"  - {k}: {v}")

    result = diagnose(patient_symptoms, disease_symptom_data)

    print("\n📋 Ймовірні хвороби:")
    for disease, score in sorted(result.items(), key=lambda x: x[1], reverse=True):
        print(f"  {disease}: {score}")

if __name__ == "__main__":
    main()
