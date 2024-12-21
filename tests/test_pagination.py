import unittest
from app.services.utils import Utilities


class TestPagination(unittest.TestCase):

    def test_pagination(self):
        start, end = Utilities.pagination(13, 7)
        self.assertEqual(start, 84)
        self.assertEqual(end, 91)
