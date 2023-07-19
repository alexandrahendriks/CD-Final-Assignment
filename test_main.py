import unittest
from main import index, cow, final


class TestFunctions(unittest.TestCase):
    def test_index(self):
        assert index() == "Hello, world!"
    def test_cow(self):
        assert cow() == "MOoooOo!"
    def test_final(self):
        assert final() == "Welcome to my final assignmen!"  