#  * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
#  * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
#  * y el procesamiento de préstamos de libros.
#  * Requisitos:
#  *    1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
#  *    información básica como título, autor y número de copias disponibles.
#  *    2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
#  *    información básica como nombre, número de identificación y correo electrónico.
#  *    3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
#  *    tomar prestados y devolver libros.

import logging

# logging es un módulo de Python que permite registrar mensajes de log durante la ejecución de un programa.
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", handlers=[logging.StreamHandler()])

# level define el nivel mínimo de mensajes que se registrarán. En este caso, se registrarán mensajes de nivel DEBUG y superiores.
# format define el formato de los mensajes de log. En este caso, se incluye la fecha y hora, el nivel del mensaje y el mensaje en sí.
# handlers define dónde se enviarán los mensajes de log. En este caso, se enviarán a la consola (StreamHandler).

class Usuario:
    def __init__(self, nombre: str, id_usuario: int, correo: str):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.correo = correo

    def __str__(self):
        return f"({self.id_usuario})Usuario: {self.nombre}, Correo: {self.correo}"
    
class Libro:
    def __init__(self, titulo: str, autor: str, copias: int):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

    def __str__(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Copias disponibles: {self.copias}"

class Prestamo:
    def __init__(self):
        self.prestramos = []

    def prestar_libro(self, usuario: Usuario, libro: Libro):
        if libro.copias > 0:
            libro.copias -= 1
            self.prestramos.append({"usuarioID": usuario.id_usuario, "tituloLibro": libro.titulo})
            return True
        return False
    
    def devolver_libro(self, usuario: Usuario, libro: Libro):
        for prestamo in self.prestramos:
            if prestamo["usuarioID"] == usuario.id_usuario and prestamo["tituloLibro"] == libro.titulo:
                libro.copias += 1
                self.prestramos.remove(prestamo)
                return True
        return False
    
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.servicio_prestamos = Prestamo()

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        logging.debug(f"Libro agregado: {libro}")

    def agregar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        logging.debug(f"Usuario agregado: {usuario}")

    def prestar_libro(self, usuario_id: int, libro_titulo: str):
        usuario = next((u for u in self.usuarios if u.id_usuario == usuario_id), None)
        libro = next((l for l in self.libros if l.titulo == libro_titulo), None)

        if usuario and libro:
            if self.servicio_prestamos.prestar_libro(usuario, libro):
                logging.debug(f"Libro '{libro_titulo}' prestado a {usuario.nombre}.")
            else:
                logging.debug(f"No hay copias disponibles de '{libro_titulo}'.")
        else:
            logging.debug("Usuario o libro no encontrado.")

    def devolver_libro(self, usuario_id: int, libro_titulo: str):
        usuario = next((u for u in self.usuarios if u.id_usuario == usuario_id),None)
        libro = next((l for l in self.libros if l.titulo == libro_titulo), None)

        if usuario and libro:
            if self.servicio_prestamos.devolver_libro(usuario, libro):
                logging.debug(f"Libro '{libro_titulo}' devuelto por {usuario.nombre}.")
            else:
                logging.debug(f"El libro '{libro_titulo}' no fue prestado a {usuario.nombre}.")
        else:
            logging.debug("Usuario o libro no encontrado.")

# Crear una instancia de la biblioteca
biblioteca = Biblioteca()

# Crear algunos libros y usuarios
libro1 = Libro("El cuco de cristal", "Javier Castillo", 12)
libro2 = Libro("La chica del tren", "Paula Hawkins", 12)
libro3 = Libro("Cien años de soledad", "Gabriel García Márquez", 1)

usuario1 = Usuario("Jesus Garcia", 1, "garciaj@gmail.com")
usuario2 = Usuario("Yolanda Fernandez", 2, "yoliFaez@gmail.com")

# Agregar libros y usuarios a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_usuario(usuario1)
biblioteca.agregar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro(1, "El cuco de cristal")
biblioteca.prestar_libro(2, "Cien años de soledad")
biblioteca.prestar_libro(2, "La chica del tren")

print(f"Libros prestados: {biblioteca.servicio_prestamos.prestramos}")

# Devolver libros
biblioteca.devolver_libro(2, "El cuco de cristal")
biblioteca.devolver_libro(2, "Cien años de soledad")

print(f"Libros prestados: {biblioteca.servicio_prestamos.prestramos}")