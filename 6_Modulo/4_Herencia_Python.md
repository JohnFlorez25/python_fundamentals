# Herencia en Python

## Introducción a la Herencia

La herencia es uno de los pilares fundamentales de la programación orientada a objetos. Podemos pensar en ella como la forma en que las características y comportamientos se transmiten de padres a hijos en la naturaleza. En programación, nos permite crear nuevas clases basadas en clases existentes, heredando sus atributos y métodos.

## Conceptos Básicos de Herencia

### Herencia Simple

Comencemos con un ejemplo básico del mundo animal:

```python
class Animal:
    """Clase base que representa a un animal genérico."""
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.energia = 100
    
    def comer(self):
        self.energia += 25
        return f"{self.nombre} está comiendo. Energía: {self.energia}"
    
    def dormir(self):
        self.energia = 100
        return f"{self.nombre} está durmiendo. Energía restaurada"
    
    def moverse(self):
        if self.energia >= 10:
            self.energia -= 10
            return f"{self.nombre} se está moviendo. Energía: {self.energia}"
        return f"{self.nombre} está muy cansado para moverse"

class Perro(Animal):
    """Clase que hereda de Animal y representa a un perro."""
    
    def __init__(self, nombre, edad, raza):
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, edad)
        # Agregamos atributos específicos de Perro
        self.raza = raza
    
    def ladrar(self):
        self.energia -= 5
        return f"¡Guau! Energía: {self.energia}"
    
    # Sobrescribimos el método moverse para hacerlo específico
    def moverse(self):
        if self.energia >= 15:
            self.energia -= 15
            return f"{self.nombre} está corriendo y moviendo la cola. Energía: {self.energia}"
        return f"{self.nombre} está muy cansado para correr"

# Ejemplo de uso
mi_perro = Perro("Max", 3, "Labrador")
print(mi_perro.comer())       # Método heredado
print(mi_perro.ladrar())      # Método propio
print(mi_perro.moverse())     # Método sobrescrito
```

### Herencia Múltiple

Python permite que una clase herede de múltiples clases padre. Veamos un ejemplo con dispositivos electrónicos:

```python
class DispositivoElectronico:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def encender(self):
        if not self.encendido:
            self.encendido = True
            return "Dispositivo encendido"
        return "Ya está encendido"
    
    def apagar(self):
        if self.encendido:
            self.encendido = False
            return "Dispositivo apagado"
        return "Ya está apagado"

class DispositivoConectado:
    def __init__(self):
        self.conectado = False
        self.red = None
    
    def conectar(self, red):
        self.conectado = True
        self.red = red
        return f"Conectado a {red}"
    
    def desconectar(self):
        self.conectado = False
        self.red = None
        return "Desconectado"

class Smartphone(DispositivoElectronico, DispositivoConectado):
    def __init__(self, marca, modelo):
        DispositivoElectronico.__init__(self, marca, modelo)
        DispositivoConectado.__init__(self)
        self.bateria = 100
    
    def usar_aplicacion(self):
        if not self.encendido:
            return "El dispositivo está apagado"
        if not self.conectado:
            return "No hay conexión a internet"
        
        self.bateria -= 10
        return f"Usando aplicación. Batería: {self.bateria}%"

# Ejemplo de uso
mi_telefono = Smartphone("Samsung", "Galaxy")
print(mi_telefono.encender())          # De DispositivoElectronico
print(mi_telefono.conectar("WiFi"))    # De DispositivoConectado
print(mi_telefono.usar_aplicacion())   # Método propio
```

## Herencia Jerárquica y Multinivel

Veamos un ejemplo más complejo con un sistema de empleados:

```python
class Persona:
    """Clase base para representar una persona."""
    
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def obtener_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

class Empleado(Persona):
    """Clase que representa un empleado genérico."""
    
    def __init__(self, nombre, edad, dni, id_empleado, salario):
        super().__init__(nombre, edad, dni)
        self.id_empleado = id_empleado
        self.salario = salario
        self.activo = True
    
    def calcular_salario(self):
        return self.salario
    
    def obtener_info(self):
        info_base = super().obtener_info()
        return f"{info_base}, ID: {self.id_empleado}, Salario: ${self.salario}"

class Desarrollador(Empleado):
    """Clase que representa un desarrollador."""
    
    def __init__(self, nombre, edad, dni, id_empleado, salario, lenguajes):
        super().__init__(nombre, edad, dni, id_empleado, salario)
        self.lenguajes = lenguajes
        self.proyectos = []
    
    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)
    
    def calcular_salario(self):
        # Bonus por proyecto
        salario_base = super().calcular_salario()
        bonus_proyectos = len(self.proyectos) * 100
        return salario_base + bonus_proyectos

class GerenteProyecto(Empleado):
    """Clase que representa un gerente de proyecto."""
    
    def __init__(self, nombre, edad, dni, id_empleado, salario):
        super().__init__(nombre, edad, dni, id_empleado, salario)
        self.equipo = []
    
    def agregar_miembro(self, empleado):
        if isinstance(empleado, Desarrollador):
            self.equipo.append(empleado)
            return f"{empleado.nombre} agregado al equipo"
        return "Solo se pueden agregar desarrolladores al equipo"
    
    def calcular_salario(self):
        # Bonus por tamaño del equipo
        salario_base = super().calcular_salario()
        bonus_equipo = len(self.equipo) * 200
        return salario_base + bonus_equipo
```

## Patrones Comunes y Mejores Prácticas

### 1. Composición sobre Herencia

A veces es mejor usar composición en lugar de herencia:

```python
class Motor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.temperatura = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        self.temperatura += 10
    
    def apagar(self):
        self.encendido = False
        self.temperatura = 0

class Auto:
    def __init__(self, marca, modelo, tipo_motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(tipo_motor)  # Composición
    
    def arrancar(self):
        self.motor.encender()
        return f"Auto {self.marca} arrancado"
```

### 2. Métodos Abstractos

Usando el módulo abc para crear clases abstractas:

```python
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio
```

## Ejemplo Práctico: Sistema de Gestión de Biblioteca

```python
class Recurso:
    """Clase base para recursos de biblioteca."""
    
    def __init__(self, titulo, codigo, ubicacion):
        self.titulo = titulo
        self.codigo = codigo
        self.ubicacion = ubicacion
        self.prestado = False
        self.fecha_prestamo = None
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            self.fecha_prestamo = "2024-02-01"  # Simplificado
            return f"{self.titulo} prestado"
        return "Ya está prestado"
    
    def devolver(self):
        if self.prestado:
            self.prestado = False
            self.fecha_prestamo = None
            return f"{self.titulo} devuelto"
        return "No estaba prestado"

class Libro(Recurso):
    def __init__(self, titulo, codigo, ubicacion, autor, isbn):
        super().__init__(titulo, codigo, ubicacion)
        self.autor = autor
        self.isbn = isbn
        self.num_paginas = None
    
    def obtener_info(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro: {self.titulo} por {self.autor} ({estado})"

class Revista(Recurso):
    def __init__(self, titulo, codigo, ubicacion, numero, mes):
        super().__init__(titulo, codigo, ubicacion)
        self.numero = numero
        self.mes = mes
    
    def obtener_info(self):
        return f"Revista: {self.titulo} - Número {self.numero}"

class DVD(Recurso):
    def __init__(self, titulo, codigo, ubicacion, duracion):
        super().__init__(titulo, codigo, ubicacion)
        self.duracion = duracion
    
    def obtener_info(self):
        return f"DVD: {self.titulo} ({self.duracion} minutos)"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.recursos = []
    
    def agregar_recurso(self, recurso):
        if isinstance(recurso, Recurso):
            self.recursos.append(recurso)
            return f"Recurso {recurso.titulo} agregado"
        return "Tipo de recurso no válido"
    
    def buscar_recurso(self, codigo):
        for recurso in self.recursos:
            if recurso.codigo == codigo:
                return recurso
        return None
    
    def listar_recursos(self):
        return [recurso.obtener_info() for recurso in self.recursos]

# Ejemplo de uso
biblioteca = Biblioteca("Biblioteca Municipal")

libro = Libro("Don Quijote", "L001", "A1", "Cervantes", "123456")
revista = Revista("National Geographic", "R001", "B2", 123, "Enero")
dvd = DVD("El Padrino", "D001", "C3", 175)

biblioteca.agregar_recurso(libro)
biblioteca.agregar_recurso(revista)
biblioteca.agregar_recurso(dvd)

print("\nRecursos en biblioteca:")
for info in biblioteca.listar_recursos():
    print(info)

recurso = biblioteca.buscar_recurso("L001")
if recurso:
    print(recurso.prestar())
    print(recurso.obtener_info())
```

## Consejos y Mejores Prácticas

1. **Utilizar super() correctamente**:
   - Siempre llamar al constructor de la clase padre
   - Mantener el orden correcto en herencia múltiple

2. **Principio de Sustitución de Liskov**:
   - Una clase derivada debe poder usarse en lugar de su clase base

3. **Evitar herencia profunda**:
   - No más de 2-3 niveles de herencia
   - Preferir composición cuando sea apropiado

4. **Documentar la herencia**:
   - Explicar la relación entre clases
   - Documentar métodos sobrescritos

## Ejercicios Prácticos

1. **Sistema de Vehículos**:
   - Implementar una jerarquía de vehículos
   - Incluir diferentes tipos (coche, moto, camión)
   - Añadir métodos específicos para cada tipo

2. **Sistema de Empleados**:
   - Expandir el ejemplo de empleados
   - Agregar más tipos de empleados
   - Implementar cálculo de salarios específico

3. **Sistema de Formas**:
   - Crear una jerarquía de formas geométricas
   - Implementar cálculos de área y perímetro
   - Añadir visualización de formas

## Conclusión

La herencia es una herramienta poderosa en POO que nos permite:
1. Reutilizar código eficientemente
2. Crear jerarquías lógicas de clases
3. Implementar comportamientos específicos
4. Mantener el código organizado y mantenible

La clave es usarla con moderación y entender cuándo la composición puede ser una mejor alternativa.