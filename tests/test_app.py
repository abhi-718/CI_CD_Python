import unittest
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




