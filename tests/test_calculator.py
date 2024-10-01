import unittest
from src.calculadora import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_suma(self):
        self.calc.suma(2, 2)
        self.assertEqual(self.calc.value, 4)
    def test_resta(self):
        self.calc.resta(2, 2)
        self.assertEqual(self.calc.value, 0)
    def test_multiplicacion(self):
        self.calc.multiplicacion(2, 2)
        self.assertEqual(self.calc.value, 4)
    def test_division(self):
        self.calc.division(9, 9)
        self.assertEqual(self.calc.value, 1)
    def test_potencia(self):
        self.calc.potencia(7, 7)
        self.assertEqual(self.calc.value, 49)
    def test_raiz(self):
        self.calc.raiz(9)
        self.assertEqual(self.calc.value, 3)
    def test_factorial(self):
        self.calc.factorial(5)
        self.assertEqual(self.calc.value, 120)
    