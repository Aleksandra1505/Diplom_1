import pytest
from praktikum.ingredient import Ingredient
from test_data import TestData

class TestIngredient:
    @pytest.mark.parametrize('ingredients', TestData.ingredients)
    def test_get_price(self, ingredients):
        ingredient_type = ingredients[0]
        name = ingredients[1]
        price = ingredients[2]
        burger = Ingredient(ingredient_type, name, price)
        assert burger.get_name() == name

    @pytest.mark.parametrize('ingredients', TestData.ingredients)
    def test_get_price(self, ingredients):
        ingredient_type = ingredients[0]
        name = ingredients[1]
        price = ingredients[2]
        burger = Ingredient(ingredient_type, name, price)
        assert burger.get_price() == price

    @pytest.mark.parametrize('ingredients', TestData.ingredients)
    def test_get_type(self, ingredients):
        ingredient_type = ingredients[0]
        name = ingredients[1]
        price = ingredients[2]
        burger = Ingredient(ingredient_type, name, price)
        assert burger.get_type() == ingredient_type




