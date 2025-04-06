from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from prompt_engine import convert_to_spec  # Make sure prompt_engine.py exists in the same folder

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Make sure templates/index.html exists

@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    requirement = data.get("requirement", "")
    
    if not requirement:
        return jsonify({"error": "No input provided"}), 400

    try:
        result = convert_to_spec(requirement)
        return jsonify({"output": result.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
