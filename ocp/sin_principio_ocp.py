# A continuación vamos a ver un ejemplo de clase sin utilizar el principio Abierto/Cerrado (OCP). Para ello vamos
# a crear una calculadora de comisiones de los clientes en función del plan que tengan, como se hace en el
# fichero ocp/principio_ocp.py donde si se aplica el principio OCP.

class Cliente:
    def __init__(self, plan: str, id_usuario: int, monto: float):
        self.plan = plan
        self.id_usuario = id_usuario
        self.monto = monto

class CalculadoraComisiones:
    def calcular_comision(self, cliente: Cliente):
        if cliente.plan == "estandar":
            return cliente.monto * 0.1
        elif cliente.plan == "premium":
            return cliente.monto * 0.02
        

cliente1 = Cliente("estandar", 1, 10000)
cliente2 = Cliente("premium", 2, 20000)

calculadora = CalculadoraComisiones()

print(f"Comisión cliente 1: {calculadora.calcular_comision(cliente1)}")
print(f"Comisión cliente 2: {calculadora.calcular_comision(cliente2)}")

# Si en el futuro se agregan nuevos tipos de clientes, como clientes VIP, será necesario modificar la clase CalculadoraComisiones para
# incluir la nueva lógica de cálculo de comisiones, lo que va en contra del principio OCP. Aun que en este ejemplo es sencillo y rapido de
# implementar, en sistemas grandes y complejos puede ser muy costoso y propenso a errores.