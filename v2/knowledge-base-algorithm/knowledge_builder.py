import pandas as pd
import json
from collections import defaultdict

df = pd.read_csv("./datasets/Final_Augmented_dataset_Diseases_and_Symptoms.csv")

disease_column = 'diseases'
symptom_columns = [col.strip() for col in df.columns if col != disease_column]

disease_symptom_counts = defaultdict(lambda: defaultdict(int))
disease_case_counts = defaultdict(int)

for _, row in df.iterrows():
    disease = row[disease_column].strip()
    disease_case_counts[disease] += 1
    for symptom in symptom_columns:
        if int(row[symptom]) == 1:
            disease_symptom_counts[disease][symptom] += 1

diseases = list(disease_case_counts.keys())

symptoms = symptom_columns

# Ймовірності: симптоми / кількість випадків
disease_symptom_probs = {}

for disease in diseases:
    total_cases = disease_case_counts[disease]
    symptom_probs = {
        symptom: round(disease_symptom_counts[disease][symptom] / total_cases, 2)
        for symptom in symptoms if disease_symptom_counts[disease][symptom] > 0
    }
    disease_symptom_probs[disease] = symptom_probs

with open("diseases.json", "w", encoding="utf-8") as f:
    json.dump(diseases, f, ensure_ascii=False, indent=2)

with open("symptoms.json", "w", encoding="utf-8") as f:
    json.dump(symptoms, f, ensure_ascii=False, indent=2)

with open("disease_symptoms.json", "w", encoding="utf-8") as f:
    json.dump(disease_symptom_probs, f, ensure_ascii=False, indent=2)

print("✅ Готово: створено 3 файли (diseases.json, symptoms.json, disease_symptoms.json)")
