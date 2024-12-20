import unittest
from unittest.mock import patch
from services.coin_service import CoinService
from config import Config


class TestCoinService(unittest.TestCase):
    
    def test_get_coins_list(self):
       response = CoinService.get_coins_list()
       self.assertEqual(response[0], {
        "id": "01coin",
        "symbol": "zoc",
        "name": "01coin" })

    def test_get_coins_categories_list(self):
        result = CoinService.get_coins_categories_list()
        self.assertEqual(result[0], {
            "category_id": "8bit-chain-ecosystem",
            "name": "8Bit Chain Ecosystem"
        })

    def test_get_coin_details(self):
        vs_currency = 'cad'
        result = CoinService.get_coin_details(vs_currency)
        self.assertEqual(result[0]["id"],"bitcoin")
