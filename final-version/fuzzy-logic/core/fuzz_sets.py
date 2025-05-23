from constants.labels import LABELS

class FuzzySymptom:
    def __init__(self, name: str, values: dict):
        self.name = name
        self.values = values

    def match(self, expected_values: dict) -> float:
        return max(
            min(self.values.get(label, 0.0), expected_values.get(label, 0.0))
            for label in LABELS
        )
