from book import Book

book1 = Book("Python Basics", "John Doe")
book2 = Book("AI Intro", "Jane Smith", False)

print(book1.title, book1.author, book1.available)
print(book2.title, book2.author, book2.available)

# Class + Static methods testing 
print("\nClass and Static Methods:")

print(Book.library_name)

Book.change_library_name("City Library")
print(Book.library_name)

print(Book.is_valid_title("Python"))
print(Book.is_valid_title(""))


