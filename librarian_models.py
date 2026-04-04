import json

#viewing a student details
def view_student(students_list,books_list,std_index,book_index):
    print(f"Name: {students_list[std_index]["name"]}")
    print(f"Roll Number: {students_list[std_index]["roll"]}")
    print(f"Department: {students_list[std_index]["department"]}")
    print(f"Year: {students_list[std_index]["year"]}")
    print("Issued Books:")
    for x in students_list[std_index]["books_issued"]:
        for y in books_list:
            print(books_list[y]["code"])



#adding a new student
def add_student(students_list):
    name=input("Enter Student Name: ")
    year=input("Enter Year: ")
    department=input("Enter Department: ")
    roll=input("Enter Roll: ")
    passwd=input("Enter Password: ")
    new_student={"name": name, "year": year, "department": department, "roll": roll,"pass": passwd,
                 "books_issued": [],
                 "issue_date": [],
                 "scheduled_return_date": [],
                 "return_status": [],
                 "return_date": [],
                 "requested_books": [],
                 "late_returned_books": [],
                 "damaged_books": [],
                 "fine": 0,
                 "fine_cleared": 0,
                 "books_with_user": 0
                 }
    students_list.append(new_student)
    with open("student_data.json", "w") as f:
        json.dump(students_list, f, indent=4)

#removing a student
def remove_student(students_list):
    find_by=input("Find by Name(N) or Roll Number(R): ")
    if find_by == "N":
        name=input("Enter Student Name: ")
        for i in range(len(students_list)):
            if students_list[i]["name"] == name:
                remove_number=i
                students_list.pop(remove_number)
                break
    elif find_by == "R":
        roll=input("Enter Student Roll Number: ")
        for i in range(len(students_list)):
            if students_list[i]["roll"] == roll:
                remove_number=i
                students_list.pop(remove_number)
                break
    with open("student_data.json", "w") as f:
        json.dump(students_list, f, indent=4)

#editing an existing student
def edit_student(students_list):
    roll=input("Enter Student Roll Number: ")
    for i in range(len(students_list)):
        if students_list[i]["roll"] == roll:
            student_number=i
            edit=input("Edit Name(N), Edit Year(Y), Edit Password(P), Edit Department(D):  ")
            if edit=="N":
                new_name=input("Enter New Name: ")
                students_list[student_number]["name"]=new_name
                break
            elif edit=="Y":
                new_year=input("Enter New Year: ")
                students_list[student_number]["year"]=new_year
                break
            elif edit=="P":
                new_pass=input("Enter New Password: ")
                students_list[student_number]["pass"]=new_pass
                break
            elif edit=="D":
                new_department=input("Enter New Department: ")
                students_list[student_number]["department"]=new_department
                break
    with open("student_data.json", "w") as f:
            json.dump(students_list, f, indent=4)