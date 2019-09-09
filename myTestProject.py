# coding: utf8
import random

class Student():
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
    def add_book_to_library(self, book):
        Library.add_book_to_library(book)

class Library():
    def __init__(self):
        self.books_list = []
    def add_book_to_library(self, book):
        self.books_list.append(book)
    def take_book_from_library(self, book):
        self.books_list.remove(book)
    def show_books_list(self):
        print self.books_list
        return self.books_list

class Book():
    def __init__(self, name, author):
        self.name = name
        self.author = author



#books_list = ['pytnonBook1', 'pytnonBook2', 'pytnonBook3', 'pytnonBook4', 'pytnonBook5', 'pytnonBook6', 'pytnonBook7',
#              'pytnonBook7', 'pytnonBook8', 'pytnonBook9', 'pytnonBook10', 'pytnonBook11']

library = Library()
student = Student('Arthur')
library.show_books_list()

book1 = Book('author1', 'pytnonBook1')
library.add_book_to_library(book1)
library.show_books_list()
student.take_book_from_library(library, book1)
#student.take_book_from_library(library, book)
#library.take_book_from_library('pytnonBook7')
library.show_books_list()
