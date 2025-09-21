class Author:
    def __init__(self, name, nationality):
        self._name = name
        self._nationality = nationality

    @property
    def name(self):
        return self._name

    @property
    def nationality(self):
        return self._nationality

    def __str__(self):
        return f"{self._name} ({self._nationality})"


class Book:
    def __init__(self, title, author: Author):
        self._title = title
        self._author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value.strip():
            self._title = value
        else:
            raise ValueError("Title cannot be empty")

    @property
    def author(self):
        return self._author

    def info(self):
        return f"'{self._title}' by {self._author}"

    def __str__(self):
        return self.info()

class EBook(Book):
    def __init__(self, title, author: Author, file_size):
        super().__init__(title, author)
        self.__file_size = file_size

    @property
    def file_size(self):
        return self.__file_size

    @file_size.setter
    def file_size(self, value):
        if value > 0:
            self.__file_size = value
        else:
            raise ValueError("File size must be positive")

    def info(self):
        return f"E-Book: '{self._title}' ({self.__file_size}MB) by {self._author}"


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, book: Book):
        self.__books.append(book)

    def remove_book(self, title):
        self.__books = [b for b in self.__books if b.title != title]

    def list_books(self):
        if not self.__books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.__books, 1):
                print(f"{idx}. {book.info()}")


if __name__ == "__main__":
    author1 = Author("George Orwell", "British")
    author2 = Author("Jane Austen", "British")

    b1 = Book("1984", author1)
    b2 = Book("Pride and Prejudice", author2)
    eb1 = EBook("Animal Farm", author1, 1.5)

    lib = Library()
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(eb1)

    print("Library contents:")
    lib.list_books()

    eb1.file_size = 2.0
    print("\nAfter updating ebook size:")
    lib.list_books()

    lib.remove_book("1984")
    print("\nAfter removing 1984:")
    lib.list_books()
