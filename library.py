class Library:
    def __init__(self):
        self.books_list = []
    def add_book_to_library(self, book):
        self.books_list.append(book)
    def take_book_from_library(self, book):
        self.books_list.remove(book)
    def show_books_list(self):
        print self.books_list
        return self.books_list