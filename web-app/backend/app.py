from flask import Flask, request, jsonify
from algorithm import get_symptoms, get_diseases, diagnose

app = Flask(__name__)

@app.route("/symptoms", methods=["GET"])
def symptoms():
    return jsonify(get_symptoms())

@app.route("/diseases", methods=["GET"])
def diseases():
    return jsonify(get_diseases())

@app.route("/diagnose", methods=["POST"])
def diagnosis():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON received"}), 400

    try:
        result = diagnose(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
