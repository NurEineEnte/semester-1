import unittest
from weather import comfort_level
class Test_comfort(unittest.TestCase):
    def test_cold(self):
        self.assertEqual(comfort_level(15), "COLD")
        self.assertEqual(comfort_level(11.2), "COLD")

    def test_hot(self):
        self.assertEqual(comfort_level(80), "HOT")
        self.assertEqual(comfort_level(25.1), "HOT")
        
    def test_ok(self):
        self.assertEqual(comfort_level(25), "OK")
        self.assertEqual(comfort_level(18.4), "OK")

if __name__ == '__main__':
    unittest.main()