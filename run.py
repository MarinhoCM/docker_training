from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def start():
    return "Olá estou aqui!"