import json
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

with open('./data/disease_symptom.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

user_symptoms = {
    "висока температура": "сильний",
    "кашель": "помірний",
    "втома": "помірний"
}

term_to_value = {
    'слабкий': 2,
    'помірний': 5,
    'сильний': 8
}

results = {}

for disease, symptoms in knowledge_base.items():
    used_inputs = {}
    rules = []

    for symptom, levels in symptoms.items():
        if symptom in user_symptoms:
            ant = ctrl.Antecedent(np.arange(0, 11, 1), symptom)
            ant['слабкий'] = fuzz.trimf(ant.universe, [0, 0, 5])
            ant['помірний'] = fuzz.trimf(ant.universe, [2, 5, 8])
            ant['сильний'] = fuzz.trimf(ant.universe, [5, 10, 10])
            used_inputs[symptom] = ant

    if not used_inputs:
        continue

    output = ctrl.Consequent(np.arange(0, 101, 1), 'result')
    output['низький'] = fuzz.trimf(output.universe, [0, 0, 50])
    output['середній'] = fuzz.trimf(output.universe, [25, 50, 75])
    output['високий'] = fuzz.trimf(output.universe, [50, 100, 100])

    for symptom, ant in used_inputs.items():
        level = user_symptoms[symptom]
        weight = symptoms[symptom][level]

        if weight >= 0.7:
            severity = 'високий'
        elif weight >= 0.4:
            severity = 'середній'
        else:
            severity = 'низький'

        rules.append(ctrl.Rule(ant[level], output[severity]))

    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    for symptom in used_inputs:
        sim.input[symptom] = term_to_value[user_symptoms[symptom]]

    sim.compute()
    results[disease] = sim.output['result']

print("\n Ймовірності діагнозів:")
for disease, prob in sorted(results.items(), key=lambda x: -x[1]):
    print(f"- {disease}: {prob:.1f}%")