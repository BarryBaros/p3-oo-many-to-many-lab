class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return [contract for contract in Contract.all_contracts() if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Invalid type for book")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        book.add_contract(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"Author('{self.name}')"


class Book:
    _all_books = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book._all_books.append(self)

    @classmethod
    def all_books(cls):
        return cls._all_books

    def contracts(self):
        return [contract for contract in Contract.all_contracts() if contract.book == self]

    def add_contract(self, contract):
        self._contracts.append(contract)

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))

    def __repr__(self):
        return f"Book('{self.title}')"


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Invalid type for author")
        if not isinstance(book, Book):
            raise Exception("Invalid type for book")
        if not isinstance(date, str):
            raise Exception("Invalid type for date")
        if not isinstance(royalties, int):
            raise Exception("Invalid type for royalties")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract._all_contracts.append(self)

    @classmethod
    def all_contracts(cls):
        return cls._all_contracts

    @classmethod
    def contracts_by_date(cls, date):
        return sorted([contract for contract in cls.all_contracts() if contract.date == date], key=lambda x: x.date)

    def __repr__(self):
        return f"Contract(author={self.author}, book={self.book}, date='{self.date}', royalties={self.royalties})"

# Example usage:

if __name__ == "__main__":
    # Create authors
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")

    # Create books
    book1 = Book("Python Programming")
    book2 = Book("Data Science Essentials")

    # Authors signing contracts for books
    author1.sign_contract(book1, "2023-01-01", 50000)
    author2.sign_contract(book1, "2023-02-01", 60000)
    author2.sign_contract(book2, "2023-03-01", 70000)

    # Testing methods
    print("Author 1 contracts:", author1.contracts())
    print("Author 1 books:", author1.books())
    print("Author 1 total royalties:", author1.total_royalties())

    print("Author 2 contracts:", author2.contracts())
    print("Author 2 books:", author2.books())
    print("Author 2 total royalties:", author2.total_royalties())

    # Testing Contract class method
    contracts_in_january = Contract.contracts_by_date("2023-01-01")
    print("Contracts signed on January 1, 2023:", contracts_in_january)
