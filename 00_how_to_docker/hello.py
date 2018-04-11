from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return ('<!DOCTYPE html><html><head><title></title></head><body><h1>Hello World</h1></body></html>')
