import pandas as pd
import json
from collections import defaultdict
from tqdm import tqdm

# Завантаження датасету
df = pd.read_csv('./datasets/DiseaseAndSymptoms.csv')


disease_symptom_counts = defaultdict(lambda: defaultdict(int))
disease_counts = defaultdict(int)

# Збираємо статистику
for _, row in df.iterrows():
    disease = row['Disease']
    disease_counts[disease] += 1
    for symptom in row[1:]:
        if pd.notna(symptom):
            symptom = symptom.strip()
            disease_symptom_counts[disease][symptom] += 1

# Побудова бази знань (flat structure)
knowledge_base = {}
for disease, symptoms in disease_symptom_counts.items():
    total_cases = disease_counts[disease]
    knowledge_base[disease] = {
        symptom: round(count / total_cases, 2)
        for symptom, count in symptoms.items()
    }

# Зберігаємо
with open('knowledge_base.json', 'w') as f:
    json.dump(knowledge_base, f, indent=2)

print("✅ Плоска база знань збережена у knowledge_base.json")