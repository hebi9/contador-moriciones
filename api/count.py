from flask import Flask, request, jsonify

app = Flask(__name__)

contador = {"count": 179}

@app.route("/api/count", methods=["GET"])
def get_count():
    return jsonify(contador)

@app.route("/api/count", methods=["POST"])
def set_count():
    data = request.json
    contador["count"] = int(data["count"])
    return jsonify(ok=True, count=contador["count"])