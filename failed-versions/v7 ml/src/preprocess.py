import pandas as pd

intensity_map = {
    "слабкий": 0.2,
    "помірний": 0.5,
    "сильний": 1.0
}

def build_feature_matrix(records):
    # Всі унікальні симптоми
    all_symptoms = set()
    for rec in records:
        all_symptoms.update(rec["symptoms"].keys())
    all_symptoms = sorted(list(all_symptoms))

    X, y = [], []
    for rec in records:
        row = []
        for s in all_symptoms:
            if s in rec["symptoms"]:
                row.append(intensity_map[rec["symptoms"][s]])
            else:
                row.append(0.0)
        X.append(row)
        y.append(rec["diagnosis"])

    df = pd.DataFrame(X, columns=all_symptoms)
    return df, y
