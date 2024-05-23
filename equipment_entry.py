class EquipmentEntry():

    def __init__(self, description='None', quantity=0):
        self._description = description
        self._quantity = quantity

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int):
        self.quantity = quantity

    def __str__(self):
        entry_str = f'{self._quantity}x {self._description}\n'
        return entry_str
