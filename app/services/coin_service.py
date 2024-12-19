from config import Config
import requests

class CoinService:
    
    @classmethod
    def get_coins_list(cls):
        url = Config.COINGECKO_API_BASE + '/list'
        response = requests.get(url)        
        data = response.json()
        return data

    @classmethod
    def get_coins_categories_list(cls):
        url = Config.COINGECKO_API_BASE + '/categories/list'
        response = requests.get(url)
        data = response.json()
        return data