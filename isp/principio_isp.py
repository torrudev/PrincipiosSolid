###
# ISP (Interface Segregation Principle) - Principio de Segregación de Interfaces
# El principio de segregación de interfaces establece que los clientes no deben verse obligados a depender de interfaces que no utilizan. En otras palabras,
# es mejor tener varias interfaces específicas y pequeñas en lugar de una única interfaz grande con métodos innecesarios para algunos objetos.
###

# Este ejemplo plasma el ISP al definir interfaces específicas para las operaciones de impresión, escaneo y fax.
# En lugar de tener una única interfaz grande que obligue a las clases a implementar métodos que no necesitan, se crean interfaces separadas para cada funcionalidad.
class Impresora:
    def imprimir(self, documento):
        pass

class Escaner:
    def escanear(self, documento):
        pass

class Fax:
    def enviar_fax(self, documento):
        pass

# Implementar solo lo necesario para impresora básica
class ImpresoraBasica(Impresora):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")

# Implementar los métodos necesarios para impresora multifuncion
# que hereda de las interfaces Impresora, Escaner y Fax.
class ImpresoraMultifuncion(Impresora, Escaner, Fax):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")

    def escanear(self, documento):
        print(f"Escaneando: {documento}")

    def enviar_fax(self, documento):
        print(f"Enviando fax: {documento}")