
from author import Author

class Book:

    book_amount = 0

    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.book_amount +=1

    def __str__(self):
        return 'name: {}, year: {}, author: ({})'.format(self.name, self.year, self.author)







