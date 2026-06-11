from flask import Flask, request, jsonify
from flask_cors import CORS
import redis
import os

app = Flask(__name__)
CORS(app)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"), port=6379, decode_responses=True
)


@app.route("/feedback", methods=["GET"])
def get_feedback():
    feedback = redis_client.lrange("feedback", 0, -1)
    return jsonify(feedback)


@app.route("/feedback", methods=["POST"])
def add_feedback():
    data = request.json

    message = data.get("message")

    if not message:
        return jsonify({"error": "Message required"}), 400

    redis_client.rpush("feedback", message)

    return jsonify({"status": "success"}), 201


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
