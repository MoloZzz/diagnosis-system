from owlready2 import get_ontology
import json

onto = get_ontology("http://purl.obolibrary.org/obo/doid.owl").load()
diseases = [{"id": cls.name, "label": cls.label[0]} for cls in onto.classes()]

with open('diseases.json', mode='w', encoding='utf-8') as json_file:
    json.dump(diseases, json_file, indent=2, ensure_ascii=False)