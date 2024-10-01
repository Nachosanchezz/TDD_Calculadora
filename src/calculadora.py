import math

class Calculator():
    def __init__(self):
        self.value = 0
    
    def suma(self, a, b):
        self.value = a + b
        return self.value
        
    def resta(self, a, b):
        self.value = a - b
        return self.value
        
    def multiplicacion(self, a, b):
        self.value = a * b
        return self.value
        
    def division(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        self.value = a / b
        return self.value
        
    def potencia (self, a, b):
        self.value = a**b
        return self.value
       
    def raiz(self, a):
        if a < 0:
            raise ValueError("No se puede sacar raiz cuadrada de un numero negativo")
        self.value = math.sqrt(a)
        return self.value
    def factorial(self, a):
        if a == 0:
            self.value = 1
        else:
            self.value = 1
            for i in range(1, a + 1):
                self.value *= i
        return self.value
        