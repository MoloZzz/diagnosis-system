import json

FIELDS_TO_KEEP = [
    "name",
    "text",
    "category",
    "IsRare",
    "IsGenderSpecific",
    "IsImmLifeThreatening",
    "IsCantMiss",
    "Risk",
    "ICD10"
]

with open('datasets/DiseasesOutput.json', mode='r', encoding='utf-8') as json_file:
    raw_data = json.load(json_file)

filtered_data = []
for item in raw_data:
    filtered_item = {key: item[key] for key in FIELDS_TO_KEEP if key in item}
    filtered_data.append(filtered_item)

with open('./knowledge-data/diseases.json', mode='w', encoding='utf-8') as out_file:
    json.dump(filtered_data, out_file, indent=2, ensure_ascii=False)

print(f"Файл успішно збережено: {len(filtered_data)} записів")
