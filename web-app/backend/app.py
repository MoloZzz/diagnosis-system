from flask import Flask, request, jsonify
from algorithm import get_symptoms, get_diseases, diagnose
from flask_cors import CORS
from logger import Logger

app = Flask(__name__)
logger = Logger("FlaskApp")
logger.info("Initializing Flask app...")
CORS(app)

@app.route("/symptoms", methods=["GET"])
def symptoms():
    logger.info("Fetching symptoms...")
    return jsonify(get_symptoms())

@app.route("/diseases", methods=["GET"])
def diseases():
    logger.info("Fetching diseases...")
    return jsonify(get_diseases())

@app.route("/diagnose", methods=["POST"])
def diagnosis():
    data = request.get_json()
    if not data:
        logger.error("No JSON received")
        return jsonify({"error": "No JSON received"}), 400

    try:
        result = diagnose(data)
        logger.info(f"Diagnosis completed successfully: symptoms={data}, diseases={result}")
        return jsonify(result)
    except Exception as e:
        logger.error(f"Error occurred during diagnosis: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logger.info("Starting Flask app...")
    app.run(debug=True)
