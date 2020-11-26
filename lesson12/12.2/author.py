

class Author:

    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def new_book(self, book):
        self.books.append(book)
        return book

    def __str__(self):
        return 'name: {}, country: {}, birthday: {}'.format(self.name, self.country, self.birthday)


