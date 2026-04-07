#Searching a book
def library_search(book_data):
    while True:
        field = input("\nSearch by (name/author/code/department/year/subject) or 'exit': ")
        if field == "exit":
            break
        if field not in book_data[0]:
            print(" Invalid field!")
            continue
        value = input("Enter value: ")
        results = [book for book in book_data if value in str(book[field])]
        if results:
            for book in results:
                print("\n Book Found:")
                for key, val in book.items():
                    print(f"{key.capitalize():12}: {val}")
                print("-" * 25)
        else:
            print(" No matching book found.")
