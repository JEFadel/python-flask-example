from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")

def health():
    return str(os.environ.get("STATUS"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)

    # sudo apt install python3-pip
    # pip install -r requirements.txt