import json
from pathlib import Path
from .fuzzy_system import run_inference

BASE_DIR = Path(__file__).resolve().parent

SYMPTOMS_PATH = BASE_DIR / "data/symptoms.json"
DISEASES_PATH = BASE_DIR / "data/diseases.json"


def get_symptoms():
    with open(SYMPTOMS_PATH, "r") as f:
        return json.load(f)


def get_diseases():
    with open(DISEASES_PATH, "r") as f:
        return json.load(f)


def diagnose(symptoms_dict):
    return run_inference(symptoms_dict)
