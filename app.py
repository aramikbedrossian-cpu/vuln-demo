import subprocess

@app.route("/run", methods=["GET"])
def run_command():
    cmd = request.args.get("cmd")

    # Define a whitelist of allowed commands
    allowed_commands = {
        "date": ["date"],
        "uptime": ["uptime"],
        "whoami": ["whoami"]
    }

    if cmd not in allowed_commands:
        return "Invalid command", 400

    result = subprocess.run(allowed_commands[cmd], capture_output=True, text=True)
    return result.stdout
