class Student:
    def __init__(self, name, books_got=0, reader_type='student'):
        self.name = name
        self.books_got = books_got
        self.reader_type = reader_type
    def return_book_to_library(self, library, book):
        library.return_book_to_library(book, self.name)
    def return_book_to_teacher(self):
        return 0
    def take_book_from_library(self, library, book):
        if self.books_got >= 3:
            print('max books got')
            return 'max books got'
        library.take_book_from_library(book, self.name)
        self.books_got += 1
    def add_book_to_library(self, library, book):
        library.add_book_to_library(book)