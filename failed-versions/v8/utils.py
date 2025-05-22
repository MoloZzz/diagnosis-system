import json
from typing import Dict

def load_json(file_path):
    """Завантаження JSON-файлу"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, file_path):
    """Збереження JSON-файлу"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_knowledge_base(file_path: str) -> Dict:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_knowledge_base(file_path: str, data: Dict):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def normalize_intensity(level):
    """Перетворює рівень вираженості у числовий формат для нечіткої логіки"""
    mapping = {
        "слабкий": 0.3,
        "помірний": 0.6,
        "сильний": 0.9
    }
    return mapping.get(level.lower(), 0.0)

def fuzzy_membership_name(value):
    """Перетворює числове значення на назву (для UI)"""
    if value <= 0.3:
        return "слабкий"
    elif value <= 0.6:
        return "помірний"
    else:
        return "сильний"
