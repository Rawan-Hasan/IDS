from flask import Flask, request, jsonify
from flask_cors import CORS
from auth import authenticate, token_required, generate_token
from model_utils import load_model_and_features, preprocess_input

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'your-secret-key'

model, selected_features = load_model_and_features('rf')

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if authenticate(data.get("username"), data.get("password")):
        token = generate_token(data["username"])
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/predict", methods=["POST"])
@token_required
def predict(current_user):
    try:
        input_data = request.get_json()["features"]
        X = preprocess_input(input_data, selected_features)
        prediction = model.predict(X)
        return jsonify({"prediction": int(prediction[0])}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
