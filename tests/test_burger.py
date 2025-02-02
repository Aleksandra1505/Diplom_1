import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock
from tests.helpers import create_burger_with_mock_ingredients
from test_data import TestData

class TestBurger:
    @pytest.mark.parametrize('bun', TestData.buns)
    def test_set_buns(self, bun):
        burger = Burger()
        bun_obj = Bun(bun['name'], bun['price'])
        burger.set_buns(bun_obj)

        assert burger.bun.get_name() == bun_obj.get_name()
        assert burger.bun.get_price() == bun_obj.get_price()

    @pytest.mark.parametrize('ingredients', TestData.ingredients)
    def test_add_ingredient(self, ingredients):
        burger = Burger()
        ingredient_obj = Ingredient(ingredients[0], ingredients[1], ingredients[2])
        burger.add_ingredient(ingredient_obj)

        assert ingredient_obj in burger.ingredients

    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_remove_ingredient(self,index: int):
        burger, mock_ingredients = create_burger_with_mock_ingredients()
        ingredient_to_remove = burger.ingredients[index]
        burger.remove_ingredient(index)

        assert ingredient_to_remove not in burger.ingredients

    @pytest.mark.parametrize("index, new_index", [(0, 1), (1, 0), (2, 1)])
    def test_move_ingredient(self, index: int, new_index: int):
        burger, mock_ingredients = create_burger_with_mock_ingredients()
        ingredient_to_move = burger.ingredients[index]
        burger.move_ingredient(index, new_index)

        assert burger.ingredients[new_index] == ingredient_to_move

    def test_get_price(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_price.return_value = TestData.buns[1]['price']

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = TestData.ingredients[1][2]

        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]

        assert burger.get_price() == mock_bun.get_price() * 2 + mock_ingredient.get_price()

    def test_get_receipt(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = TestData.buns[0]['name']
        mock_bun.get_price.return_value = TestData.buns[0]['price']
        burger.bun = mock_bun

        mock_ingredient1 = Mock()
        mock_ingredient1.get_name.return_value = TestData.ingredients[0][1]
        mock_ingredient1.get_type.return_value = 'соусы'
        mock_ingredient1.get_price.return_value = TestData.ingredients[0][2]

        mock_ingredient2 = Mock()
        mock_ingredient2.get_name.return_value = TestData.ingredients[5][1]
        mock_ingredient2.get_type.return_value = 'начинки'
        mock_ingredient2.get_price.return_value = TestData.ingredients[5][2]

        mock_ingredient3 = Mock()
        mock_ingredient3.get_name.return_value = TestData.ingredients[7][1]
        mock_ingredient3.get_type.return_value = 'начинки'
        mock_ingredient3.get_price.return_value = TestData.ingredients[7][2]

        burger.ingredients = [mock_ingredient1, mock_ingredient2, mock_ingredient3]
        expected_receipt = "(==== Флюоресцентная булка R2-D3 ====)\n= соусы Соус Spicy-X =\n= начинки Говяжий метеорит (отбивная) =\n= начинки Филе Люминесцентного тетраодонтимформа =\n(==== Флюоресцентная булка R2-D3 ====)\nPrice: 6054"
        receipt_text = burger.get_receipt().replace("\n\n", "\n")

        assert receipt_text == expected_receipt


    

