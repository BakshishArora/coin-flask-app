import unittest
from unittest.mock import patch, MagicMock

from app.services.auth import AuthService

class TestAuthService(unittest.TestCase):
    def test_generate_jwt(self):
        token = AuthService.generate_jwt('Bakshish')
        self.assertIsNotNone(token)
    
    @patch('jwt.decode')
    def test_decode(self, mock_jwt_decode):
        mock_jwt_decode.return_value = {'username': 'Bakshish'}
        decoded_payload = AuthService.decode('token')
        self.assertEqual(decoded_payload, {'username': 'Bakshish'})