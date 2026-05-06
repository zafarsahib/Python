class Book:
    library_name = "Central Library"

    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title}  bookborrowed.")
        else:
            print(f"{self.title} book is not available.")

    def return_book(self):
        self.available = True
        print(f"{self.title} book returned.")

    def display_info(self):
        status = "Available" if self.available else "book Not Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")      

    @classmethod
    def change_library_name(cls, new_name):
        cls.library_name = new_name

    @staticmethod
    def is_valid_title(title):
        return len(title.strip()) > 0
    
