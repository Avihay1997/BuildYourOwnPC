from flask import Flask, jsonify

app = Flask(__name__)

components = [
    {"id": 1, "type": "CPU", "name": "Intel i7 12700K", "price": 1300},
    {"id": 2, "type": "GPU", "name": "NVIDIA RTX 4070", "price": 2500},
    {"id": 3, "type": "RAM", "name": "Corsair 16GB DDR5", "price": 450},
]

@app.route("/components", methods=["GET"])
def get_components():
    return jsonify(components)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
