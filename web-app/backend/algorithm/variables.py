import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import json


def create_variables_from_rules(filepath):
    with open(filepath, 'r') as file:
        disease_map = json.load(file)

    input_vars = set()
    for symptoms in disease_map.values():
        input_vars.update(symptoms.keys())

    variable_refs = {}
    for name in input_vars:
        var = ctrl.Antecedent(np.arange(0, 11, 1), name)
        var['low'] = fuzz.trimf(var.universe, [0, 0, 5])
        var['medium'] = fuzz.trimf(var.universe, [3, 5, 7])
        var['high'] = fuzz.trimf(var.universe, [5, 10, 10])
        variable_refs[name] = var

    # окремі вихідні змінні для кожної хвороби
    for disease in disease_map:
        diagnosis = ctrl.Consequent(np.arange(0, 1.1, 0.1), disease)
        diagnosis['no'] = fuzz.trimf(diagnosis.universe, [0, 0, 0.5])
        diagnosis['maybe'] = fuzz.trimf(diagnosis.universe, [0.25, 0.5, 0.75])
        diagnosis['yes'] = fuzz.trimf(diagnosis.universe, [0.5, 1, 1])
        variable_refs[disease] = diagnosis

    return variable_refs