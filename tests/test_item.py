"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    item1.calculate_total_price()
    assert item1.price * item1.quantity == 200000
    assert item2.price * item2.quantity == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item1.apply_discount()
    assert item1.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number("1") == 1
    assert Item.string_to_number("1.4") == 1
    assert Item.string_to_number("1.0") == 1


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_name():
    Item.name = 'Смартфон'
    assert Item.name == 'Смартфон'
def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test_sts():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'

