books = [
    {"name": "ABCD", "author": "MNB", "code": 1032, "department": "CSE", "year": "1st", "subject": "Math",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "ABUD", "author": "PKC", "code": 1033, "department": "ECE", "year": "2nd", "subject": "Physics",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "AOCD", "author": "MKC", "code": 1034, "department": "CSE", "year": "3rd", "subject": "DSA",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "ASCD", "author": "MNK", "code": 1035, "department": "ME", "year": "1st", "subject": "Mechanics",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "ABND", "author": "ASN", "code": 1036, "department": "CE", "year": "2nd", "subject": "Structure",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "ABCP", "author": "ASM", "code": 1037, "department": "CSE", "year": "4th", "subject": "AI",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},

    {"name": "FBCD", "author": "MRT", "code": 1038, "department": "ECE", "year": "3rd", "subject": "Signals",
     "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]}
]

def print_book(book):
    print("\n Book Found:")
    print(f"Name       : {book['name']}")
    print(f"Author     : {book['author']}")
    print(f"Code       : {book['code']}")
    print(f"Department : {book['department']}")
    print(f"Year       : {book['year']}")
    print(f"Subject    : {book['subject']}")
    print(f"Copies     : {book['no_of_copies']}")
    print("-" * 30)


def search_books(field, value):
    found = False

    for book in books:
        if field in book:
            if str(value).lower() in str(book[field]).lower():
                print_book(book)
                found = True

    if not found:
        print("\n No matching book found.")


if __name__ == "__main__":
    while True:
        print("\n Search Options: name, author, code, department, year, subject")
        field = input("Enter what you want to search by (or 'exit'): ").lower()

        if field == "exit":
            print("Exiting program...")
            break

        value = input("Enter search value: ")

        search_books(field, value)