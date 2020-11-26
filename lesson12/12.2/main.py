from library import Library
from book import Book
from author import Author

author1 = Author('John Snow', 'USA', 1980)
author2 = Author('Homer Simpson', 'Germany', 1790)

book1 = Book('Black', 1890, author1)
book2 = Book('White', 2000, author1)
print(str(Book.book_amount))

library = Library('school')
library.new_book(book1)
library.new_book(book2)

library_amount = len(library.books)

for item in library.books:
    print(item)

def print_all_books(books):
    for book in books:
        print(book)

books_by_author = library.group_by_author(author1)
print_all_books(books_by_author)

books_by_year = library.group_by_year(2000)
print_all_books(books_by_year)








