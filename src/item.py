import csv


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:9]

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        cls.all.clear()
        try:
            with open(path, 'r', encoding='cp1251') as f:
                reader = csv.DictReader(f, delimiter=',')
                for row in reader:
                    if len(row) != 3:
                        raise InstantiateCSVError(f'Файл item.csv поврежден')

                    cls(row['name'], int(row['price']), int(row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл items.csv')

    @staticmethod
    def string_to_number(item):
        return int(float(item))

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('.')
        return self.quantity + other.quantity
