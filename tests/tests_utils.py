import pytest
from utils import *

def test_get_price():
    item = Item("Смартфон", 10000, 20)
    assert type(item.get_price()) == int
def test_apply_discount():

    item = Item("Смартфон", 10000, 20)
    item.aply_discount()
    assert item.price == 7000

def test_property():
    item = Item("Смартфон", 10000, 20)
    assert item.name == "Смартфон"


def test_staticmethod():
    assert Item.is_integer(5) == True
    assert Item.is_integer(5.0) == True
    assert Item.is_integer(5.1) == False

def test_init_():
    c = Phone('Iphone', 10, 20, 2)
    assert c.sim == 2

def test_add():
    c = Phone('Iphone', 10, 20, 2)
    b = Item('Phone', 10, 20)
    assert b + c == 40

