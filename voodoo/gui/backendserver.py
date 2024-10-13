from flask import Flask, request, jsonify
from flask_cors import CORS
from backend import process_data, another_function  # backend.py'den fonksiyonları içe aktarıyoruz

app = Flask(__name__)
CORS(app)

# Dinamik fonksiyon çağrısını desteklemek için
FUNCTION_MAP = {
    'process_data': lambda state: process_data(state),
    'another_function': lambda state: another_function(state),
}

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.get_json()
    function_name = data.get("function")
    state = data.get("state")
    
    if function_name in FUNCTION_MAP:
        # Dinamik olarak fonksiyonu çağırıyoruz
        FUNCTION_MAP[function_name](state)
        return jsonify({"status": "success", "message": f"{function_name} executed"}), 200
    else:
        return jsonify({"status": "error", "message": f"Function {function_name} not found"}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)
