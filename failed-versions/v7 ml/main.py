from src.predictor import predict_disease

if __name__ == "__main__":
    input_symptoms = {
        "висока температура": "сильний",
        "кашель": "помірний",
        "втома": "слабкий"
    }

    prediction = predict_disease(input_symptoms)

    print("Можливі хвороби (від найймовірнішої):")
    for disease, score in prediction.items():
        print(f"{disease}: {score:.2f}")
