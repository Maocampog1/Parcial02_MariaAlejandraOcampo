from flask import Flask, jsonify, abort
import math

app = Flask(__name__)

def paridad(n: int) -> str:
    return "par" if (n % 2 == 0) else "impar"

@app.route("/api/factorial/<int:n>", methods=["GET"])
def get_factorial(n: int):
    if n < 0:
        abort(400, description="El factorial no está definido para negativos.")
    fact = math.factorial(n)
    data = {
        "numero": n,
        "factorial": str(fact),
        "paridad": paridad(n)   
    }
    return jsonify(data), 200

@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)
