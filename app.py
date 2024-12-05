from flask import Flask, jsonify, request
from flask import Flask, request, jsonify

# Inicializar o app
app = Flask(__name__)

# Definir o comportamento do app
@app.route("/greet", methods=["GET"])
def index():
    """
    1. Capturar primeiro nome e último nome dos parâmetros da URL.
    2. Se qualquer um não for fornecido: responder com um erro.
    3. Se o primeiro nome não for fornecido e o segundo for, responder com "Hello Mr <second-name>!".
    4. Se o primeiro nome for fornecido e o segundo nome não for, responder com "Hello, <first-name>!".
    5. Se ambos os nomes forem fornecidos, responder com "Is your name <first-name> <second-name>?"
    """
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    if not first_name and not last_name:
        return jsonify({"error": "First name and last name are required"}), 400
    elif not first_name:
        return f"Hello Mr. {last_name}!", 200
    elif not last_name:
        return f"Hello, {first_name}!", 200
    else:
        return f"Is your name {first_name} {last_name}?", 200

# Rodar o servidor
if __name__ == "__main__":
    app.run(port=5000)
