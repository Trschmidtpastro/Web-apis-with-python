from flask import Flask, jsonify, request
# Intitialise the app
app = Flask(__name__)
# Define what the app does
@app.route("/greeting")
def index():
    response = {"data":"Hello World !!!"}
    return jsonify(response)

