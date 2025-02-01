# Tuplas en Python: Inmutabilidad y Eficiencia

## Introducción a las Tuplas

Las tuplas son estructuras de datos fundamentales en Python que se distinguen por su inmutabilidad - una vez creadas, sus elementos no pueden ser modificados. Esta característica aparentemente limitante es en realidad una de sus mayores fortalezas, proporcionando seguridad y eficiencia en muchos escenarios de programación.

## Creación de Tuplas

### Sintaxis Básica
```python
# Creación directa con paréntesis
coordenadas = (10, 20)
punto_3d = (1, 2, 3)

# Tupla sin paréntesis (empaquetado de tupla)
persona = "Juan", 25, "Medellín"

# Tupla de un solo elemento (requiere coma)
singleton = (42,)  # La coma es necesaria
no_tupla = (42)    # Esto es solo un número entre paréntesis

# Tupla vacía
vacia = ()
vacia_alternativa = tuple()
```

### Creación desde Otros Iterables
```python
# Desde una lista
lista_numeros = [1, 2, 3, 4]
tupla_numeros = tuple(lista_numeros)

# Desde un rango
tupla_rango = tuple(range(5))  # (0, 1, 2, 3, 4)

# Desde una cadena
tupla_caracteres = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

## Acceso a Elementos

### Indexación
```python
coordenadas = (10, 20, 30, 40, 50)

# Acceso por índice positivo
primer_elemento = coordenadas[0]    # 10
tercer_elemento = coordenadas[2]    # 30

# Acceso por índice negativo
ultimo_elemento = coordenadas[-1]   # 50
penultimo = coordenadas[-2]         # 40

# Slicing (rebanado)
sub_tupla = coordenadas[1:4]        # (20, 30, 40)
reversa = coordenadas[::-1]         # (50, 40, 30, 20, 10)
```

### Desempaquetado de Tuplas
```python
# Desempaquetado básico
punto = (3, 4)
x, y = punto

# Desempaquetado con * para capturar múltiples elementos
primero, *resto, ultimo = (1, 2, 3, 4, 5)
print(primero)  # 1
print(resto)    # [2, 3, 4]
print(ultimo)   # 5

# Intercambio de variables usando tuplas
a, b = 10, 20
a, b = b, a  # Intercambio elegante
```

## Ventajas Sobre Listas

### 1. Inmutabilidad y Seguridad
```python
# Las tuplas protegen datos que no deben cambiar
def calcular_area_triangulo(base, altura):
    dimensiones = (base, altura)  # Nadie puede modificar estos valores
    return (dimensiones[0] * dimensiones[1]) / 2

# Uso como claves de diccionarios (las listas no pueden ser claves)
coordenadas_valores = {(0, 0): "origen", (1, 1): "diagonal"}
```

### 2. Rendimiento
```python
import sys

# Comparación de memoria
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)

print(f"Tamaño lista: {sys.getsizeof(lista)} bytes")
print(f"Tamaño tupla: {sys.getsizeof(tupla)} bytes")

# Las tuplas son más rápidas para iterar
def sumar_elementos(contenedor):
    suma = 0
    for elemento in contenedor:  # Más rápido con tuplas
        suma += elemento
    return suma
```

### 3. Claridad de Intención
```python
# La tupla indica claramente que estos valores no deben cambiar
DIAS_SEMANA = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")

# Útil para retornar múltiples valores de una función
def obtener_dimensiones_pantalla():
    return (1920, 1080)  # Claramente comunica que son valores fijos
```

## Operaciones y Métodos

### Métodos Disponibles
```python
numeros = (1, 2, 2, 3, 2, 4)

# count(): Contar ocurrencias
conteo_doses = numeros.count(2)  # 3

# index(): Encontrar posición
posicion_tres = numeros.index(3)  # 3

# Operaciones de concatenación
tupla1 = (1, 2)
tupla2 = (3, 4)
concatenada = tupla1 + tupla2  # (1, 2, 3, 4)

# Repetición
repetida = tupla1 * 3  # (1, 2, 1, 2, 1, 2)
```

## Casos de Uso Prácticos

### 1. Retorno de Múltiples Valores
```python
def analizar_texto(texto):
    caracteres = len(texto)
    palabras = len(texto.split())
    lineas = texto.count('\n') + 1
    return (caracteres, palabras, lineas)

# Uso
texto = "Hola\nMundo"
cars, pals, lins = analizar_texto(texto)
```

### 2. Datos Inmutables en Colecciones
```python
# Registro de coordenadas GPS
registro_ubicaciones = [
    (4.7110, -74.0721, "Bogotá"),
    (3.4516, -76.5320, "Cali"),
    (6.2442, -75.5812, "Medellín")
]

# Nadie puede modificar accidentalmente las coordenadas
```

### 3. Nombrando Tuplas
```python
from collections import namedtuple

# Creando una "clase" simple e inmutable
Punto = namedtuple('Punto', ['x', 'y'])
p = Punto(11, y=22)

# Acceso por nombre o índice
print(p.x)    # 11
print(p[0])   # 11
```

## Tips y Mejores Prácticas

1. **Uso de Tuplas vs Listas**:
   ```python
   # Usar tuplas para datos heterogéneos
   persona = ("Juan", 25, "Ingeniero")  # ✓
   
   # Usar listas para datos homogéneos
   calificaciones = [85, 92, 78, 95]    # ✓
   ```

2. **Tuplas como Documentación**:
   ```python
   # Las tuplas pueden servir como documentación implícita
   def procesar_imagen(dimensiones):
     ancho, alto = dimensiones  # Claramente espera una tupla de 2 elementos
     return ancho * alto
   ```

3. **Rendimiento en Estructuras de Datos**:
   ```python
   # Usar tuplas en sets y como claves de diccionarios
   coordenadas = {(0, 0), (1, 1), (2, 2)}  # Set de tuplas
   ```

## Ejercicios Prácticos

1. **Sistema de Coordenadas**:
```python
def distancia_entre_puntos(punto1, punto2):
    """Calcula la distancia euclidiana entre dos puntos."""
    x1, y1 = punto1
    x2, y2 = punto2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Uso
p1 = (0, 0)
p2 = (3, 4)
print(f"Distancia: {distancia_entre_puntos(p1, p2)}")  # 5.0
```

2. **Registro de Temperaturas**:
```python
def analizar_temperaturas(registros):
    """Analiza tuplas de (temperatura, fecha)."""
    if not registros:
        return None
    
    temps = [temp for temp, _ in registros]
    return (min(temps), max(temps), sum(temps)/len(temps))

# Uso
temperaturas = [
    (25, "2024-02-01"),
    (28, "2024-02-02"),
    (23, "2024-02-03")
]
min_temp, max_temp, promedio = analizar_temperaturas(temperaturas)
```

## Conclusión

Las tuplas son una herramienta fundamental en Python que ofrecen:
- Inmutabilidad para datos que no deben cambiar
- Mejor rendimiento que las listas
- Claridad de intención en el código
- Versatilidad en múltiples contextos de programación

Su uso adecuado puede mejorar significativamente la calidad y eficiencia de nuestro código.