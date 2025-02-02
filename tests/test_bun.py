import pytest
from praktikum.bun import Bun
from test_data import TestData

class TestBun:

    @pytest.mark.parametrize('bun', TestData.buns)
    def test_get_price(self, bun):
        name = bun['name']
        price = bun['price']
        burger = Bun(name, price)
        assert burger.get_name() == name

    @pytest.mark.parametrize('bun', TestData.buns)
    def test_get_price(self, bun):
        name = bun['name']
        price = bun['price']
        burger = Bun(name, price)
        assert burger.get_price() == price

