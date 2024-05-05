import pytest
from unittest.mock import patch
from diplom_1.bun import Bun


class TestBun:

    @pytest.mark.parametrize("bun_name, bun_price", [("Классическая", 50.0), ("Сезам", 60.0), ("Бриошь", 70.0)])
    def test_init_sets_name_and_price_correctly(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name
        assert bun.price == bun_price

    @pytest.mark.parametrize("bun_name, bun_price", [("Классическая", 50.0), ("Сезам", 60.0), ("Бриошь", 70.0)])
    def test_get_name_returns_correct_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_name, bun_price", [("Классическая", 50.0), ("Сезам", 60.0), ("Бриошь", 70.0)])
    def test_get_price_returns_correct_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

    @patch("diplom_1.bun.Bun.__init__", return_value=None)
    def test_init_with_mock(self, mock_init):
        Bun("Сезам", 60.0)
        mock_init.assert_called_once_with("Сезам", 60.0)


if __name__ == "__main__":
    pytest.main()
