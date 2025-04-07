###
# SRP (Single Responsibility Principle o Principio de Responsabilidad Única)
# Una clase debe tener una, y solo una, razón para cambiar. Esto significa que una clase debe tener una única responsabilidad o propósito.
# Algunas de las ventajas son:
#   - Facilita la comprensión del código.
#   - Fácil de mantener.
#   - Mejor aplicación de pruebas unitarias.
#   - Sistema más modular y escalable.
###

# Este ejemplo ilustra el principio de responsabilidad única (SRP) al separar las responsabilidades de un jugador de baloncesto, 
# el cálculo de estadísticas y la exportación de datos.

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntos_por_partido = []

    def agregar_puntos(self, puntos):
        self.puntos_por_partido.append(puntos)

class CalculadoraEstadisticas:
    def promedio_puntos(self, jugador: Jugador):
        if not jugador.puntos_por_partido:
            return "Este jugador no ha jugado ningún partido."
        return sum(jugador.puntos_por_partido) / len(jugador.puntos_por_partido)

class ExportarDatos:
    def exportar_a_csv(self, jugador: Jugador, promedio):
        with open(f"{jugador.nombre}_stats.txt", 'w') as archivo:
            archivo.write(f"Estadísticas de {jugador.nombre}:\n")
            archivo.write(f"Promedio de puntos: {promedio}\n")
            archivo.write("Puntos por partido:\n")
            
            for puntos in jugador.puntos_por_partido:
                archivo.write(f"\t·{puntos}\n")

# Crear jugador
lebron = Jugador("LeBron James")
curry = Jugador("Stephen Curry")

# Agregar puntos
lebron.agregar_puntos(25)
lebron.agregar_puntos(16)
lebron.agregar_puntos(33)
lebron.agregar_puntos(26)
curry.agregar_puntos(13)
curry.agregar_puntos(52)
curry.agregar_puntos(37)
curry.agregar_puntos(36)

# Calcular promedio
calculadora = CalculadoraEstadisticas()

promedio_lebron = calculadora.promedio_puntos(lebron)
promedio_curry = calculadora.promedio_puntos(curry)

print(f"Promedio de puntos de {lebron.nombre}: {promedio_lebron}")
print(f"Promedio de puntos de {curry.nombre}: {promedio_curry}")

exportador = ExportarDatos()
exportador.exportar_a_csv(lebron, promedio_lebron)