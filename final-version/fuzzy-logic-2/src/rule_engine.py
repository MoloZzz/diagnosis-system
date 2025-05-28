import json
from skfuzzy import control as ctrl

def load_disease_rules(filepath, variable_refs):
    with open(filepath, 'r') as file:
        disease_map = json.load(file)

    rules = []
    for disease, symptoms in disease_map.items():
        condition = None
        for symptom, level in symptoms.items():
            if symptom not in variable_refs:
                continue
            term = variable_refs[symptom][level]
            condition = term if condition is None else condition & term

        if condition and disease in variable_refs:
            rules.append(ctrl.Rule(condition, variable_refs[disease]['yes']))

    return rules
