from unittest.mock import Mock
from praktikum.burger import Burger
from test_data import TestData

def create_mock_ingredient(index: int):
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = TestData.ingredients[index][2]
    mock_ingredient.get_name.return_value = TestData.ingredients[index][1]
    mock_ingredient.get_type.return_value = TestData.ingredients[index][0]
    return mock_ingredient

def create_burger_with_mock_ingredients(count=3):
    burger = Burger()
    mock_ingredients = []
    for i in range(count):
        mock_ingredient = create_mock_ingredient(i)
        burger.add_ingredient(mock_ingredient)
        mock_ingredients.append(mock_ingredient)
    return burger, mock_ingredients