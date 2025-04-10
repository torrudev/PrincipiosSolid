###
# DIP (Dependency Inversion Principle) - Principio de Inversión de Dependencias
# Este principio establece que los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
# Los detalles deben depender de las abstracciones, no al revés.
###

# Abstracion
class RepositorioUsuario:
    def guardar(self, datos):
        raise NotImplementedError()

# Implementacion concreta
class MySQLRepositorio(RepositorioUsuario):
    def guardar(self, datos):
        print("Guardando en MySQL")

# Depende de la abstracción
class ServicioUsuario:
    def __init__(self, repositorio: RepositorioUsuario):
        self.repositorio = repositorio

    def registrar_usuario(self, usuario):
        self.repositorio.guardar(usuario)

mysql_repo = MySQLRepositorio()
servicio = ServicioUsuario(mysql_repo)
servicio.registrar_usuario("Juan")

# Otro ejemplo en el que si se aplica el DIP

# Abstracion
class AbstractInterruptor:
    def encender(self):
        pass

    def apagar(self):
        pass

class InterruptorLampara(AbstractInterruptor):
    def encender(self):
        print("Lámpara encendida")

    def apagar(self):
        print("Lámpara apagada")

class Lampara:
    def __init__(self, interruptor: AbstractInterruptor):
        self.interruptor = interruptor

    def utilizar(self, accion):
        if accion == "on":
            self.interruptor.encender()
        elif accion == "off":
            self.interruptor.apagar()

# Uso de la clase Lampara con el interruptor
interruptor = Lampara(InterruptorLampara())
interruptor.utilizar("on")
interruptor.utilizar("off")

# En este ejemplo, la clase Lampara no depende de una implementación concreta del interruptor. Puede trabajar con cualquier clase que implemente la interfaz AbstractInterruptor.