import book
import student as st
import library
import teacher




library = library.Library()
student = st.Student('Arthur')
student2 = st.Student('Bim')
teacher = teacher.Teacher('Grand')
#teacher2 = teacher.Teacher('Master')
library.show_books_list()

book1 = book.Book('author1', 'pytnonBook1')
book2 = book.Book('author1', 'pytnonBook2')
book3 = book.Book('author1', 'pytnonBook3')
book4 = book.Book('author1', 'pytnonBook4')
book5 = book.Book('author1', 'pytnonBook5')
book6 = book.Book('author1', 'pytnonBook6')
book7 = book.Book('author1', 'pytnonBook7')
book8 = book.Book('author1', 'pytnonBook8')
book9 = book.Book('author1', 'pytnonBook9')
book10 = book.Book('author1', 'pytnonBook10')


library.add_book_to_library(book1)
library.add_book_to_library(book2)
library.add_book_to_library(book3)
library.add_book_to_library(book4)
library.add_book_to_library(book5)
library.add_book_to_library(book6)
library.add_book_to_library(book7)
library.add_book_to_library(book8)
library.add_book_to_library(book9)
library.add_book_to_library(book10)






library.show_books_list()
#student.take_book_from_library(library, book1)
#student.take_book_from_library(library, book2)
#student.take_book_from_library(library, book3)
#student.take_book_from_library(library, book4)
#library.take_book_from_library('pytnonBook7')
library.show_books_list()


library.take_book_from_library(book7, student.name, student.reader_type)
library.take_book_from_library(book6, student.name, student.reader_type)
library.take_book_from_library(book5, student.name, student.reader_type)
library.take_book_from_library(book4, student.name, student.reader_type)

#library.take_book_from_library(book5, student.name)

#print (library.inventory.get('Arthur'))

