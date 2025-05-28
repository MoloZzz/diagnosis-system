import json
from skfuzzy import control as ctrl
import itertools


def generate_partial_rule_combinations(symptoms_dict, min_conditions=2):
    """
    Генерує всі можливі підмножини умов розміром >= min_conditions
    """
    keys = list(symptoms_dict.keys())
    combinations = []
    for r in range(len(keys), min_conditions - 1, -1):
        for combo in itertools.combinations(keys, r):
            partial = {k: symptoms_dict[k] for k in combo}
            combinations.append((partial, r))
    return combinations


def load_disease_rules(filepath, variable_refs, min_conditions=2):
    with open(filepath, 'r') as file:
        disease_map = json.load(file)

    rules = []
    for disease, symptoms in disease_map.items():
        full_len = len(symptoms)
        partial_rules = generate_partial_rule_combinations(symptoms, min_conditions=min_conditions)

        for pr_dict, length in partial_rules:
            condition = None
            skip = False
            for symptom, level in pr_dict.items():
                if symptom not in variable_refs:
                    skip = True
                    break
                term = variable_refs[symptom][level]
                condition = term if condition is None else condition & term

            if not skip and condition and disease in variable_refs:
                # Пріоритет повного правила > часткового (через множення)
                if length == full_len:
                    rules.append(ctrl.Rule(condition, variable_refs[disease]['yes']))
                else:
                    # Для часткових — слабший вплив: використовуємо 'maybe'
                    rules.append(ctrl.Rule(condition, variable_refs[disease]['maybe']))

    return rules
