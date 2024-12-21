import unittest
from unittest.mock import patch

from app.controllers.auth_controller import AuthController

class TestAuthController(unittest.TestCase):
    @patch('app.services.auth.AuthService.generate_jwt')
    def test_get_credentials(self, mock_generate_jwt):
        mock_generate_jwt.return_value = 'test_token'
        data = {'username': 'Bakshish', 'password': 'BakshishPassword'}
        response = AuthController.get_credentials(data)
        self.assertEqual(response[0], {'access_token': 'test_token'})

    @patch('app.services.auth.AuthService.decode')
    def test_authorize_error(self, mock_decode):
        mock_decode.return_value = 'error'
        result = AuthController.authorize('Bearer token')
        self.assertEqual(result, {'error': 'Invalid Payload'})

    @patch('app.services.auth.AuthService.decode')
    def test_authorize_success(self, mock_decode):
        username = 'Bakshish'
        mock_decode.return_value = {'username': username}
        result = AuthController.authorize('Bearer token')
        self.assertEqual(result, {"logged_in_as": username})
