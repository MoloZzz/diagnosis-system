def fuzzy_membership(intensity: str):
    return {
        "слабкий": [1.0, 0.2, 0.1],
        "помірний": [0.2, 1.0, 0.2],
        "сильний": [0.1, 0.2, 1.0]
    }[intensity]

def symptom_vector(intensity):
    levels = ["слабкий", "помірний", "сильний"]
    return dict(zip(levels, fuzzy_membership(intensity)))
