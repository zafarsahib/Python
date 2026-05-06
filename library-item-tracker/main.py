from book import Book

book1 = Book("Python Basics", "John Doe")
book2 = Book("Urdu Poetry", "Iqbal Lahori", False)

print(book1.title, book1.author, book1.available)
print(book2.title, book2.author, book2.available)

print("\nTesting Methods for book1 and book2")

# Testing methods on book1
book1.display_info()
book1.borrow()
book1.display_info()
book1.return_book()
book1.display_info()

print("\nTesting book2 methods")
book2.display_info()
book2.borrow()   # should say not available