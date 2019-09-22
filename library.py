class Library:
    def __init__(self):
        self.books_list = []
        self.inventory = {}
    def add_book_to_library(self, book):
        self.books_list.append(book)
    def take_book_from_library(self, book, reader_name, reader_type):
        #self.books_list.remove(book)
        try:
            self.books_list.remove(book)
        except Exception as e:
            print(e)
            print ('Can\'t delete book, it isn\'t in list')
        if str(self.inventory.get(reader_name)) == 'None':
            print ('reader_name is None ' + reader_name)
            print (self.inventory)
            self.inventory[reader_name] = [book]
        else:
            if len(self.inventory[reader_name]) < 3 or reader_type == 'teacher':
                print ('reader_name is exist ' + reader_name)
                print (self.inventory)
                print (self.inventory.get(reader_name))
                self.inventory[reader_name].append(book)
                print (self.inventory)
                print len(self.inventory[reader_name])
            else:
                print ('Can\'t give book to '+reader_name+'. Max limit reached')

    def return_book_to_library(self, book, reader_name):
        self.books_list.append(book)
        #self.inventory.remove(book, reader_name)

    def show_books_list(self):
        print self.books_list
        return self.books_list
    def show_inventory(self):
        print self.inventory
        return self.inventory