class Author:
    def __init__(self, name, contracts):
        self.name = name
        self.contract_list = contracts
        self.books = []

    def contracts(self):
        return [c for c in self.contract_list if c.author == self]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)

        self.contract_list.append(contract)
        self.books.append(book)
        book.authors.append(self)

        return contract

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    def __init__(self, title, contracts):
        self.title = title
        self.contract_list = contracts
        self.authors = []

    def contracts(self):
        return [c for c in self.contract_list if c.book == self]


class Contract:
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties