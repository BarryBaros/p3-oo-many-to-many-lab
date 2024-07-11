class Author:
    def __init__(self, name):
        self.name = name


class Book:
    def __init__(self, title):
        self.title = title



class Contract:
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError(" royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties