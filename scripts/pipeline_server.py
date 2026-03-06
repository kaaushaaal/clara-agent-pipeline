from flask import Flask
import subprocess
import sys
import os

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run_pipeline():

    venv_python = os.path.join("venv", "Scripts", "python.exe")

    subprocess.run([venv_python, "scripts/run_all_accounts.py"], check=True)

    return {"status": "pipeline executed"}

if __name__ == "__main__":
    app.run(port=5000)