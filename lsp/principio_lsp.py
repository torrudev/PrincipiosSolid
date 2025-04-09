###
# LSP (Liskov Substitution Principle) - Principio de Sustitución de Liskov
# Este principio formulado por Barbara Liskov establece que los objetos de una subclase deben poder sustituir a los objetos de la superclase sin alterar
# el comportamiento del programa. En otras palabras, si una clase B es una subclase de A, entonces los objetos de la clase A deben poder ser reemplazados 
# por objetos de la clase B sin que el programa falle o produzca resultados inesperados.
###

# Este ejemplo ilustra el LSP al usar subclases de la clase Figura (Cuadrado y Circulo) que pueden ser utilizadas como sustitutos de la clase Figura sin alterar
# el comportamiento esperado.
class Figura:
    def dibujar(self):
        return "Dibujando una figura"
    
class Cuadrado(Figura):
    def dibujar(self):
        return "Dibujando un cuadrado"
    
class Circulo(Figura):
    def dibujar(self):
        return "Dibujando un círculo"

# Dibujamos una figura
figura = Figura()
print(figura.dibujar())

# Ahora vamos a usar el metodo dibujar() de la clase padre desde las subclases obteniendo el mismo tipo de resultado esperado.
# Por lo tanto, podemos decir que las subclases cumplen con el principio de sustitución de Liskov.
cuadrado = Cuadrado()
circulo = Circulo()
print(cuadrado.dibujar())
print(circulo.dibujar())