# Diccionarios en Python: Mapeo de Claves y Valores

## ¿Qué son los Diccionarios?

Un diccionario en Python es una estructura de datos que permite almacenar información en pares de clave-valor, similar a un diccionario real donde cada palabra (clave) tiene su definición (valor). Imagina una agenda telefónica: el nombre de cada persona sería la clave, y su número de teléfono sería el valor.

## Creación de Diccionarios

### Sintaxis Básica
```python
# Diccionario vacío
agenda = {}
agenda_alternativa = dict()

# Diccionario con datos iniciales
estudiante = {
    "nombre": "Ana García",
    "edad": 20,
    "carrera": "Ingeniería",
    "promedio": 4.5
}

# Creación usando dict() con pares clave-valor
configuracion = dict(
    idioma="español",
    tema="oscuro",
    notificaciones=True
)
```

### Tipos de Datos como Claves y Valores
```python
# Las claves pueden ser cualquier objeto inmutable
diccionario_mixto = {
    42: "número",              # Entero como clave
    "pi": 3.14159,            # Cadena como clave
    (1, 2): "coordenada",     # Tupla como clave
    "lista": [1, 2, 3],       # Lista como valor
    "tupla": (4, 5, 6),       # Tupla como valor
    "dict": {"a": 1}          # Diccionario como valor
}

# Importante: Las listas NO pueden ser claves porque son mutables
# Este código generaría un error:
# error_dict = {[1, 2]: "valor"}  # TypeError
```

## Acceso a Elementos

### Métodos Básicos de Acceso
```python
estudiante = {
    "nombre": "Ana García",
    "edad": 20,
    "carrera": "Ingeniería"
}

# Acceso directo con corchetes
nombre = estudiante["nombre"]      # Ana García

# Acceso seguro con get()
edad = estudiante.get("edad")      # 20
# get() con valor por defecto
ciudad = estudiante.get("ciudad", "No especificada")  # No especificada

# Comparación de métodos de acceso
try:
    # Esto generará KeyError si la clave no existe
    telefono = estudiante["telefono"]
except KeyError:
    print("La clave 'telefono' no existe")

# Mientras que esto no generará error
telefono = estudiante.get("telefono")  # Retorna None si no existe
```

## Métodos Principales de Diccionarios

### Obtención de Claves, Valores e Items

```python
producto = {
    "nombre": "Laptop",
    "precio": 1200,
    "stock": 5,
    "disponible": True
}

# Obtener todas las claves
claves = producto.keys()
print(f"Claves: {list(claves)}")  
# Salida: Claves: ['nombre', 'precio', 'stock', 'disponible']

# Obtener todos los valores
valores = producto.values()
print(f"Valores: {list(valores)}")  
# Salida: Valores: ['Laptop', 1200, 5, True]

# Obtener pares clave-valor
items = producto.items()
for clave, valor in items:
    print(f"{clave}: {valor}")

# Nota: keys(), values() e items() devuelven vistas dinámicas
# Las vistas se actualizan cuando el diccionario cambia
```

### Modificación de Diccionarios

```python
inventario = {"manzanas": 50, "peras": 30}

# Actualizar o añadir elementos
inventario["manzanas"] = 45      # Actualizar existente
inventario["naranjas"] = 25      # Añadir nuevo

# Actualizar múltiples elementos
inventario.update({
    "manzanas": 40,
    "peras": 25,
    "plátanos": 35
})

# Eliminar elementos
del inventario["peras"]          # Eliminar con del
fruta = inventario.pop("manzanas")  # Eliminar y obtener valor
ultimo = inventario.popitem()    # Eliminar y obtener último par

# Limpiar diccionario
inventario.clear()  # Elimina todos los elementos
```

### Métodos de Verificación

```python
usuario = {
    "nombre": "Carlos",
    "edad": 25,
    "activo": True
}

# Verificar existencia de clave
tiene_nombre = "nombre" in usuario              # True
tiene_email = "email" in usuario               # False

# Verificar no existencia
no_tiene_telefono = "telefono" not in usuario  # True

# Longitud del diccionario
num_campos = len(usuario)                      # 3
```

## Casos de Uso Prácticos

### 1. Contador de Frecuencias
```python
def contar_palabras(texto):
    """Cuenta la frecuencia de cada palabra en un texto."""
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        # Incrementa el contador, iniciando en 0 si no existe
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    
    return frecuencias

texto = "el gato y el perro el gato"
print(contar_palabras(texto))
# Salida: {'el': 3, 'gato': 2, 'y': 1, 'perro': 1}
```

### 2. Caché de Resultados
```python
def fibonacci_con_cache(n, cache=None):
    """Calcula Fibonacci usando un diccionario como caché."""
    if cache is None:
        cache = {}
    
    if n in cache:
        return cache[n]
    
    if n <= 1:
        return n
    
    cache[n] = fibonacci_con_cache(n-1, cache) + fibonacci_con_cache(n-2, cache)
    return cache[n]
```

### 3. Registro de Estudiantes
```python
class RegistroEstudiantes:
    def __init__(self):
        self.estudiantes = {}
    
    def agregar_estudiante(self, id, nombre, notas):
        self.estudiantes[id] = {
            "nombre": nombre,
            "notas": notas,
            "promedio": sum(notas) / len(notas)
        }
    
    def obtener_promedio(self, id):
        estudiante = self.estudiantes.get(id)
        if estudiante:
            return estudiante["promedio"]
        return None
```

## Tips y Mejores Prácticas

### 1. Evitar KeyError con setdefault()
```python
# En lugar de:
if "contador" not in diccionario:
    diccionario["contador"] = 0
diccionario["contador"] += 1

# Usar:
diccionario.setdefault("contador", 0)
diccionario["contador"] += 1
```

### 2. Acceso a Datos Anidados
```python
def obtener_valor_seguro(diccionario, ruta, default=None):
    """Accede de forma segura a datos anidados."""
    for clave in ruta.split('.'):
        try:
            diccionario = diccionario[clave]
        except (KeyError, TypeError):
            return default
    return diccionario

datos = {"usuario": {"perfil": {"nombre": "Ana"}}}
nombre = obtener_valor_seguro(datos, "usuario.perfil.nombre")
```

### 3. Diccionarios por Comprensión
```python
# Crear diccionario de cuadrados
cuadrados = {x: x**2 for x in range(5)}
# Salida: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrar elementos
positivos = {k: v for k, v in numeros.items() if v > 0}
```

## Ejercicios Prácticos

### 1. Sistema de Inventario
```python
def gestionar_inventario():
    inventario = {}
    
    def agregar_producto(nombre, cantidad, precio):
        inventario[nombre] = {
            "cantidad": cantidad,
            "precio": precio,
            "valor_total": cantidad * precio
        }
    
    def actualizar_cantidad(nombre, nueva_cantidad):
        if nombre in inventario:
            inventario[nombre]["cantidad"] = nueva_cantidad
            inventario[nombre]["valor_total"] = \
                nueva_cantidad * inventario[nombre]["precio"]
    
    return inventario, agregar_producto, actualizar_cantidad
```

### 2. Análisis de Datos
```python
def analizar_ventas(ventas_diarias):
    """Analiza datos de ventas usando métodos de diccionarios."""
    resultados = {
        "total_ventas": sum(ventas_diarias.values()),
        "promedio_diario": sum(ventas_diarias.values()) / len(ventas_diarias),
        "mejor_dia": max(ventas_diarias.items(), key=lambda x: x[1]),
        "peor_dia": min(ventas_diarias.items(), key=lambda x: x[1])
    }
    return resultados
```

## Consejos para el Rendimiento

1. Los diccionarios son muy eficientes para búsquedas
2. Usar `get()` con valor por defecto evita excepciones
3. `setdefault()` es más eficiente que verificar y asignar
4. Para iteraciones frecuentes, considerar guardar `keys()`, `values()` o `items()` en variables

## Conclusión

Los diccionarios son una estructura de datos fundamental en Python que ofrece:
- Acceso rápido a valores mediante claves
- Flexibilidad en tipos de datos
- Métodos poderosos para manipulación de datos
- Excelente rendimiento para búsquedas

Su uso adecuado puede mejorar significativamente la claridad y eficiencia de nuestro código.