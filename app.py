from librarian_models import add_student, remove_student, edit_student
import json
with open("student_data.json","r") as f:
    students = json.load(f)
remove_student(students)