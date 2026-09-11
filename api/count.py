from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path

app = Flask(__name__)

contador = {"count": 179}

ROOT = Path(__file__).resolve().parent.parent

# Página principal
@app.route("/")
def index():
    return send_from_directory(ROOT, "index.html")

# API
@app.route("/api/count", methods=["GET"])
def get_count():
    return jsonify(contador)

@app.route("/api/count", methods=["POST"])
def set_count():
    data = request.get_json()
    contador["count"] = int(data["count"])
    return jsonify({"ok": True, "count": contador["count"]})