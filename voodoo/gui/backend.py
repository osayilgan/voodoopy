from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS enabled

@app.route('/run_function', methods=['POST'])
def run_function():
    data = request.json
    function_name = data.get('function_name')
    state = data.get('state')

    # Gelen fonksiyon adını dinamik olarak çağırma
    if function_name == 'process_data':
        result = process_data(state)
    elif function_name == 'another_function':
        result = another_function(state)
    else:
        result = {"error": "Fonksiyon bulunamadı"}

    return jsonify(result)

# Python fonksiyonları
def process_data(state):
    print(f"Process Data State: {state}")
    return {"message": "process_data çalıştı", "state": state}

def another_function(state):
    print(f"Another Function State: {state}")
    return {"message": "another_function çalıştı", "state": state}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3001, debug=True)

