from flask import Flask, jsonify, request
# Intitialise the app
app = Flask(__name__)
# Define what the app does
@app.route("/greeting")
def index():
    
    name = request.args.get("name")
    if not name:
        return jsonify({status}:{error})
    
    response = {"data":f"Hello {name}!"}
    return jsonify(response)

