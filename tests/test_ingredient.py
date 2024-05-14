import unittest
from parameterized import parameterized
from unittest.mock import MagicMock
from diplom_1.ingredient import Ingredient


class TestIngredient(unittest.TestCase):

    def setUp(self):
        self.ingredient = Ingredient("SAUCE", "Сырный", 15.0)

    def test_init(self):
        self.assertEqual(self.ingredient.type, "SAUCE")
        self.assertEqual(self.ingredient.name, "Сырный")
        self.assertEqual(self.ingredient.price, 15.0)

    @parameterized.expand([
        (10.50,),
        (20.75,),
        (30.0,),
    ])
    def test_price_formatting(self, mocked_price):
        self.ingredient.get_price = MagicMock(return_value=mocked_price)
        formatted_price = self.ingredient.get_price()
        self.assertEqual(formatted_price, mocked_price)

    @parameterized.expand([
        ("Сырный с зеленью",),
        ("Грибной",),
        ("С кунжутом",),
    ])
    def test_name_formatting(self, mocked_name):
        self.ingredient.name = mocked_name
        self.assertEqual(self.ingredient.get_name(), mocked_name)

    @parameterized.expand([
        ("SAUCE",),
        ("FILLING",),
        ("CHEESE",),
    ])
    def test_type_formatting(self, mocked_type):
        self.ingredient.type = mocked_type
        self.assertEqual(self.ingredient.get_type(), mocked_type)
