import unittest
from app.services.coin_service import CoinService


class TestCoinService(unittest.TestCase):
    '''
        The tests may fail if rate limits are exceeded (if endpoint is hit too many times in short period) for Coingecko API.
    '''

    def test_get_coins_list(self):
        response = CoinService.get_coins_list()
        response = response[0]
        self.assertIn('id', response)
        self.assertIn('symbol', response)
        self.assertIn('name', response)

    def test_get_coins_categories_list(self):
        response = CoinService.get_coins_categories_list()
        response = response[0]
        self.assertIn('category_id', response)
        self.assertIn('name', response)

    def test_get_coin_details(self):
        vs_currency = 'cad'
        result = CoinService.get_coin_details(vs_currency)
        self.assertEqual(result[0]["id"], "bitcoin")
