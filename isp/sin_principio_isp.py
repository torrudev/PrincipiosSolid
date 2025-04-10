# A continuación vamos a ver un ejemplo sin utilizar el Principio de Segregación de Interfaces (ISP).
# Para ello vamos a crear una interfaz de impresora que tiene métodos para imprimir, escanear y enviar fax.

class Impresora:
    def imprimir(self, documento):
        raise NotImplementedError("Método no implementado")

    def escanear(self, documento):
        raise NotImplementedError("Método no implementado")

    def enviar_fax(self, documento):
        raise NotImplementedError("Método no implementado")
    
class ImpresoraBasica(Impresora):
    def imprimir(self, documento):
        print(f"Imprimiendo: {documento}")

    def escanear(self, documento):
        raise Exception("Esta impresora no escanea.")
    
    def enviar_fax(self, documento):
        raise Exception("Esta impresora no envia fax.")
    
impresora_basica = ImpresoraBasica()

impresora_basica.imprimir("Documento 1")
impresora_basica.enviar_fax("Documento 2") # Esto lanzará una excepción porque la impresora básica no puede enviar fax.