from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


result: float = list_avg([5, 5, 9])
print(result)


class Book():
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

    def __str__(self) -> str:
        return f'Book name: {self.name} pages: {self.page_count}'

    def __repr__(self) -> str:
        return f'<Book(name={self.name}, pages={self.page_count})>'


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'

    def list_of_books(self) -> List[Book]:
        print(self.books)


book: Book = Book(name='Harry Potter', page_count=1045)
book2: Book = Book(name='Python 101', page_count=500)
shelf: BookShelf = BookShelf([book, book2])
print(shelf)
shelf.list_of_books()
