import os
from flask import Flask, request

app = Flask(__name__)

# ❌ Example of insecure code (for demo only!)
@app.route("/run", methods=["GET"])
def run_command():
    cmd = request.args.get("cmd")
    return os.popen(cmd).read()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
