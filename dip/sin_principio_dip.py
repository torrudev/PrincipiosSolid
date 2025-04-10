# Ahora vamos a ver un ejemplo en el que NO aplicamos el Principio de Inversión de Dependencias (DIP).
# Para ellos vamos a crear una clase Lámpara que depende directamente de una clase Interruptor.
# La forma correcta de hacerlo se encuentra en el archivo dip/principio_dip.py.

# En este ejemplo, la clase Lampara depende directamente de la clase Interruptor. Si queremos cambiar la implementación del interruptor, tendremos que modificar la clase Lampara.
class Interruptor:
    def encender(self):
        print("Lámpara encendida")

    def apagar(self):
        print("Lámpara apagada")

class Lampara:
    def __init__(self):
        self.interruptor = Interruptor()

    def utilizar(self, accion):
        if accion == "on":
            self.interruptor.encender()
        elif accion == "off":
            self.interruptor.apagar()

lampara = Lampara()
lampara.utilizar("on")
lampara.utilizar("off")