###
# OCP (Open/Close Principle o Principio Abierto/Cerrado)
# Las entidades de software (clases, módulos, funciones, etc.) deben estar abiertas para su extensión, pero cerradas para su modificación. Que quiere decir esto:
#   - Abierto a extension: Se pueden agregar nuevas funcionalidades sin modificar el código existente.
#   - Cerrado a modificación: No necesita alterar el código que ya funciona para adaptarse a nuevos requerimientos.

# La forma de llegar a cumplir este principio esta muy relacionada con el principio de responsabilidad única (SRP), aunque decir
# que se cumple el OCP no significa que se cumpla el SRP y viceversa. El principio OCP se puede cumplir de varias formas, 
# pero una de las más comunes es a través de la herencia/polimorfismo.

# SEÑAL DE QUE NO ESTAMOS CUMPLIENDO EL OCP:
#   - Si cada vez que hay un nuevo requisito o una modificación, las mismas clases se ven afectadas, podemos empezar a entender que se
#   está violando este principio
###

# Este ejemplo ilustra el principio OCP al permitir que se agreguen nuevos planes de comisiones sin modificar el código existente.
# En este ejemplo estarán los clientes estandar que tienen una comision general del 10% y los clientes premium que tienen una comision del 2%.
# Si en el futuro se agregan nuevos tipos de clientes, como clientes VIP, no será necesario modificar la clase base Cliente, sino que simplemente
# se puede crear una nueva clase que herede de Cliente y sobrescriba el método calcular_comision con el nuevo porcentaje de comisión deseado.

class Cliente:
    def __init__(self, nombre: str, id_usuario: int, monto: float):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.monto = monto

    def calcular_comision(self):
        # Comision general del 10%
        return self.monto * 0.1

class ClientePremium(Cliente):
    def calcular_comision(self):
        # Comision del 1%
        return self.monto * 0.02
    
class Impresora:
    def imprimir_comision(self, cliente: Cliente):
        print(f"El cliente {cliente.nombre} tiene una comision de {cliente.calcular_comision()}")

impresora = Impresora()

# Crear clientes de diferentes tipos
clientes = [
    Cliente("Juan", 1, 10000),
    Cliente("Maria", 2, 20000),
    ClientePremium("Pedro", 3, 17000)
]

for c in clientes:
    impresora.imprimir_comision(c)

# Añadir un nuevo tipo de cliente (ClienteVIP) sin modificar el código existente.
# Esto es una extensión del código, no una modificación.
class ClienteVIP(Cliente):
    def calcular_comision(self):
        # Comision del 1%
        return self.monto * 0.01
    
# Crear clientes con el nuevo tipo ClienteVIP
clientes2 = [
    Cliente("Juan", 1, 10000),
    Cliente("Maria", 2, 20000),
    ClientePremium("Pedro", 3, 17000),
    ClienteVIP("Teresa", 4, 18000)
]

for c in clientes2:
    impresora.imprimir_comision(c)