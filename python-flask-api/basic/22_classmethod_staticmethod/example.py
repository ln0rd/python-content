# IMPORTANT
# Variable set outside __init__ belong to the class. They're shared by all instances.
# Variables created inside __init__ (and all other method functions) and prefaced with self. belong to the object instance.

class Book:
    TYPES = ('hardcover', 'paperback')

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f'<Book {self.name}, {self.book_type}, {self.weight}g>'

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


# We can acess variables outside init
print(Book.TYPES)

book = Book('Harry Potter', 'hardcover', 1500)
print(book)

# creating book from factorie
book = Book.hardcover('Dom quixote', 1500)
print(book)

book = Book.paperback('Python 101', 1000)
print(book)
