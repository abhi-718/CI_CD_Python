import unittest
from unittest import result
from src import app

class Testcalc(unittest.TestCase):

    def test_add(self):
        result = app.add(10,15)
        self.assertEqual(result,25)

    def test_sub(self):
        result = app.sub(10,5)
        self.assertEqual(result,5)

    def test_mul(self):
        result = app.mul(4,3)
        self.assertEqual(result,12)

    def test_power(self):
        result = app.power(5,2)
        self.assertEqual(result,25)
    
    def test_divide(self):
        result = app.divide(6,3)
        self.assertEqual(result,2)
        self.assertRaises(Exception,app.divide,4,0)

        with self.assertRaises(Exception, msg="Try again"):
            app.divide(4,0)
    
    


if __name__ == '__main__':
    unittest.main()

