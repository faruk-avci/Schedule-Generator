from flask import Flask, request, jsonify, render_template, session
import sqlite3
import traceback
from generate_schedules import generate_schedules_m
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)  # Replace with a fixed secret key in production

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json.get('data', '')

    data = '%' + data.upper() + '%'
    print(data)

    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT course_name FROM courses WHERE course_name LIKE ?
    ''', (data,))

    result = cursor.fetchall()

    unique_results = set(result)
    conn.close()
    print(result)
    if result:
        return jsonify(list(unique_results))
    else:
        return jsonify({})

@app.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    try:
        data = request.json
        courses = data.get('courses', [])
        if not courses:
            return jsonify({"error": "No courses provided"}), 400

        schedules = generate_schedules_m(courses)
        session['schedules'] = schedules  # Store schedules in session
        return jsonify({"message": "Schedules generated successfully"})
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/get_schedules', methods=['GET'])
def get_schedules():
    try:
        schedules = session.get('schedules', [])
        return jsonify(schedules)
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/schedules')
def schedules_page():
    return render_template('schedules.html')

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5000, debug=True)
