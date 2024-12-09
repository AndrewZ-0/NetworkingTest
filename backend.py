from flask import Flask, request, jsonify
from flask_cors import CORS

import subprocess

app = Flask(__name__)
CORS(app)

@app.route("/out", methods = ["GET"])
def send_data():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/sort", methods = ["POST"])
def sort():
    data = request.data.decode("utf-8")

    print(f"Received:", data)

    sorted_vals = cppSort([int(val) for val in data.split(",")])

    print(f"Sending: {sorted_vals}")

    return jsonify({"sorted_vals": sorted_vals})


def start_process():
    subprocess.run(["c++", "-o", "sorter", "sorter.cpp"])

    return subprocess.Popen(
        ["./server/sorter"],
        stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )

def cppSort(vals):
    process.stdin.write(f"{len(vals)}\n")

    for val in vals:
        process.stdin.write(f"{val}\n")
    process.stdin.flush()

    return [int(val) for val in process.stdout.readline().split(",")]


if __name__ == '__main__':
    process = start_process()

    app.run(host = "0.0.0.0", port = 1234, debug = False)
