from praktikum.database import Database

class TestDataBase:

    def test_available_buns(self):
        database = Database()
        accessible_buns = database.available_buns()
        real_name = ["black bun", "white bun", "red bun"]
        actual_name = [bun.get_name() for bun in accessible_buns]
        assert real_name == actual_name

    def test_available_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        real_name = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_name = [ingredient.get_name() for ingredient in available_ingredients]
        assert real_name == actual_name


