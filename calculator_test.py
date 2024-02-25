import unittest
import calculator_main

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertAlmostEqual(calculator_main.square_root(16), 4.0)   
        self.assertAlmostEqual(calculator_main.square_root(25), 5.0)   
        self.assertAlmostEqual(calculator_main.square_root(4), 2.0)    
        self.assertAlmostEqual(calculator_main.square_root(9), 3.0)    

    def test_factorial(self):
        self.assertEqual(calculator_main.factorial(0), 1)     
        self.assertEqual(calculator_main.factorial(1), 1)     
        self.assertEqual(calculator_main.factorial(5), 120)   
        self.assertEqual(calculator_main.factorial(6), 720)   

    def test_natural_log(self):
        self.assertAlmostEqual(calculator_main.natural_log(1), 0.0)          
        self.assertAlmostEqual(calculator_main.natural_log(2), 0.6931471806) 
        self.assertAlmostEqual(calculator_main.natural_log(3), 1.0986122886) 
        self.assertAlmostEqual(calculator_main.natural_log(5), 1.6094379124) 

    def test_power(self):
        self.assertAlmostEqual(calculator_main.power(2, 3), 8.0)     
        self.assertAlmostEqual(calculator_main.power(4, 2), 16.0)    
        self.assertAlmostEqual(calculator_main.power(5, 2), 25.0)    
        self.assertAlmostEqual(calculator_main.power(4, 3), 64.0)    

if __name__ == '__main__':
    unittest.main()

