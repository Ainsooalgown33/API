from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['GET'])
def get_info():
    # Replace with your registered email and GitHub URL
    response = {
        "email": "dunsieman@gmail.com",
        "current_datetime": datetime.utcnow().isoformat() + "Z",
        "github_url": "https://github.com/Ainsooalgown33?tab=repositories"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)