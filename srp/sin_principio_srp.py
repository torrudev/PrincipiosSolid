###
# Algunos trucos para detectar violaciones al principio de responsabilidad única (SRP) son:
#   - La clase tiene demasiados métodos que hacen cosas distintas: Ej. clase Empleado que calcula salario, guardad datos en base de datos y genera reportes.
#   - La clase depende de muchas cosas diferentes: Muchos imports o dependencias externas pueden ser señal de múltiples responsabilidades.
#   - Cambios frecuentes en múltiples partes de la clase: Si cada vez que cambia un requerimiento distinto, tienes que modificar la misma clase, 
#     probablemente tiene mas de una responsabilidad.
#   - Dificultad para nombrar la clase: Si no puedes describir claramente lo que hace en una o dos palabras.
#   - Código dificil de probar: Si al probar una clase tienes que simular muchos aspectos diferentes posible violación del principio.
#   - Clases grandes y difíciles de mantener: Cuando se necesita mucho esfuerzo para entenderla o hacer pequeñas modificaciones probablemente esté sobrecargada.
###

# A continuación vamos a ver un ejemplo de clase sin utilizar el principio de responsabilidad única (SRP). Para ello vamos a crear una clase Jugador
# que tiene múltiples responsabilidades: almacenar datos del jugador, calcular estadísticas y exportar datos.

class JugadorNBA:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos_por_partido = []

    def agregar_puntos(self, puntos):
        self.puntos_por_partido.append(puntos)

    def promedio_puntos(self):
        return sum(self.puntos_por_partido) / len(self.puntos_por_partido)

    def guardar_en_archivo(self):
        with open(f"{self.nombre}_stats.txt", "w") as archivo:
            archivo.write(f"Estadísticas de {self.nombre}:\n")
            archivo.write(f"Promedio de puntos: {self.promedio_puntos()}\n")
            archivo.write("Puntos por partido:\n")
            
            for puntos in self.puntos_por_partido:
                archivo.write(f"\t·{puntos}\n")

# Crear jugador
Durant = JugadorNBA("Kevin Durant")

# Agregar puntos
Durant.agregar_puntos(38)
Durant.agregar_puntos(30)
Durant.agregar_puntos(23)
Durant.agregar_puntos(11)

# Calcular promedio (Esto debería ser una responsabilidad separada)
promedio = Durant.promedio_puntos()
print(f"Promedio de puntos de {Durant.nombre}: {promedio}")

# Guardar estadísticas en archivo (Esto debería ser una responsabilidad separada)
Durant.guardar_en_archivo()