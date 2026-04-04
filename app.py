from librarian_models import remove_student
import json
with open("database/student_data.json", "r") as f:
    students = json.load(f)
remove_student(students)