import prettytable

class Advertisment:

    def __init__(self, title='None', price=0.0, description='None'):
        self._title = title
        self._price = price # in €
        self._description = description

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title: str):
        self._title = title

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: float):
        self._price = price

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, text: str):
        self._description = text

    def __str__(self):
        table = prettytable.PrettyTable(['advertisement', ''])
        table.add_row(['title', self._title])
        table.add_row(['price', f'{self._price} €'])
        table.add_row(['description', self._description])
        return str(table)
