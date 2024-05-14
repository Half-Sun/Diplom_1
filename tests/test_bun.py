import unittest
from unittest.mock import patch
from diplom_1.bun import Bun

class TestBun(unittest.TestCase):

    @patch("diplom_1.bun.Bun.__init__", return_value=None)
    def test_init_with_mock_1(self, mock_init):
        Bun("Сезам", 60.0)
        mock_init.assert_called_once_with("Сезам", 60.0)

    @unittest.mock.patch("diplom_1.bun.Bun.__init__", return_value=None)
    def test_init_with_mock_2(self, mock_init):
        Bun("Сезам", 60.0)
        mock_init.assert_called_once_with("Сезам", 60.0)

    def test_init_sets_name_and_price_correctly(self):
        bun_name = "Классическая"
        bun_price = 50.0
        bun = Bun(bun_name, bun_price)
        self.assertEqual(bun.name, bun_name)
        self.assertEqual(bun.price, bun_price)

    def test_get_name_returns_correct_name(self):
        bun_name = "Классическая"
        bun_price = 50.0
        bun = Bun(bun_name, bun_price)
        self.assertEqual(bun.get_name(), bun_name)

    def test_get_price_returns_correct_price(self):
        bun_name = "Классическая"
        bun_price = 50.0
        bun = Bun(bun_name, bun_price)
        self.assertEqual(bun.get_price(), bun_price)
