# coding: utf8
import random
'''
import random

class Warrior():

    def __init__(self, name='default Name', hp=100, loss=0):
        self.name = name
        self.hp = hp
        self.loss = loss

    def sethp(self, changeValue):
        self.hp = self.hp + changeValue
        if self.hp <= 0:
            self.loss = 1
            print(self.name + ' loss')
        else:
            return self.hp

    def gethp(self):
        return self.hp

firstWarrior = Warrior('first warrior')
# firstWarrior.name = 'first warrior'
secondWarrior = Warrior('second warrior')
# secondWarrior.name = 'second warrior'
# secondWarrior = Warrior()

while firstWarrior.loss == 0 and secondWarrior.loss == 0:
    random_damage = random.randint(1, 10)
    firstWarrior.sethp(-random_damage)
    print(firstWarrior.gethp())
    random_damage = random.randint(1, 10)
    secondWarrior.sethp(-random_damage)
    print(secondWarrior.gethp())
'''


'''
class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s



p1 = Person("Bill", "Ross")

print (p1.name, p1.surname)
'''
'''
class Person():
    def __init__(self, name, surname, exp=1):
        self.name = name
        self.surname = surname
        self.exp = exp
    def getInfo(self):
        return self.name + ' ' + self.surname + ' ' + str(self.exp)
    def __del__(self):
        return 'До свидания, мистер ' + self.surname

firstPerson = Person('Thomas', 'Anderson')
print (firstPerson.getInfo())
firstPerson.__del__()
print (firstPerson.getInfo())
'''

'''
class Table():
    def __init__(self, l, w, h):
        self.lenght = l
        self.width = w
        self.height = h
class KitchenTable(Table):
    def setpPaces(self, p):
        self.places = p
class DeskTable(Table):
    def square(self):
        self.square = self.lenght * self.width
class ComputerTable(DeskTable):
    def square(self, e):
        self.square = self.lenght * self.width - e
class SpecialKitchenTable(Table):
    def __init__(self, l, w, h, p):
        Table.__init__(self, l, w, h)
        self.places = p

t1 = KitchenTable(5, 10, 20)
t2 = SpecialKitchenTable(10, 5, 20, 6)
print (t2.places)

'''


'''
class Hero():
    def __init__(self, number, team, level=0):
        self.number = number
        self.team = team
        self.level = level
        self.team_list = []
    def level_up(self):
        self.level = self.level+1
    def add_soldier_to_team(self, unit):
        self.team_list.append(unit)


class Soldier():
    def __init__(self, number, team, level=0):
        self.number = number
        self.team = team
    def follow_hero(self, hero):
        self.hero_to_follow = hero
    def __str__(self):
        return str(self.number) + ' ' + self.team

counter = 1

team = ['red', 'blue']
hero1 = Hero(counter, 'red')
counter += 1
hero2 = Hero(counter, 'blue')
counter += 1

for i in range(1, 101):
    current_team = random.choice(team)
    soldier = Soldier(counter, current_team)
    if random.choice(team) == 'red':
        hero1.add_soldier_to_team(soldier)
    else:
        hero2.add_soldier_to_team(soldier)
    counter += 1

print (len(hero1.team_list))
print (len(hero2.team_list))

if len(hero1.team_list) > len(hero2.team_list):
    hero1.level_up()
elif len(hero2.team_list) > len(hero1.team_list):
    hero2.level_up()

hero1.team_list[0].follow_hero(hero1)
print(hero1.team_list[0])
'''


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
