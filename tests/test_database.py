
import unittest
from unittest.mock import patch
from diplom_1.bun import Bun
from diplom_1.ingredient import Ingredient
from diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE
from diplom_1.database import Database
from diplom_1.conftest import SESAME_BUN_NAME, SESAME_BUN_PRICE, MUSTARD_INGREDIENT_NAME, MUSTARD_INGREDIENT_PRICE

class TestDatabase(unittest.TestCase):

    def test_init(self):
        db = Database()

        self.assertEqual(len(db.buns), 3)
        self.assertEqual(len(db.ingredients), 6)

        found_black_bun = any(bun.name == "black bun" and bun.price == 100 for bun in db.buns)
        self.assertTrue(found_black_bun)

    @patch.object(Database, 'available_buns')
    def test_available_buns_simple(self, mock_available_buns):
        test_buns = [Bun(SESAME_BUN_NAME, SESAME_BUN_PRICE)]
        mock_available_buns.return_value = test_buns

        db = Database()
        available_buns = db.available_buns()

        self.assertNotEqual(available_buns, [])

    @patch.object(Database, 'available_ingredients')
    def test_available_ingredients(self, mock_available_ingredients):
        test_ings = [Ingredient(INGREDIENT_TYPE_SAUCE, MUSTARD_INGREDIENT_NAME, MUSTARD_INGREDIENT_PRICE)]
        mock_available_ingredients.return_value = test_ings

        db = Database()
        available_ingredients = db.available_ingredients()

        self.assertEqual(available_ingredients, test_ings)


if __name__ == "__main__":
    unittest.main()
