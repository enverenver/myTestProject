import book
import student
import library
import teacher





library = library.Library()
student = student.Student('Arthur')
library.show_books_list()

book1 = book.Book('author1', 'pytnonBook1')
library.add_book_to_library(book1)
library.show_books_list()
student.take_book_from_library(library, book1)
#student.take_book_from_library(library, book)
#library.take_book_from_library('pytnonBook7')
library.show_books_list()
