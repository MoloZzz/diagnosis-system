from utils.load_data import load_data
from core.engine import diagnose

if __name__ == '__main__':
    symptoms, diseases, rules = load_data()
    print("Дані про симптоми:", symptoms)
    
    patient_data = {
        'Насмарк': {'Слабко виражений': 1.0, 'Помірно виражений': 0.2, 'Яскраво виражений': 0.1},
        'Висока температура': {'Слабко виражений': 0.0, 'Помірно виражений': 0.5, 'Яскраво виражений': 0.4},
        'Задишка': {'Слабко виражений': 0.0, 'Помірно виражений': 1.0, 'Яскраво виражений': 0.0}
    }

    
    results = diagnose(patient_data, symptoms, diseases, rules)
    print("Результати діагностики:")
    for disease, score in results:
        desc = diseases.get(disease, {}).get('description', '')
        print(f"{disease}: {score:.2f} - {desc}")