from pathlib import Path
import json

def load_data(data_dir='data'):
    data_path = Path(data_dir)
    
    with open(data_path / 'symptoms.json', 'r', encoding='utf-8') as f:
        symptoms = json.load(f)
        
    with open(data_path / 'diseases.json', 'r', encoding='utf-8') as f:
        diseases = json.load(f)
        
    with open(data_path / 'rules.json', 'r', encoding='utf-8') as f:
        rules = json.load(f)
        
    return symptoms, diseases, rules
