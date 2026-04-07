import json

def library_system():
    file_name = "book_data.json"

    with open(file_name, "r") as f:
        books = json.load(f)

    while True:
        field = input("\nSearch by (name/author/code) or 'exit': ")

        if field == "exit":
            break

        if books and field not in books[0]:
            print("Invalid field!")
            continue

        value = input("Enter value: ")

        results = [b for b in books if value in str(b.get(field, ""))]

        if results:
            for b in results:
                print("\nBook Found:")
                print("Name:", b.get("name"))
                print("Author:", b.get("author"))
                print("Code:", b.get("code"))

            if input("Request this book? (yes/no): ").lower() == "yes":
                name = input("Enter your name: ")

                for b in results:
                    b.setdefault("requests", []).append(name)

                with open(file_name, "w") as f:
                    json.dump(books, f, indent=4)

                print("Request added!")

        else:
            print("No book found.")

library_system()