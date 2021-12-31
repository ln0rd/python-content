# whe  we have a class and exist another class as propertie

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Book: {self.name}'


class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f'BookShelf with {len(self.books)} books.'

    def list_of_books(self):
        for book in self.books:
            print(book)


book = Book('Harry Potter')
book2 = Book('Don\'t loot upon')
shelf = BookShelf(book, book2)


print(shelf)
shelf.list_of_books()
