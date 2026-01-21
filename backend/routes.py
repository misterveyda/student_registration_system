from flask import request, jsonify
from models import students

def register_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student registered successfully"})
