import json
import pandas as pd
from sklearn.ensemble import RandomForestClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
import joblib
from preprocess import intensity_map, build_feature_matrix

# Завантаження
with open("data/dataset.json", "r", encoding='utf-8') as f:
    records = json.load(f)

X, y = build_feature_matrix(records)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Навчання
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Збереження
joblib.dump(model, "model.pkl")
print("Accuracy:", model.score(X_test, y_test))
