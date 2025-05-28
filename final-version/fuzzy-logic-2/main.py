from src.fuzzy_system import run_inference

patient_symptoms = {
    "fever": "medium",
    "cough": "medium",
    "headache": "medium",
}

if __name__ == '__main__':
    results = run_inference(patient_symptoms)
    print("\nЙмовірність кожної хвороби:")
    for disease, val in results.items():
        print(f"  - {disease}: {val:.2f}")