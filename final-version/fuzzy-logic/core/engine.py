from constants.labels import LABELS

def diagnose(patient_data, symptoms, diseases, rules):
    results = {}

    for disease, conditions in rules.items():
        scores = []
        for condition in conditions:
            symptom = condition['symptom']
            expected_set = condition['expected']
            
            # Якщо у пацієнта немає даних по симптомі, пропускаємо
            if symptom not in patient_data:
                continue
            
            user_set = patient_data[symptom]
            
            # Обчислюємо ступінь відповідності (максимум мінімумів по лейблах)
            match_score = max(
                min(user_set.get(label, 0.0), expected_set.get(label, 0.0))
                for label in LABELS
            )
            scores.append(match_score)
        
        if scores:
            results[disease] = sum(scores) / len(scores)
        else:
            results[disease] = 0.0
    
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)
    return sorted_results
