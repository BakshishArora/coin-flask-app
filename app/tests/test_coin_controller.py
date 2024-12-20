import unittest
from unittest.mock import patch
from services.coin_service import CoinService  
from services.utils import Utilities
from controllers.coins_controller import CoinsController
from config import Config


class TestCoinController(unittest.TestCase):

    @patch('services.coin_service.CoinService.get_coin_details')
    @patch('services.utils.Utilities.pagination')
    def test_get_coin_details(self, mockutils, mockcontroller):
        mockutils.return_value = 2, 1
        mockcontroller.return_value = [{}, {}, {}]
        response = CoinsController.get_coin_details()
        self.assertEquals(len(response),2)

    @patch('services.coin_service.CoinService.get_coins_list')
    @patch('services.utils.Utilities.pagination')
    def test_get_coin_list(self, mockutils, mockcontroller):
        mockutils.return_value = 1, 3
        mockcontroller.return_value = [{}, {}, {}]
        response = CoinsController.get_coins_list()
        print(response)
        self.assertEquals(len(response),3)

    @patch('services.coin_service.CoinService.get_coins_categories_list')
    @patch('services.utils.Utilities.pagination')
    def test_get_coin_categories_list(self, mockutils, mockcontroller):
        mockutils.return_value = 1, 4
        mockcontroller.return_value = [{}, {}, {}, {}]
        response = CoinsController.get_coins_categories_list()
        print(response)
        self.assertEquals(len(response),4)

class TestPagination(unittest.TestCase):

    def test_pagination(self):
        start, end = Utilities.pagination(13, 7)
        self.assertEqual(start, 84)
        self.assertEqual(end, 91)




if __name__ == '__main__':
    unittest.main()
