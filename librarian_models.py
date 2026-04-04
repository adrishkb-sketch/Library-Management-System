import json

#viewing a student details
def view_student(students_list, books_list, std_index):
    print(f"Name: {students_list[std_index]['name']}")
    print(f"Roll Number: {students_list[std_index]['roll']}")
    print(f"Department: {students_list[std_index]['department']}")
    print(f"Year: {students_list[std_index]['year']}")
    print("Issued Books:")
    for i in range(len(students_list[std_index]["books_issued"])):
        book_code = students_list[std_index]["books_issued"][i]
        for y in books_list:
            if y["code"] == book_code:
                print(f"{y['name']} (Code: {book_code})")
                print(f"Issue Date: {students_list[std_index]['issue_date'][i]}")
                print(f"Scheduled Return: {students_list[std_index]['scheduled_return_date'][i]}")
                if i < len(students_list[std_index]["return_date"]):
                    print(f"Actual Return: {students_list[std_index]['return_date'][i]}")
                else:
                    print("Actual Return: Not Returned")
                print("-" * 30)
                break
    print("Requested Books:")
    for i in students_list[std_index]["books_requested"]:
        book_code=i
        for y in range(len(books_list)):
            if books_list[y]["code"] == book_code:
                print(f"{books_list[y]["name"]}\n")
    print("Late Returned Books:")
    for i in students_list[std_index]["late_returned_books"]:
        book_code=i
        for y in range(len(books_list)):
            if books_list[y]["code"] == book_code:
                print(f"{books_list[y]["name"]}\n")
    print("Damaged Books: ")
    for i in students_list[std_index]["damaged_books"]:
        book_code=i
        for y in range(len(books_list)):
            if books_list[y]["code"] == book_code:
                print(f"{books_list[y]["name"]}\n")
    print(f"Total Fine: {students_list[std_index]['fine']}")
    print(f"Fine Cleared: {students_list[std_index]['fine_cleared']}")
    print(f"Books with student: {students_list[std_index]['books_with_user']}")


# test change
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
    with open("book_data.json", "r") as f:
        book_data = json.load(f)
    view_student(students_list,book_data,len(students_list)-1)

#removing a student
def remove_student(students_list):
    find_by=input("Find by Name(N) or Roll Number(R): ")
    if find_by == "N":
        name=input("Enter Student Name: ")
        for i in range(len(students_list)):
            if students_list[i]["name"] == name:
                remove_number=i
                with open("book_data.json", "r") as f:
                    book_data = json.load(f)
                view_student(students_list,book_data,i)
                confirmation=input("Do you want to remove the book from the list? (Y/N): ")
                if confirmation == "Y":
                    students_list.pop(remove_number)
                else:
                    break
                break
    elif find_by == "R":
        roll=input("Enter Student Roll Number: ")
        for i in range(len(students_list)):
            if students_list[i]["roll"] == roll:
                remove_number=i
                with open("book_data.json", "r") as f:
                    book_data = json.load(f)
                view_student(students_list,book_data,i)
                confirmation = input("Do you want to remove the book from the list? (Y/N): ")
                if confirmation == "Y":
                    students_list.pop(remove_number)
                else:
                    break
                break
    with open("student_data.json", "w") as f:
        json.dump(students_list, f, indent=4)

#editing an existing student
def edit_student(students_list):
    roll=input("Enter Student Roll Number: ")
    for i in range(len(students_list)):
        if students_list[i]["roll"] == roll:
            student_number=i
            with open("book_data.json", "r") as f:
                book_data = json.load(f)
            view_student(students_list, book_data, i)
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