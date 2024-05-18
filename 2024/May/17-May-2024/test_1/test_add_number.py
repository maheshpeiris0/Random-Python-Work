import unittest

class TestAddNumbers(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        self.assertEqual(add_number(1,2),3)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_number(-1,-2),-3)
        
    def test_add_positive_negative_numbers(self):
        self.assertEqual(add_number(1,-2),-1)


if __name__ == '__main__':
    unittest.main()