class Student:
    def __init__(self, name, books_got=0):
        self.name = name
        self.books_got = books_got
    def return_book_to_library(self, library, book):
        library.add_book_to_library(book)
    def return_book_to_teacher(self):
        return 0
    def take_book_from_library(self, library, book):
        if self.books_got >= 10:
            return 'max books got'
        library.take_book_from_library(book)
        self.books_got += 1
    def add_book_to_library(self, library, book):
        library.add_book_to_library(book)