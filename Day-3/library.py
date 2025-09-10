# You are building a Library Management System in Python. The system should store books in a dictionary where:
# Key → Book ID
# Value → Book Title
# Write a Python program to perform the following operations using Dictionaries:
# Add a book to the library (Book ID, Title).
# Remove a book using Book ID.
# Search for a book by Book ID and display the title.
# Update the title of a book (e.g., correction in title).
# Display all books in the library.
# Count the total number of books in the library.
# Check if a book title exists in the library (reverse lookup).
def lib():
    d = {1: "Dhawan", 2: "Dhoni", 3: "Rohit"}
    while True:
        print("\nLibrary Operations:")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book by ID")
        print("4. Update Book Title")
        print("5. Display All Books")
        print("6. Count Total Books")
        print("7. Check if Title Exists")
        print("8. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            k = int(input("Enter Book ID: "))
            v = input("Enter Book Title: ")
            d[k] = v
            print(f"Book '{v}' added successfully.")
        elif ch == 2:
            r = int(input("Enter Book ID to remove: "))
            if r in d:
                removed = d.pop(r)
                print(f"Book '{removed}' removed successfully.")
            else:
                print("Book ID not found.")
        elif ch == 3:
            s = int(input("Enter Book ID to search: "))
            if s in d:
                print(f"Book found: {d[s]}")
            else:
                print("Book ID not found.")
        elif ch == 4:
            k = int(input("Enter Book ID to update: "))
            if k in d:
                v = input("Enter new Book Title: ")
                d[k] = v
                print("Book updated successfully.")
            else:
                print("Book ID not found.")
        elif ch == 5:
            if d:
                print("Books in Library:")
                for bid, title in d.items():
                    print(f"{bid}: {title}")
            else:
                print("Library is empty.")
        elif ch == 6:
            print("Total number of books:", len(d))
        elif ch == 7:
            title = input("Enter Book Title to check: ")
            if title in d.values():
                print(f"Yes, '{title}' exists in the library.")
            else:
                print(f"No, '{title}' not found.")
        elif ch == 8:
            print("Thank you!")
            break
        else:
            print("Invalid choice! Please try again.")
lib()

        