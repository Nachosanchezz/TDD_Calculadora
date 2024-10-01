import math

class Calculator():
    def __init__(self):
        self.value = 0
    
    def suma(self, a, b):
        self.value = a + b
        return a + b
    def resta(self, a, b):
        self.value = a - b
        return a - b
    def multiplicacion(self, a, b):
        self.value = a * b
        return a * b
    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        self.value = a / b
        return a / b
    def potencia (self, a, b):
        self.value = a**b
        return a**b
    def raiz(self, a):
        if a < 0:
            raise ValueError("No se puede sacar raiz cuadrada de un numero negativo")
        self.value = math.sqrt(a)
        return self.value
    def factorial(self, numero):
        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos")
        elif numero == 0:
            return 1
        factor = 1
        for i in range(1, numero + 1):
            factor *= i
        return factor