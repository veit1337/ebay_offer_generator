import prettytable

from equipment_entry import EquipmentEntry

class Advertisment:

    def __init__(self, title='None', price=0.0, equipment=[], description_intro='None'):
        self._title = title
        self._price = price # in €
        self._equipment: list[EquipmentEntry] = equipment
        self._description = description_intro

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
    def equipment(self):
        return self._equipment

    @equipment.setter
    def equipment(self, equipment: list):
        self._equipment = equipment

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
        table.add_row(['description_intro', self._description])
        for item in self._equipment:
            table.add_row(['', item])
        return str(table)
