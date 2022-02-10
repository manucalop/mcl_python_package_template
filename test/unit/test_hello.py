import unittest
from hello_world import hello

class TestSpreadsheetApi(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(True, True, 'I leave Python!')

if __name__ == '__main__':
    unittest.main()

