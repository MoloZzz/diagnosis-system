labels = ['Слабко виражений', 'Помірно виражений', 'Яскраво виражений']

A1 = {'Слабко виражений': 1.0, 'Помірно виражений': 0.2, 'Яскраво виражений': 0.1}
A2 = {'Слабко виражений': 0.0, 'Помірно виражений': 1.0, 'Яскраво виражений': 0.0}
A3 = {'Слабко виражений': 0.1, 'Помірно виражений': 0.0, 'Яскраво виражений': 1.0}
A4 = {'Слабко виражений': 0.0, 'Помірно виражений': 0.5, 'Яскраво виражений': 0.4}

rules = {
    'Грип': [('Насмарк', A3), ('Висока температура', A2), ('Насмарк', A1)],
    'Covid': [('Висока температура', A3), ('Втрата смаку', A2), ('Задишка', A1)],
    'Застуда': [('Висока температура', A1), ('Насмарк', A2), ('Втрата смаку', A1)],
    'Алергія': [('Насмарк', A1), ('Задишка', A2)],
}

patient_data = {
    'Насмарк': A1,
    'Висока температура': A4,
    'Насмарк': A1,
    'Задишка': A1
    # Втрата смаку – відсутній
}

results = {}
explanations = {}

for disease, conditions in rules.items():
    scores = []
    details = []
    for var, expected_set in conditions:
        if var not in patient_data:
            details.append(f"- {var}: ❌ Відсутній у пацієнта")
            continue

        user_set = patient_data[var]
        match_score = max(
            min(user_set[label], expected_set.get(label, 0.0)) for label in labels
        )
        scores.append(match_score)

        # Побудова текстового пояснення
        details.append(
            f"- {var}:\n"
            f"    Очікуване: {expected_set}\n"
            f"    У пацієнта: {user_set}\n"
            f"    Відповідність: {match_score:.2f}"
        )

    if scores:
        avg_score = sum(scores) / len(scores)
    else:
        avg_score = 0.0

    results[disease] = avg_score
    explanations[disease] = "\n".join(details)

sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

print("🔍 Результати діагностики:\n")
for disease, score in sorted_results:
    print(f"✅ {disease}: {score:.2f}")
    print(explanations[disease])
    print("-" * 50)
