class Teacher:
    def __init__(self, name, books_got=0, reader_type='teacher'):
        self.name = name
        self.books_got = books_got
        self.reader_type = reader_type
    def return_book_to_library(self, library, book):
        library.add_book_to_library(book)
    def take_book_from_library(self, library, book):
        library.take_book_from_library(book)
        self.books_got += 1
    def add_book_to_library(self, library, book):
        library.add_book_to_library(book)
