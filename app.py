from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

# Temporary in-memory list to store students
students = [
    {"name": "Joynase", "grade": 3, "section": "Stallman"}
]

# 🌐 API Routes
@app.route('/')
def home():
    return "Welcome to Joynase Flask API!"

@app.route('/student')
def get_student():
    return jsonify(students[0])  # Returns the first student for demo

# 🎓 Dashboard Route
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form['name']
        grade = request.form['grade']
        section = request.form['section']
        students.append({
            "name": name,
            "grade": int(grade),
            "section": section
        })
        return redirect(url_for('dashboard', show_view='true'))

    show_view = request.args.get('show_view') == 'true'
    return render_template('index.html', students=students, show_view=show_view)

# 🖊️ Update student by ID
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    if id < 0 or id >= len(students):
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()
    students[id]['name'] = data['name']
    students[id]['grade'] = int(data['grade'])
    students[id]['section'] = data['section']
    return jsonify({"message": "Student updated successfully"})

# 🗑️ Delete student by ID
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if id < 0 or id >= len(students):
        return jsonify({"error": "Student not found"}), 404

    students.pop(id)
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

