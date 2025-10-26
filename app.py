from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)

# Temporary in-memory list to store students
students = [
    {"name": "Your Name", "grade": 10, "section": "Zechariah"}
]

# 🌐 API Routes
@app.route('/')
def home():
    return "Welcome to my Flask API!"

@app.route('/student')
def get_student():
    return jsonify(students[0])  # Returns the first student for demo

# 🎓 Dashboard Route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        grade = request.form['grade']
        section = request.form['section']

        # Add new student to list
        students.append({
            "name": name,
            "grade": grade,
            "section": section
        })

        return redirect('/dashboard')

    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
