from flask import Flask, request, jsonify
from flask_cors import CORS
import importlib

app = Flask(__name__)
CORS(app)

# Dinamik olarak modülden fonksiyon çağırmak için
def dynamic_import_function(function_name):
    # application/backend.py modülünden fonksiyonu dinamik olarak import ediyoruz
    module_name = 'application.backend'
    module = importlib.import_module(module_name)
    function_ = getattr(module, function_name)
    return function_

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.get_json()
    function_name = data.get("function")
    state = data.get("state")
    
    try:
        # Dinamik fonksiyon çağrımı
        function_to_call = dynamic_import_function(function_name)
        function_to_call(state)
        return jsonify({"status": "success", "message": f"{function_name} executed"}), 200
    except AttributeError:
        return jsonify({"status": "error", "message": f"Function {function_name} not found"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)
