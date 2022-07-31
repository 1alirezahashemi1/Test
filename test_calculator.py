import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(4,8),12)

    def test_subtraction(self):
        self.assertEqual(calculator.subtraction(36,3),33)
    
    def test_divide(self):
        with self.assertRaises(ValueError):
            calculator.divide(10,0)



if __name__ == '__main__':
    unittest.main()