# Métodos de Instancia en Python: Una Exploración Profunda

## Introducción a los Métodos de Instancia

Cuando programamos orientado a objetos en Python, los métodos de instancia son como las habilidades o acciones que cada objeto puede realizar. Si pensamos en una persona como un objeto, caminar, hablar o comer serían métodos de instancia - acciones que cada persona puede realizar de manera individual.

### ¿Qué es un Método de Instancia?

Un método de instancia es una función que pertenece a un objeto específico (una instancia de una clase) y puede acceder y modificar los atributos de ese objeto. Estos métodos siempre reciben `self` como primer parámetro, que es una referencia al objeto que está llamando al método.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):  # Este es un método de instancia
        """Este método usa los atributos del objeto para crear un saludo personalizado."""
        return f"¡Hola! Me llamo {self.nombre} y tengo {self.edad} años."
    
    def cumplir_anios(self):  # Otro método de instancia
        """Este método modifica un atributo del objeto."""
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años."

# Creando y usando una instancia
ana = Persona("Ana", 25)
print(ana.saludar())        # ¡Hola! Me llamo Ana y tengo 25 años.
print(ana.cumplir_anios())  # ¡Feliz cumpleaños! Ahora tengo 26 años.
```

## Características de los Métodos de Instancia

### 1. Acceso a Atributos del Objeto

Los métodos de instancia pueden acceder y modificar los atributos del objeto usando `self`:

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []
    
    def depositar(self, cantidad):
        """Método que modifica el saldo y registra el movimiento."""
        if cantidad > 0:
            self.saldo += cantidad
            self.movimientos.append(f"Depósito: +{cantidad}")
            return f"Depósito exitoso. Nuevo saldo: {self.saldo}"
        return "La cantidad debe ser positiva"
    
    def consultar_movimientos(self):
        """Método que accede a los atributos sin modificarlos."""
        return f"Movimientos de {self.titular}:\n" + "\n".join(self.movimientos)
```

### 2. Interacción entre Métodos

Los métodos de instancia pueden llamarse entre sí usando `self`:

```python
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []
    
    def agregar_nota(self, nota):
        """Agrega una nueva nota y actualiza el promedio."""
        if 0 <= nota <= 5:
            self.notas.append(nota)
            return self.calcular_estado()  # Llamada a otro método
        return "Nota no válida"
    
    def calcular_promedio(self):
        """Calcula el promedio de notas."""
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def calcular_estado(self):
        """Determina el estado basado en el promedio."""
        promedio = self.calcular_promedio()  # Llamada a otro método
        if promedio >= 3:
            return f"Aprobado con {promedio}"
        return f"Reprobado con {promedio}"
```

### 3. Validaciones y Lógica de Negocio

Los métodos de instancia pueden incluir validaciones complejas y lógica de negocio:

```python
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.ventas = []
    
    def realizar_venta(self, cantidad):
        """Método con validaciones y lógica de negocio."""
        if not self._validar_cantidad(cantidad):
            return "Cantidad no válida"
        
        if not self._verificar_stock(cantidad):
            return "Stock insuficiente"
        
        valor_venta = self._calcular_valor(cantidad)
        self._actualizar_stock(cantidad)
        self._registrar_venta(cantidad, valor_venta)
        
        return f"Venta exitosa por ${valor_venta}"
    
    def _validar_cantidad(self, cantidad):
        """Método privado para validación."""
        return isinstance(cantidad, int) and cantidad > 0
    
    def _verificar_stock(self, cantidad):
        """Método privado para verificar disponibilidad."""
        return self.stock >= cantidad
    
    def _calcular_valor(self, cantidad):
        """Método privado para cálculos."""
        return self.precio * cantidad
    
    def _actualizar_stock(self, cantidad):
        """Método privado para actualizar estado."""
        self.stock -= cantidad
    
    def _registrar_venta(self, cantidad, valor):
        """Método privado para registro."""
        self.ventas.append({
            "cantidad": cantidad,
            "valor": valor,
            "fecha": "2024-02-01"  # Simplificado para el ejemplo
        })
```

## Patrones Comunes en Métodos de Instancia

### 1. Métodos de Acceso (Getters)

```python
class Empleado:
    def __init__(self, nombre, salario):
        self._nombre = nombre    # Atributo protegido
        self._salario = salario  # Atributo protegido
    
    def obtener_nombre(self):
        """Getter para el nombre."""
        return self._nombre
    
    def obtener_salario(self):
        """Getter para el salario."""
        return self._salario
    
    def obtener_info_completa(self):
        """Getter que combina información."""
        return {
            "nombre": self._nombre,
            "salario": self._salario,
            "salario_anual": self._calcular_salario_anual()
        }
    
    def _calcular_salario_anual(self):
        """Método privado para cálculos internos."""
        return self._salario * 12
```

### 2. Métodos de Modificación (Setters)

```python
class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
        self._prestado = False
    
    def cambiar_estado_prestamo(self, nuevo_estado):
        """Setter con validación."""
        if not isinstance(nuevo_estado, bool):
            raise ValueError("El estado debe ser un booleano")
        self._prestado = nuevo_estado
        return "Estado actualizado"
    
    def actualizar_informacion(self, **kwargs):
        """Setter múltiple con validaciones."""
        cambios_realizados = []
        
        if "titulo" in kwargs:
            self._titulo = kwargs["titulo"]
            cambios_realizados.append("título")
            
        if "autor" in kwargs:
            self._autor = kwargs["autor"]
            cambios_realizados.append("autor")
        
        return f"Se actualizó: {', '.join(cambios_realizados)}"
```

### 3. Métodos de Estado

```python
class TareaProyecto:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = "pendiente"
        self.fecha_inicio = None
        self.fecha_fin = None
        self.comentarios = []
    
    def iniciar(self):
        """Cambia el estado de la tarea a 'en progreso'."""
        if self.estado != "pendiente":
            return "La tarea ya fue iniciada"
        
        self.estado = "en progreso"
        self.fecha_inicio = "2024-02-01"  # Simplificado
        return "Tarea iniciada"
    
    def completar(self):
        """Marca la tarea como completada."""
        if self.estado == "completada":
            return "La tarea ya está completada"
        
        self.estado = "completada"
        self.fecha_fin = "2024-02-01"  # Simplificado
        return "Tarea completada"
    
    def agregar_comentario(self, comentario):
        """Agrega un comentario a la tarea."""
        self.comentarios.append({
            "texto": comentario,
            "fecha": "2024-02-01",
            "estado_tarea": self.estado
        })
        return "Comentario agregado"
    
    def obtener_estado_actual(self):
        """Retorna un resumen del estado actual."""
        return {
            "descripcion": self.descripcion,
            "estado": self.estado,
            "tiempo_activa": self._calcular_tiempo_activa(),
            "num_comentarios": len(self.comentarios)
        }
    
    def _calcular_tiempo_activa(self):
        """Método privado para cálculos internos."""
        return "1 día"  # Simplificado para el ejemplo
```

## Mejores Prácticas

### 1. Nombres Descriptivos y Documentación

```python
class GestionInventario:
    def agregar_producto(self, producto, cantidad):
        """
        Agrega una cantidad específica de un producto al inventario.
        
        Args:
            producto (str): Nombre del producto a agregar
            cantidad (int): Cantidad a agregar
        
        Returns:
            str: Mensaje de confirmación
            
        Raises:
            ValueError: Si la cantidad es negativa
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        # ... resto del código
```

### 2. Principio de Responsabilidad Única

```python
# Mal ejemplo: Método que hace demasiado
def procesar_venta(self, producto, cantidad, cliente):
    # Validar stock
    # Calcular precio
    # Actualizar inventario
    # Generar factura
    # Enviar email
    # Actualizar estadísticas
    pass

# Buen ejemplo: Métodos con responsabilidades específicas
def validar_venta(self, producto, cantidad):
    """Valida si una venta es posible."""
    pass

def realizar_venta(self, producto, cantidad):
    """Procesa la venta y actualiza el inventario."""
    pass

def generar_factura(self, venta):
    """Genera la factura de una venta."""
    pass
```

### 3. Encapsulamiento Adecuado

```python
class GestionArchivos:
    def __init__(self, ruta):
        self._ruta = ruta
        self._archivo = None
    
    def procesar_archivo(self, operacion):
        """Método público que usa métodos privados."""
        try:
            self._abrir_archivo()
            resultado = self._realizar_operacion(operacion)
            return resultado
        finally:
            self._cerrar_archivo()
    
    def _abrir_archivo(self):
        """Método privado para manejo interno."""
        self._archivo = open(self._ruta, 'r')
    
    def _realizar_operacion(self, operacion):
        """Método privado para procesamiento."""
        pass
    
    def _cerrar_archivo(self):
        """Método privado para limpieza."""
        if self._archivo:
            self._archivo.close()
```

## Ejercicios Prácticos

### 1. Sistema de Gestión de Biblioteca

```python
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.prestamos = {}
    
    def agregar_libro(self, isbn, titulo, autor):
        """Agrega un nuevo libro al inventario."""
        pass
    
    def prestar_libro(self, isbn, lector):
        """Registra el préstamo de un libro."""
        pass
    
    def devolver_libro(self, isbn):
        """Procesa la devolución de un libro."""
        pass
    
    def obtener_estadisticas(self):
        """Genera estadísticas de la biblioteca."""
        pass
```

### 2. Sistema de Calificaciones

```python
class SistemaCalificaciones:
    def __init__(self):
        self.estudiantes = {}
        self.materias = {}
    
    def registrar_nota(self, estudiante, materia, nota):
        """Registra una nueva calificación."""
        pass
    
    def calcular_promedio_estudiante(self, estudiante):
        """Calcula el promedio de un estudiante."""
        pass
    
    def generar_reporte_curso(self):
        """Genera un reporte completo del curso."""
        pass
```

## Conclusión

Los métodos de instancia son fundamentales en la programación orientada a objetos en Python porque:

1. Permiten definir el comportamiento específico de cada objeto
2. Facilitan el encapsulamiento y la organización del código
3. Permiten la interacción controlada con los atributos del objeto
4. Facilitan la implementación de lógica de negocio compleja

La clave para escribir buenos métodos de instancia es:

1. Mantener una única responsabilidad por método
2. Documentar adecuadamente el comportamiento
3. Utilizar nombres descriptivos y claros
4. Implementar validaciones apropiadas
5. Mantener el encapsulamiento

Con una buena comprensión y aplicación de estos conceptos, podremos crear código más mantenible, reutilizable y robusto.