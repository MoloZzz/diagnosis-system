import json
from pathlib import Path

# --- Load data ---
BASE_DIR = Path(__file__).parent

with open(BASE_DIR / "data" / "symptoms.json") as f:
    symptoms = json.load(f)

with open(BASE_DIR / "data" / "diseases.json") as f:
    diseases = json.load(f)

with open(BASE_DIR / "data" / "relations.json") as f:
    relations = json.load(f)

with open(BASE_DIR / "input" / "patient_input.json") as f:
    patient_data = json.load(f)

# --- Fuzzy similarity function ---
def fuzzy_similarity(disease_symptoms, patient_symptoms):
    sim_scores = []
    for symptom, patient_levels in patient_symptoms.items():
        if symptom in disease_symptoms:
            disease_levels = disease_symptoms[symptom]
            sim = sum(
                min(disease_levels.get(level, 0), patient_levels.get(level, 0))
                for level in ["low", "medium", "high"]
            )
            sim_scores.append(sim / 3)  # normalize
    return sum(sim_scores) / len(sim_scores) if sim_scores else 0

# --- Run diagnosis ---
results = []
for disease in diseases:
    score = fuzzy_similarity(relations[disease], patient_data)
    results.append((disease, round(score, 3)))

# --- Sort by similarity ---
results.sort(key=lambda x: x[1], reverse=True)

# --- Output ---
print("🔍 Diagnosis Results:")
for disease, score in results:
    print(f"  - {disease.capitalize():<10}: {score:.2f}")
