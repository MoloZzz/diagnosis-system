from src.variables import create_variables_from_rules
from src.rule_engine import load_disease_rules
from skfuzzy import control as ctrl

rules_path = "./data/rules.json"
variable_refs = create_variables_from_rules(rules_path)
rules = load_disease_rules(rules_path, variable_refs)
diagnosis_ctrl = ctrl.ControlSystem(rules)

def resolve_input_value(var, val):
    mapping = {
        "low": 2,
        "medium": 5,
        "high": 8
    }
    if isinstance(val, str) and val.lower() in mapping:
        return mapping[val.lower()]
    raise ValueError(f"Симптом '{var}' повинен мати значення 'low', 'medium' або 'high'.")

def run_inference(inputs):
    diagnosis = ctrl.ControlSystemSimulation(diagnosis_ctrl)

    for var in [v for v in variable_refs if isinstance(variable_refs[v], ctrl.Antecedent)]:
        raw_val = inputs.get(var, "medium")
        diagnosis.input[var] = resolve_input_value(var, raw_val)

    diagnosis.compute()

    results = {}
    for disease in [k for k in variable_refs if isinstance(variable_refs[k], ctrl.Consequent)]:
        results[disease] = diagnosis.output.get(disease, 0.0)

    return results