import json
from src.fuzzy_model import symptom_vector

def predict_disease(input_symptoms):
    with open("data/disease_symptom_map.json", encoding="utf-8") as f:
        disease_map = json.load(f)

    results = {}
    for disease, symptom_profiles in disease_map.items():
        match_score = 0
        matched = 0

        for symptom, intensity in input_symptoms.items():
            if symptom in symptom_profiles:
                patient_vec = symptom_vector(intensity)
                profile_vec = symptom_profiles[symptom]

                # Скалярний добуток як метрика схожості
                match = sum(min(patient_vec[k], profile_vec[k]) for k in profile_vec)
                match_score += match
                matched += 1

        if matched:
            results[disease] = match_score / matched

    return dict(sorted(results.items(), key=lambda x: x[1], reverse=True))
