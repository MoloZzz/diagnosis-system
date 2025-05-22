import json
from typing import Dict

class DiagnosisEngine:
    def __init__(self, disease_db: Dict[str, Dict[str, Dict[str, float]]]):
        self.disease_db = disease_db
        self.levels = ["low", "medium", "high"]
        self.level_functions = {
            "low": lambda x: max(0, 1 - x * 2) if x <= 0.5 else 0,
            "medium": lambda x: 1 - abs(x - 0.5) * 2,
            "high": lambda x: max(0, (x - 0.5) * 2) if x >= 0.5 else 0
        }

    def fuzzify(self, value: float) -> Dict[str, float]:
        return {level: round(f(value), 3) for level, f in self.level_functions.items()}

    def diagnose(self, input_symptoms: Dict[str, float]) -> Dict[str, float]:
        results = {}
        for disease, symptoms_profile in self.disease_db.items():
            score = 0
            relevant_symptoms = 0

            for symptom, profile_levels in symptoms_profile.items():
                if symptom not in input_symptoms:
                    continue

                input_fuzzy = self.fuzzify(input_symptoms[symptom])
                match_score = sum(
                    input_fuzzy[level] * profile_levels.get(level, 0)
                    for level in self.levels
                )
                score += match_score
                relevant_symptoms += 1

            results[disease] = round(score / relevant_symptoms, 3) if relevant_symptoms else 0.0

        return dict(sorted(results.items(), key=lambda item: item[1], reverse=True))

# utils.py

def load_knowledge_base(file_path: str) -> Dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_knowledge_base(file_path: str, data: Dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# train.py

if __name__ == "__main__":
    # Можна доповнити або змінити базу знань тут
    knowledge_base = {
        "flu": {
            "fever": {"low": 0, "medium": 0, "high": 1},
            "cough": {"low": 0.1, "medium": 0.8, "high": 0.1}
        },
        "cold": {
            "fever": {"low": 0.7, "medium": 0.3, "high": 0},
            "cough": {"low": 0.2, "medium": 0.6, "high": 0.2}
        },
        "migraine": {
            "headache": {"low": 0, "medium": 0.1, "high": 0.9},
            "fever": {"low": 0.6, "medium": 0.3, "high": 0.1}
        }
    }
    save_knowledge_base("knowledge_base.json", knowledge_base)
