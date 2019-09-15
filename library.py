class Library:
    def __init__(self):
        self.books_list = []
        self.inventory = []
    def add_book_to_library(self, book):
        self.books_list.append(book)
    def take_book_from_library(self, book, reader_name):
        self.books_list.remove(book)
        self.inventory.append((book, reader_name))
    def return_book_to_library(self, book, reader_name):
        self.books_list.append(book)
        self.inventory.remove(book, reader_name)
    def show_books_list(self):
        print self.books_list
        return self.books_list
    def show_invenyory(self):
        print self.inventory
        return self.inventory