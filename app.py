from flask import Flask, jsonify, request, render_template, redirect, url_for

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

        # ✅ Redirect with query parameter to show student list
        return redirect(url_for('dashboard', show_view='true'))

    # ✅ Check if we should auto-show the student list
    show_view = request.args.get('show_view') == 'true'

    return render_template('index.html', students=students, show_view=show_view)

if __name__ == '__main__':
    app.run(debug=True)
