from src import diagnose, get_symptoms, get_diseases

patient_symptoms = {
    "fever": "medium",
    "cough": "medium",
    "headache": "medium",
}

if __name__ == '__main__':
    results = diagnose(patient_symptoms)
    print("\nЙмовірність кожної хвороби:")
    for disease, val in results.items():
        print(f"  - {disease}: {val:.2f}")