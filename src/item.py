import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8
    all = []


    def __init__(self, __name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = __name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'Item({self.__name}, {self.price}, {self.quantity})'

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
    def instantiate_from_csv(cls):
        with open('..\src\items.csv', 'r', encoding='windows-1251') as file:
            reader = csv.DictReader(file, delimiter=',')
            cls.all.clear()
            for row in reader:
                cls.all.append(cls(row['name'], int(row['price']), int(row['quantity'])))
            return cls.all

    @staticmethod
    def string_to_number(item):
        return int(float(item))
