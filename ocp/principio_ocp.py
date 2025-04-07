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

class Plan:
    def calcular_comision(self, monto):
        raise NotImplementedError

class PlanNormal(Plan):
    def calcular_comision(self, monto):
        return monto * 0.1

class PlanPrime(Plan):
    def calcular_comision(self, monto):
        return monto * 0.01
    
def procesar_comision(plan: Plan, monto: float):
    return plan.calcular_comision(monto)

normal = PlanNormal()
prime = PlanPrime()

print(procesar_comision(normal, 1000.3))
print(procesar_comision(prime, 1000))