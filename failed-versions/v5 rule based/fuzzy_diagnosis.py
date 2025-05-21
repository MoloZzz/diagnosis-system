import json

class FuzzyDiagnosisSystem:
    def __init__(self, diseases_file, rules_file):
        with open(diseases_file, 'r', encoding='utf-8') as f:
            self.diseases = json.load(f)
        with open(rules_file, 'r', encoding='utf-8') as f:
            self.rules = json.load(f)

    def fuzzy_and(self, a, b):
        return min(a, b)

    def match_symptom(self, patient_symptom, rule_symptom):
        # ∀ label ∈ ("слабкий", "помірний", "сильний") беремо min(patient, rule)
        return min(patient_symptom.get(k, 0.0) for k in rule_symptom)

    def rule_activation(self, rule, observation):
        activations = []
        for symptom, expected_fuzzy in rule["if"].items():
            if symptom in observation:
                activation = self.match_symptom(observation[symptom], expected_fuzzy)
                activations.append(activation)
            else:
                activations.append(0.0)  # симптом відсутній
        return min(activations)  # AND по всіх симптомах

    def diagnose(self, observation):
        result = {}
        for rule in self.rules:
            disease = rule["then"]
            activation = self.rule_activation(rule, observation)
            if disease not in result:
                result[disease] = activation
            else:
                result[disease] = max(result[disease], activation)  # OR між правилами
        return result
