# main.py
from flask import Flask, request, jsonify
import hazelcast

hz_client = hazelcast.HazelcastClient(cluster_members=["hazelcast:5701"])
cache = hz_client.get_map("calc-cache").blocking()

app = Flask(__name__)

def cached_operation(op_name, a, b):
    key = f"{op_name}:{a}:{b}"
    if cache.contains_key(key):
        return cache.get(key)
    else:
        if op_name == "add":
            result = a + b
        elif op_name == "subtract":
            result = a - b
        elif op_name == "multiply":
            result = a * b
        else:
            raise ValueError("Unsupported operation")

        cache.put(key, result)
        return result

@app.route("/add")
def add_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": cached_operation("add", a, b)})

@app.route("/subtract")
def subtract_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": cached_operation("subtract", a, b)})

@app.route("/multiply")
def multiply_route():
    a = int(request.args.get("a", 0))
    b = int(request.args.get("b", 0))
    return jsonify({"result": cached_operation("multiply", a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
