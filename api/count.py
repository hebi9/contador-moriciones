from flask import Flask, request, jsonify

app = Flask(__name__)

contador = {"count": 179}

@app.route("/", methods=["GET"])
def get_count():
    return jsonify(contador)

@app.route("/", methods=["POST"])
def set_count():
    data = request.get_json()
    contador["count"] = int(data["count"])
    return jsonify({"ok": True, "count": contador["count"]})