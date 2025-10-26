from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    return jsonify({
        "name": "Your Name",
        "grade": 10,
        "section": "Zechariah"
    })

# Required for Render to bind to the correct port
import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
