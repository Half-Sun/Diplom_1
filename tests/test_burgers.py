import unittest
from unittest.mock import Mock
from diplom_1.bun import Bun
from diplom_1.ingredient import Ingredient
from diplom_1.burger import Burger


class TestBurger(unittest.TestCase):

    def setUp(self) -> Burger:
        self.burger = Burger()
        return self.burger

    def test_init(self):
        self.assertEqual(self.burger.bun, None)
        self.assertEqual(self.burger.ingredients, [])

    def test_set_buns(self):
        bun = Bun("Классическая", 50.0)
        self.burger.set_buns(bun)
        self.assertEqual(self.burger.bun, bun)

    def test_add_ingredient(self):
        ingredient = Ingredient("Огурец", "SAUCE", 10.0)
        self.burger.add_ingredient(ingredient)
        self.assertEqual(self.burger.ingredients[0], ingredient)

    def test_remove_ingredient(self):
        ingredient1 = Ingredient("Огурец", "SAUCE", 10.0)
        ingredient2 = Ingredient("Помидор", "FILLING", 15.0)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)

        self.burger.remove_ingredient(0)
        self.assertEqual(self.burger.ingredients[0], ingredient2)

        self.burger.remove_ingredient(0)
        self.assertEqual(self.burger.ingredients, [])

    def test_move_ingredient(self):
        ingredient1 = Ingredient("Огурец", "SAUCE", 10.0)
        ingredient2 = Ingredient("Помидор", "FILLING", 15.0)
        ingredient3 = Ingredient("Сыр", "CHEESE", 20.0)
        self.burger.add_ingredient(ingredient1)
        self.burger.add_ingredient(ingredient2)
        self.burger.add_ingredient(ingredient3)

        self.burger.move_ingredient(0, 2)
        self.assertEqual(
            self.burger.ingredients, [ingredient2, ingredient3, ingredient1]
        )

    def test_get_price(self):
        mock_ingredient_prices = [10.0, 15.0]
        bun = Bun("Классическая", 50.0)
        ingredients = []

        for price in mock_ingredient_prices:
            mock_ingredient = Mock(Ingredient)
            mock_ingredient.get_price.return_value = price
            ingredients.append(mock_ingredient)

        burger = Burger()
        burger.set_buns(bun)
        for ingredient in ingredients:
            burger.add_ingredient(ingredient)

        expected_price = bun.get_price() * 2 + sum(mock_ingredient_prices)
        self.assertEqual(burger.get_price(), expected_price)

    def test_get_receipt_simple(self):
        bun = Bun("Классическая", 50.0)
        ingredient1 = Ingredient("Огурец", "SAUCE", 10.0)
        ingredient2 = Ingredient("Помидор", "FILLING", 15.0)

        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        expected_substrings = [
            "(==== Классическая ====)",
            "= огурец SAUCE =",
            "= помидор FILLING =",
            "(==== Классическая ====)",
            f"Price: {burger.get_price()}",
        ]

        actual_receipt = burger.get_receipt()

        for expected_substring in expected_substrings:
            self.assertIn(expected_substring, actual_receipt)

