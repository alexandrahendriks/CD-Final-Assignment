import unittest
from main import index, cow


class TestFunctions(unittest.TestCase):
    def test_index(self):
        assert index() == "Hello, world!"