
from book import Book

class Library:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, book):
        self.books.append(book)
        self.authors.append(book.author)
        return book

    def group_by_author(self, author):
        books = []
        for book in self.books:
            if book.author == author:
                books.append(book)
        return books

    def group_by_year(self, year):
        books = []
        for book in self.books:
            if book.year == year:
                books.append(book)
        return books






