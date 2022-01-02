import TooManyPagesReadError


class Book:
    def __init__(self, name: str, page_count: str):
        self.name = name
        self.page_count = page_count
        self.page_read = 0

    def __repr__(self) -> str:
        return f'<Book name=({self.name}) page_count=({self.page_count}) page_read=({self.page_read})>'

    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f'You tried to read more pages than exist')
        self.page_read += pages
        print(f'You have read {self.page_read} pages')


harry_potter = Book('Harry Potter and the Philosopher\'s Stone', 264)
harry_potter.read(30)
harry_potter.read(50)

try:
    harry_potter.read(300)
except:
    print(f'You tried read more pages than exist in this book: {harry_potter}')
