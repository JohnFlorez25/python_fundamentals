# Introducción a la Programación Orientada a Objetos en Python

## El Mundo a Través de Objetos

Imagina que estás en una biblioteca. En ella encuentras libros, estantes, lectores, bibliotecarios y tarjetas de préstamo. Cada uno de estos elementos tiene características propias (como el título de un libro o el nombre de un lector) y puede realizar ciertas acciones (como prestar un libro o registrar un nuevo lector). La Programación Orientada a Objetos (POO) nos permite modelar este mundo en código de una manera natural y organizada.

## ¿Qué es una Clase?

Una clase es como un plano o una plantilla que define qué características (atributos) y qué acciones (métodos) tendrá un tipo específico de objeto. Piensa en ella como la receta para crear algo.

### Ejemplo: Creando una Clase Libro

```python
class Libro:
    """
    Esta clase representa un libro en una biblioteca.
    Contiene información básica sobre el libro y métodos para gestionarlo.
    """
    
    # El método __init__ es el constructor de la clase
    def __init__(self, titulo, autor, isbn):
        # Atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.fecha_prestamo = None
    
    # Método para prestar el libro
    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.fecha_prestamo = "2024-02-01"  # Simplificado para el ejemplo
            return True
        return False
    
    # Método para devolver el libro
    def devolver(self):
        self.disponible = True
        self.fecha_prestamo = None

# Creando un objeto libro (instancia de la clase)
mi_libro = Libro("Don Quijote", "Miguel de Cervantes", "978-84-376-0494-7")
```

### Anatomía de una Clase

1. **Definición de la Clase**: Usando la palabra clave `class`
2. **Constructor**: El método `__init__` que se llama al crear un nuevo objeto
3. **Atributos**: Variables que almacenan datos del objeto
4. **Métodos**: Funciones que definen el comportamiento del objeto

## Objetos: Las Instancias de una Clase

Un objeto es una instancia específica de una clase. Si la clase Libro es la receta, un objeto libro es el pastel que hemos horneado siguiendo esa receta.

```python
# Creando varios objetos de la clase Libro
libro_quijote = Libro("Don Quijote", "Miguel de Cervantes", "978-84-376-0494-7")
libro_rayuela = Libro("Rayuela", "Julio Cortázar", "978-84-376-0494-8")

# Cada objeto tiene sus propios atributos
print(libro_quijote.titulo)  # Don Quijote
print(libro_rayuela.titulo)  # Rayuela

# Y puede usar sus métodos de forma independiente
libro_quijote.prestar()  # Este libro está prestado
libro_rayuela.prestar()  # Este otro también
```

## Atributos: Las Características de los Objetos

Los atributos son variables que pertenecen a un objeto y almacenan sus características o estado.

### Ejemplo: Clase Estudiante con Diferentes Tipos de Atributos

```python
class Estudiante:
    # Atributo de clase (compartido por todas las instancias)
    escuela = "Instituto Técnico"
    
    def __init__(self, nombre, edad, grado):
        # Atributos de instancia (únicos para cada estudiante)
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.notas = []  # Lista vacía para almacenar notas
        
    def agregar_nota(self, nota):
        """Agrega una nueva nota al estudiante."""
        if 0 <= nota <= 5:
            self.notas.append(nota)
            return True
        return False
    
    def calcular_promedio(self):
        """Calcula el promedio de notas del estudiante."""
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

# Creando estudiantes
estudiante1 = Estudiante("Ana García", 15, "10A")
estudiante2 = Estudiante("Carlos López", 16, "10B")

# Usando atributos y métodos
estudiante1.agregar_nota(4.5)
estudiante1.agregar_nota(4.0)
print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")
```

## Métodos: El Comportamiento de los Objetos

Los métodos son funciones que pertenecen a una clase y definen qué pueden hacer los objetos de esa clase.

### Tipos de Métodos

```python
class CuentaBancaria:
    tasa_interes = 0.05  # Atributo de clase
    
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []
    
    # Método de instancia
    def depositar(self, cantidad):
        """Realiza un depósito en la cuenta."""
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append(f"Depósito: +{cantidad}")
            return True
        return False
    
    # Método de instancia que usa atributo de clase
    def aplicar_interes(self):
        """Aplica la tasa de interés al saldo."""
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        self.movimientos.append(f"Interés aplicado: +{interes}")
    
    # Método estático (no necesita acceder a self)
    @staticmethod
    def validar_monto(monto):
        """Valida si un monto es válido."""
        return monto > 0 and isinstance(monto, (int, float))
    
    # Método de clase (puede acceder a atributos de clase)
    @classmethod
    def modificar_tasa_interes(cls, nueva_tasa):
        """Modifica la tasa de interés para todas las cuentas."""
        if 0 < nueva_tasa < 1:
            cls.tasa_interes = nueva_tasa
            return True
        return False
```

## Ejemplo Práctico: Sistema de Biblioteca

Veamos cómo todos estos conceptos se juntan en un ejemplo más completo:

```python
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.prestamos = {}
    
    def agregar_libro(self, libro):
        """Agrega un nuevo libro a la biblioteca."""
        self.libros.append(libro)
    
    def buscar_libro(self, isbn):
        """Busca un libro por su ISBN."""
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None
    
    def prestar_libro(self, isbn, lector):
        """Presta un libro a un lector."""
        libro = self.buscar_libro(isbn)
        if libro and libro.disponible:
            libro.prestar()
            self.prestamos[isbn] = lector
            return True
        return False
    
    def devolver_libro(self, isbn):
        """Procesa la devolución de un libro."""
        libro = self.buscar_libro(isbn)
        if libro and not libro.disponible:
            libro.devolver()
            del self.prestamos[isbn]
            return True
        return False

# Uso del sistema
biblioteca = Biblioteca("Biblioteca Municipal")

# Agregando libros
libro1 = Libro("Don Quijote", "Cervantes", "001")
libro2 = Libro("Rayuela", "Cortázar", "002")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Prestando libros
biblioteca.prestar_libro("001", "Ana García")
print(f"¿Está disponible Don Quijote? {libro1.disponible}")
```

## Conceptos Clave para Recordar

1. **Clase**: Es la plantilla o plano que define las características y comportamientos de un tipo de objeto.

2. **Objeto**: Es una instancia específica de una clase, con sus propios valores para los atributos.

3. **Atributos**: Son las variables que almacenan datos dentro de un objeto.
   - Atributos de instancia: Únicos para cada objeto
   - Atributos de clase: Compartidos por todos los objetos de la clase

4. **Métodos**: Son las funciones que definen qué puede hacer un objeto.
   - Métodos de instancia: Operan sobre atributos específicos del objeto
   - Métodos de clase: Operan sobre la clase en general
   - Métodos estáticos: Funciones utilitarias relacionadas con la clase

## Ejercicios Prácticos

Para practicar estos conceptos, intenta:

1. Agregar más funcionalidades a la clase Libro:
   - Método para renovar un préstamo
   - Atributo para tracking de historia de préstamos
   - Método para calcular multas por retraso

2. Expandir la clase Estudiante:
   - Agregar manejo de múltiples materias
   - Implementar cálculo de promedio por materia
   - Agregar sistema de asistencia

3. Crear nuevas clases para el sistema de biblioteca:
   - Clase Lector con historial de préstamos
   - Clase Préstamo para manejar las transacciones
   - Clase Multa para gestionar penalizaciones

## Consejos para Programar con POO

1. Planifica tus clases antes de comenzar a programar
2. Mantén las responsabilidades de cada clase bien definidas
3. Utiliza nombres descriptivos para clases, atributos y métodos
4. Documenta tu código usando docstrings y comentarios
5. Sigue el principio de encapsulamiento (próximo tema)