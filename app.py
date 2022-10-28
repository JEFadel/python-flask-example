from flask import Flask
import os

app = Flask(__name__)

@app.route("/health")

def health():
    return str(os.environ.get("STATUS"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=(os.environ.get("APP_PORT")), debug=True)

    # sudo apt install python3-pip
    # pip install -r requirements.txt
    # Oi, profº, deixando esse comentário só pra não dizer que meu código ficou igual o de todo mundo :P
    
    # docker build . -t localhost:32000/app-flask:latest
    # docker run --rm -d -e APP_PORT=3333