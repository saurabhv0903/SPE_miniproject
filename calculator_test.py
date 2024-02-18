import unittest
import calculator_main

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(calculator_main.square_root(16), 4.0)   # Square root of 16 is 4
        self.assertAlmostEqual(calculator_main.square_root(25), 5.0)   # Square root of 25 is 5
        self.assertAlmostEqual(calculator_main.square_root(4), 2.0)    # Square root of 4 is 2
        self.assertAlmostEqual(calculator_main.square_root(9), 3.0)    # Square root of 9 is 3

    def test_factorial(self):
        self.assertEqual(calculator_main.factorial(0), 1)     # Factorial of 0 is 1
        self.assertEqual(calculator_main.factorial(1), 1)     # Factorial of 1 is 1
        self.assertEqual(calculator_main.factorial(5), 120)   # Factorial of 5 is 120
        self.assertEqual(calculator_main.factorial(6), 720)   # Factorial of 6 is 720

    def test_natural_log(self):
        self.assertAlmostEqual(calculator_main.natural_log(1), 0.0)          # Natural log of 1 is 0
        self.assertAlmostEqual(calculator_main.natural_log(2), 0.6931471806) # Natural log of 2 is approximately 0.6931
        self.assertAlmostEqual(calculator_main.natural_log(3), 1.0986122886) # Natural log of 3 is approximately 1.0986
        self.assertAlmostEqual(calculator_main.natural_log(5), 1.6094379124) # Natural log of 5 is approximately 1.6094

    def test_power(self):
        self.assertAlmostEqual(calculator_main.power(2, 3), 8.0)     # 2 raised to the power 3 is 8
        self.assertAlmostEqual(calculator_main.power(4, 2), 16.0)    # 4 raised to the power 2 is 16
        self.assertAlmostEqual(calculator_main.power(5, 2), 25.0)    # 5 raised to the power 2 is 25
        self.assertAlmostEqual(calculator_main.power(4, 3), 64.0)    # 4 raised to the power 3 is 64

if __name__ == '__main__':
    unittest.main()

