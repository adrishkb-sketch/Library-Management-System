books = [
    {"name": "ABCD", "author": "MNB", "code": 1032, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "ABUD", "author": "PKC", "code": 1033, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "AOCD", "author": "MKC", "code": 1034, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "ASCD", "author": "MNK", "code": 1035, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "ABND", "author": "ASN", "code": 1036, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "ABCP", "author": "ASM", "code": 1037, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]},
    {"name": "FBCD", "author": "MRT", "code": 1038, "no_of_copies": 5, "book_numbers": [], "edition": [], "condition": ["Good", "Bad", "Okay", "Terrible"]}
]
def search_by_name(book_name):
    found = False
    for book in books:
        if book_name.lower() in book["name"].lower():
            print("\nBook Found:")
            print_book(book)
            found = True
    if not found:
        print("No book found with that name.")
def search_by_author(author_name):
    found = False
    for book in books:
        if author_name.lower() in book["author"].lower():
            print("\nBook Found:")
            print_book(book)
            found = True
    if not found:
        print("No book found by that author.")
def print_book(book):
    print(f"Name: {book['name']}")
    print(f"Author: {book['author']}")
    print(f"Code: {book['code']}")
    print(f"Copies: {book['no_of_copies']}")
    print("-" * 20)
    
if __name__ == "__main__":
    while True:
        print("\n1. Search by Book Name")
        print("2. Search by Author")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter book name: ")
            search_by_name(name)

        elif choice == "2":
            author = input("Enter author name: ")
            search_by_author(author)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

print("There is nobody as beautiful a soul as Nidhi 🫠")