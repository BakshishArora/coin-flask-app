import unittest
from unittest.mock import patch

from app.controllers.coins_controller import CoinsController


class TestCoinController(unittest.TestCase):

    @patch('app.services.coin_service.CoinService.get_coin_details')
    @patch('app.services.utils.Utilities.pagination')
    def test_get_coin_details(self, mockutils, mockcontroller):
        mockutils.return_value = 2, 1
        mockcontroller.return_value = [{}, {}, {}]
        response = CoinsController.get_coin_details()
        self.assertEqual(len(response), 2)

    @patch('app.services.coin_service.CoinService.get_coins_list')
    @patch('app.services.utils.Utilities.pagination')
    def test_get_coin_list(self, mockutils, mockcontroller):
        mockutils.return_value = 2, 1
        mockcontroller.return_value = [{}, {}, {}]
        response = CoinsController.get_coins_list()
        print(response)
        self.assertEqual(len(response), 2)

    @patch('app.services.coin_service.CoinService.get_coins_categories_list')
    @patch('app.services.utils.Utilities.pagination')
    def test_get_coin_categories_list(self, mockutils, mockcontroller):
        mockutils.return_value = 2, 1
        mockcontroller.return_value = [{}, {}, {}]
        response = CoinsController.get_coins_categories_list()
        print(response)
        self.assertEqual(len(response), 2)
