from flask import Flask
import os

app = Flask(__name__)
count = 0

@app.route("/")
def hello_world():
    return "Olá. professor!"

@app.route("/health")
def health():
    return "OK"

@app.route("/counter")
def counter():
    global count
    count += 1
    return str(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=(os.environ.get("APP_PORT")), debug=True)

    # sudo apt install python3-pip
    # pip install -r requirements.txt
    # Oi, profº, deixando esse comentário só pra não dizer que meu código ficou igual o de todo mundo :P
    
    # git add .
    # git commit -m [MENSAGEM]
    # git push origin kubernetes/desafio-01

    # docker build . -t localhost:32000/app-flask:latest
    # docker save localhost:32000/app-flask:latest > myimage.tar
    # microk8s ctr image import myimage.tar
    # docker run --rm -d -e APP_PORT=3500 -p 3500:3500 localhost:32000/app-flask:latest

    # kubectl port-forward 