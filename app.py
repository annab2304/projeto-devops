from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Minha app com Docker 🚀"

@app.route("/status")
def status():
    return "OK"

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b