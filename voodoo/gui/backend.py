from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Backend fonksiyonlarını burada dinamik olarak çalıştıracağız
@app.route("/run_function", methods=["POST"])
def run_function():
    data = request.json
    function_name = data.get("function_name")
    state = data.get("state")

    try:
        # eval() ile gelen fonksiyon adını string olarak çalıştırıyoruz
        # Öncelikle güvenlik açısından kontrol sağlamak iyi olabilir
        result = eval(f"{function_name}(state)")  # Dinamik fonksiyon çalıştırma
    except Exception as e:
        result = {"error": f"Fonksiyon çalıştırılırken hata oluştu: {str(e)}"}

    return jsonify(result)

# Python fonksiyonları
def process_data(state):
    print(f"Process Data State: {state}")
    return {"message": "process_data çalıştı", "state": state}

def another_function(state):
    print(f"Another Function State: {state}")
    return {"message": "another_function çalıştı", "state": state}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
