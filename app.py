from flask import Flask, jsonify, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# In-memory student list
students = [
    {"name": "Joynase", "grade": 10, "section": "Zechariah"}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Students API! 🌟",
        "emoji": "🚀📚😊"
    })

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form.get('name')
        grade = request.form.get('grade')
        section = request.form.get('section')
        if name and grade and section:
            students.append({
                "name": name,
                "grade": grade,
                "section": section
            })
        return redirect(url_for('dashboard'))
    return render_template('dashboard.html', students=students)

# Bind to Render's dynamic port
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

