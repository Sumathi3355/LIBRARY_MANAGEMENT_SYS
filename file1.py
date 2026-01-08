books = []

def add_book(name):
    books.append(name)
    print("Book added")

def view_books():
    if not books:
        print("No books available")
    else:
        for b in books:
            print(b)

add_book("Python Basics")
add_book("Data Structures")

view_books()
