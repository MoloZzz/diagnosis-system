import csv
import json

symptoms = []

with open('datasets/SYMP.csv', mode='r', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        symptom = {
            "class_id": row.get("Class ID", "").strip() or None,
            "code": row.get("http://www.geneontology.org/formats/oboInOwl#id", "").strip() or None,
            "preferred_label": row.get("Preferred Label", "").strip() or None,
            "synonyms": [],
            "definition": row.get("definition", "").strip() or row.get("Definitions", "").strip() or None,
            "parent_id": row.get("Parents", "").strip() or None,
            "is_obsolete": row.get("Obsolete", "").strip().lower() == "true"
        }

        # Обробка синонімів (розділені через |)
        synonyms_field = row.get("Synonyms", "") or row.get("has_exact_synonym", "")
        if synonyms_field:
            symptom["synonyms"] = [s.strip() for s in synonyms_field.split("|") if s.strip()]

        symptoms.append(symptom)

with open('symptoms.json', mode='w', encoding='utf-8') as json_file:
    json.dump(symptoms, json_file, indent=2, ensure_ascii=False)
