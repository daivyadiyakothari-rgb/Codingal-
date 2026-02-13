# Activity 1 
class fruit:
    # Constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

# Object Creation
apple = fruit ('Apple', 'Red')

# Calling Function 
print(apple.name)
print(apple.color)

# Activity 2
class Employee:
    def __init__(self): 
        print("Emoployee created")
    print("Employee deleted")
obj = Employee()
del obj 

# Activity 3
# Activity-2
# Library Management System using OOP, Loops, and Conditionals

class Library:
    def __init__(self, name):
        self.name = name
        self.books = ["Harry Potter", "Rich Dad Poor Dad", "Atomic Habits", "Python Basics"]
        self.lend_data = {}  # To track which user has borrowed which book

    def display_books(self):
        print("\n📚 Available Books in the Library:")
        for book in self.books:
            print(f" - {book}")

    def lend_book(self, user, book):
        if book not in self.books:
            print(f"❌ The book '{book}' is not available in the library.")
        elif book in self.lend_data:
            print(f"⚠️ Sorry, '{book}' is currently lent out to {self.lend_data[book]}.")
        else:
            self.lend_data[book] = user
            print(f"✅ Book '{book}' has been lent to {user}.")

    def add_book(self, book):
        if book in self.books:
            print("⚠️ This book already exists in the library.")
        else:
            self.books.append(book)
            print(f"✅ Book '{book}' has been added to the library.")

    def return_book(self, book):
        if book in self.lend_data:
            del self.lend_data[book]
            print(f"✅ Book '{book}' has been returned successfully.")
        else:
            print(f"⚠️ '{book}' was not lent out from this library.")


# --- Main Program ---
if __name__ == "__main__":
    my_library = Library("City Central Library")

    while True:
        print("\n========== Library Menu ==========")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        print("5. Exit")
        print("===================================")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            my_library.display_books()

        elif choice == '2':
            user = input("Enter your name: ")
            book = input("Enter the book name you want to borrow: ")
            my_library.lend_book(user, book)

        elif choice == '3':
            book = input("Enter the name of the book to add: ")
            my_library.add_book(book)

        elif choice == '4':
            book = input("Enter the name of the book to return: ")
            my_library.return_book(book)

        elif choice == '5':
            print("\n📘 Thank you for using the Library Management System!")
            break

        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

        