# 📚 Book Database
books = [
    {"name": "ABCD", "author": "MNB", "code": 1032, "department": "CSE", "year": "1st", "subject": "Math", "no_of_copies": 5},
    {"name": "ABUD", "author": "PKC", "code": 1033, "department": "ECE", "year": "2nd", "subject": "Physics", "no_of_copies": 5},
    {"name": "AOCD", "author": "MKC", "code": 1034, "department": "CSE", "year": "3rd", "subject": "DSA", "no_of_copies": 5},
    {"name": "ASCD", "author": "MNK", "code": 1035, "department": "ME", "year": "1st", "subject": "Mechanics", "no_of_copies": 5},
    {"name": "ABND", "author": "ASN", "code": 1036, "department": "CE", "year": "2nd", "subject": "Structure", "no_of_copies": 5},
    {"name": "ABCP", "author": "ASM", "code": 1037, "department": "CSE", "year": "4th", "subject": "AI", "no_of_copies": 5},
    {"name": "FBCD", "author": "MRT", "code": 1038, "department": "ECE", "year": "3rd", "subject": "Signals", "no_of_copies": 5}
]

# 🔍 Simple Function
def library_search():
    while True:
        field = input("\nSearch by (name/author/code/department/year/subject) or 'exit': ")

        if field == "exit":
            break

        if field not in books[0]:
            print(" Invalid field!")
            continue

        value = input("Enter value: ")

        results = [book for book in books if value in str(book[field])]

        if results:
            for book in results:
                print("\n Book Found:")
                for key, val in book.items():
                    print(f"{key.capitalize():12}: {val}")
                print("-" * 25)
        else:
            print(" No matching book found.")


library_search()