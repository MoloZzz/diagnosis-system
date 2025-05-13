import pandas as pd
import json

# Завантаження датасету
df = pd.read_csv('./datasets/DiseaseAndSymptoms.csv')

knowledge_base = {}

# Обробка кожного запису
for index, row in df.iterrows():
    disease = row['Disease']
    symptoms = []

    # Проходимося по всіх колонках, які містять симптоми
    for col in row.index:
        if col.startswith('Symptom') and pd.notna(row[col]):
            symptom = str(row[col]).strip().lower()
            symptoms.append(symptom)

    # Додаємо симптоми до бази знань
    if disease not in knowledge_base:
        knowledge_base[disease] = {}

    for symptom in symptoms:
        # Призначаємо вагу (можна пізніше адаптувати, наприклад за важливістю)
        knowledge_base[disease][symptom] = 1.0

# Збереження бази знань у форматі JSON
with open('knowledge_base.json', 'w', encoding='utf-8') as f:
    json.dump(knowledge_base, f, ensure_ascii=False, indent=4)
