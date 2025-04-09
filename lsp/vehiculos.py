#  * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
#  * cumplir el LSP.
#  * Instrucciones:
#  * 1. Crea la clase Vehículo.
#  * 2. Añade tres subclases de Vehículo.
#  * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
#  * 4. Desarrolla un código que compruebe que se cumple el LSP.
#  */

class Vehiculo:
    def __init__(self, velocidad=0):
        self.velocidad = velocidad

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"Velocidad actual: {self.velocidad} km/h")

    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"Velocidad actual: {self.velocidad} km/h")

class Coche(Vehiculo):
    def acelerar(self, incremento):
        print("Acelerando el coche...")
        super().acelerar(incremento)
        print("El coche ha acelerado.")

    def frenar(self, decremento):
        print("Frenando el coche...")
        super().frenar(decremento)
        print("El coche ha frenado.")

class Moto(Vehiculo):
    def acelerar(self, incremento):
        print("Acelerando la moto...")
        super().acelerar(incremento)
        print("La moto ha acelerado.")

    def frenar(self, decremento):
        print("Frenando la moto...")
        super().frenar(decremento)
        print("La moto ha frenado.")

class Camion(Vehiculo):
    def acelerar(self, incremento):
        print("Acelerando el camion...")
        super().acelerar(incremento)
        print("El camion ha acelerado.")

    def frenar(self, decremento):
        print("Frenando el camion...")
        super().frenar(decremento)
        print("El camion ha frenado.")

# Comprobación del LSP

def comprobar(vehiculo):
    vehiculo.acelerar(32)
    vehiculo.frenar(12)

coche = Coche()
moto = Moto()
camion = Camion()

# Demuestrar que las subclases Coche, Moto y Camion pueden ser utilizadas como sustitutos de la clase Vehiculo sin alterar el comportamiento esperado.
comprobar(coche)
comprobar(moto)
comprobar(camion)