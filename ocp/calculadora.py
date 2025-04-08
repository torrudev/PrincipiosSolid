#  * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas. 
#  * Requisitos:
#  * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
#  * Instrucciones:
#  * 1. Implementa las operaciones de suma, resta, multiplicación y división.
#  * 2. Comprueba que el sistema funciona.
#  * 3. Agrega una quinta operación para calcular potencias.
#  * 4. Comprueba que se cumple el OCP.

from abc import ABC, abstractmethod
    
class Operacion(ABC):
    @abstractmethod
    def calculo(a,b):
        pass

class Calculadora:
    def __init__(self):
        self.operaciones = {}

    def agregar_operacion(self, nombre: str, operacion: Operacion):
        self.operaciones[nombre] = operacion

    def calcular(self, operacion: str, a, b):
        if operacion not in self.operaciones:
            return f"Operación '{operacion}' no registrada en la calculadora."
        return self.operaciones[operacion].calculo(a, b)
    
class Suma(Operacion):
    def calculo(self, a, b):
        return a + b
    
class Resta(Operacion):
    def calculo(self, a, b):
        return a - b

class Multiplicacion(Operacion):
    def calculo(self, a, b):
        return a * b

class Division(Operacion):
    def calculo(self, a, b):
        if b == 0:
            return "No se puede dividir entre cero."
        return a / b
    
# instanciar la calculadora
calculadora = Calculadora()

# agregar operaciones
calculadora.agregar_operacion("suma", Suma())
calculadora.agregar_operacion("resta", Resta())
calculadora.agregar_operacion("multiplicacion", Multiplicacion())
calculadora.agregar_operacion("division", Division())

# calcular operaciones
print(calculadora.calcular("suma", 5, 3))
print(calculadora.calcular("resta", 5, 3))
print(calculadora.calcular("multiplicacon", 5, 3))
print(calculadora.calcular("division", 5, 0))

# agregar una nueva operación (potencia) sin modificar el código existente.
class Potencia(Operacion):
    def calculo(self, a, b):
        return a ** b
    
calculadora.agregar_operacion("potencia", Potencia())

print(calculadora.calcular("potencia", 2, 3))