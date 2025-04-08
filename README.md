# Principios Solid
Proyecto con la finalidad de comprender los Principios Solid, con ejemplos de buenas prácticas y malas.

## 📚 Descripción

La finalidad de este repositorio es comprender los Principios Solid mediante un ejemplo para cada uno de ellos. El lenguaje de programación utilizado para ralizar estos ejemplo va a ser Python. Los principios SOLID son un conjunto de **cinco principios de diseño** destinados a escribir software más limpio, mantenible y escalable. Fueron popularizados por **Robert C. Martin (Uncle Bob)** y son ampliamente utilizados en el desarrollo orientado a objetos.

---

## 📐 Principios SOLID

### 1. **S – Single Responsibility Principle (SRP)**

> *"Una clase debe tener una única razón para cambiar."*

Cada clase debe encargarse de **una sola responsabilidad** o funcionalidad del sistema. Separar responsabilidades hace que el código sea más fácil de entender, probar y mantener.

---

### 2. **O – Open/Closed Principle (OCP)**

> *"Las entidades de software deben estar abiertas para extensión, pero cerradas para modificación."*

El diseño debe permitir **agregar nuevas funcionalidades sin modificar el código existente**, usando abstracciones y polimorfismo.

---

### 3. **L – Liskov Substitution Principle (LSP)**

> *"Los objetos de una subclase deben poder sustituir a los de la clase base sin alterar el comportamiento del programa."*

Las clases hijas deben comportarse como sus clases padres, respetando su contrato. No deben romper la lógica si se usan en lugar de sus padres.

---

### 4. **I – Interface Segregation Principle (ISP)**

> *"Ningún cliente debe estar obligado a depender de interfaces que no usa."*

Es mejor tener muchas **interfaces pequeñas y específicas** que una sola grande con métodos innecesarios para algunos objetos.

---

### 5. **D – Dependency Inversion Principle (DIP)**

> *"Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones."*

Se debe **depender de interfaces y no de implementaciones concretas**, promoviendo el desacoplamiento entre componentes.

## 🧰 Tecnologías utilizadas

- Python 3.13
