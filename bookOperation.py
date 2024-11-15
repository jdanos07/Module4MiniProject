import re

class Book_Operations:
    def __init__(self, id_code, title, author, genre, publication_date, available=True):
        self.__id_code = id_code
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__publication_date = publication_date
        self.__available = available
    
    def get_id(self):
        return self.__id_code
    
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def get_available(self):
        return self.__available 
    
    def set_available(self, available):
        self.__available = available

    def display(self):
        availability = 'Available' if self.__available else "Checked Out"
        print(f'{self.__id_code}: {self.__title}, {self.__author}, {self.__genre}, {self.__publication_date}, {availability}')



library = {}

def new_book(library):
    id_code = f'{len(library) + 1:03d}'
    title = input('Title: ')
    author = input('Author: ')
    genre = input('Genre: ')
    while True:
        publication_date = input('Publication Date (mm/yyyy): ')
        if date_format(publication_date):
            break
        else: 
            print('Invalid format. Use mm/yyyy formatting.')
    available = True
    library[id_code] = Book_Operations(id_code, title, author, genre, publication_date, available)    

def date_format(publication_date):
    format = r'^\d{1,2}/\d{4}$'
    return bool(re.match(format, publication_date))
       
def display_library():
    for book in library.values():
        book.display()
        
def search_books():
    how_to_find = input('Search books by ID, Title, or Author: ').lower()
    if how_to_find == 'id':
        id_search = input('Input ID: ')
        if id_search in library:
            library[id_search].display()
        else:
            print('A book with this ID does not exist.\nPlease try again.')
    elif how_to_find == 'title':
        title_search = input('Input Title: ').lower()
        for book in library.values():
            if book.get_title().lower() == title_search:
                book.display()
                found = True
            if not found:
                print('A book with this Title does not exist.\nPlease try again.')
    elif how_to_find == 'author':
        print('Searching by author will find all books by this author.')
        author_search = input('Input Author: ').lower()
        for book in library.values():
            if book.get_author().lower() == author_search:
                book.display()
                found = True
            if not found:
                print('A book with this Author does not exist.\nPlease try again.')

def borrow_book():
    display_library()
    book_to_borrow = input('Book ID being borrowed: ')
    if book_to_borrow in library:
        book = library[book_to_borrow]
        if book.get_available():
            book.set_available(False)    
            print(f'"{book.get_title()}" has been checked out.')
        else:
            print({f'"{book.get_title()}" is not available to be checked out.'})

def return_book(): 
    book_to_return = input('Book ID to return: ')
    if book_to_return in library:
        book = library[book_to_return]
        if not book.get_available():
            book.set_available(True)
            print(f'"{book.get_title()}" has been returned.')
        else:
            print(f'"{book.get_title()}" has not been checked out.')

def bo_main(library):
    print('Book operations:')
    while True:
        print('\n    1. Add Book\n    2. Borrow Book\n    3. Return Book\n    4. Search Book\n    5. Display Library\n    6. Back to Main\n')
    
        menu_selection = input('Menu Selection (Number or Menu Title): ').lower()
    
        if menu_selection == '6' or menu_selection == 'back':
            break

        elif menu_selection == '1' or menu_selection == 'add book':
            new_book(library)
        elif menu_selection == '2' or menu_selection == 'borrow book':
            borrow_book()
        elif menu_selection == '3' or menu_selection == 'return book':
            return_book()
        elif menu_selection == '4' or menu_selection == 'search library':
            search_books()
        elif menu_selection == '5' or menu_selection == 'display library':
            display_library()
        
        else:
            print('Invalid selection. Please enter either the number \"1\" or the text \"Book Operations\".')