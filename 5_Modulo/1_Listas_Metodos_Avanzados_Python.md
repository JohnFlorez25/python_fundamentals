# Métodos Avanzados de Listas en Python

## Introducción a los Métodos de Listas

Las listas en Python son estructuras de datos extremadamente versátiles que ofrecen una amplia gama de métodos especializados. Conocer estos métodos en profundidad nos permite escribir código más eficiente y elegante.

## Métodos de Inserción y Eliminación

### insert() - Inserción en Posición Específica
```python
# Sintaxis: lista.insert(posición, elemento)
estudiantes = ["Ana", "Carlos", "Diana"]
estudiantes.insert(1, "Bernardo")
print(estudiantes)  # ["Ana", "Bernardo", "Carlos", "Diana"]

# Uso práctico: Insertar estudiante nuevo manteniendo orden alfabético
def insertar_ordenado(lista, nuevo_estudiante):
    for i, estudiante in enumerate(lista):
        if estudiante > nuevo_estudiante:
            lista.insert(i, nuevo_estudiante)
            return
    lista.append(nuevo_estudiante)
```

### pop() - Extracción con Retorno
```python
# Sintaxis básica: lista.pop() o lista.pop(índice)
tareas = ["Estudiar", "Trabajar", "Ejercicio", "Descansar"]

# Eliminar y obtener última tarea
ultima_tarea = tareas.pop()
print(f"Completada: {ultima_tarea}")  # Completada: Descansar

# Eliminar y obtener tarea específica
tarea_actual = tareas.pop(1)  # Elimina "Trabajar"
print(f"Realizando: {tarea_actual}")

# Uso práctico: Implementar una pila de tareas
class PilaTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
    
    def completar_tarea(self):
        return self.tareas.pop() if self.tareas else None
```

### index() - Búsqueda de Elementos
```python
# Sintaxis: lista.index(elemento[, inicio[, fin]])
colores = ["rojo", "verde", "azul", "verde", "amarillo"]

# Búsqueda simple
pos_verde = colores.index("verde")  # Retorna 1

# Búsqueda con rango
pos_verde_siguiente = colores.index("verde", 2)  # Busca desde índice 2

# Uso práctico: Búsqueda segura
def buscar_seguro(lista, elemento):
    try:
        return lista.index(elemento)
    except ValueError:
        return -1
```

## Métodos de Ordenamiento y Manipulación

### sort() y sorted() - Ordenamiento Avanzado
```python
# sort() modifica la lista original
# sorted() crea una nueva lista
estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Diana", "nota": 88}
]

# Ordenar por nota
estudiantes.sort(key=lambda x: x["nota"], reverse=True)

# Ordenamiento múltiple
def ordenar_por_nota_y_nombre(estudiante):
    return (-estudiante["nota"], estudiante["nombre"])

estudiantes.sort(key=ordenar_por_nota_y_nombre)
```

### extend() - Extensión de Listas
```python
# Sintaxis: lista.extend(iterable)
numeros_base = [1, 2, 3]
numeros_extra = [4, 5, 6]

# Extender lista
numeros_base.extend(numeros_extra)

# Uso práctico: Combinar múltiples fuentes de datos
def combinar_datos(*listas):
    resultado = []
    for lista in listas:
        resultado.extend(lista)
    return resultado
```

## Métodos de Búsqueda y Conteo

### count() - Conteo de Ocurrencias
```python
# Sintaxis: lista.count(elemento)
votos = ["A", "B", "A", "C", "B", "A", "A"]

# Contar votos
votos_a = votos.count("A")  # 4

# Uso práctico: Análisis de frecuencia
def obtener_frecuencias(lista):
    return {elemento: lista.count(elemento) 
            for elemento in set(lista)}
```

### clear() - Limpieza de Lista
```python
# Sintaxis: lista.clear()
carrito = ["Producto1", "Producto2", "Producto3"]

# Limpiar carrito después de compra
def procesar_compra(carrito):
    # Procesar items
    total = len(carrito)
    carrito.clear()
    return f"Compra de {total} items procesada"
```

## Métodos de Copia y Referencia

### copy() - Copia Superficial
```python
# Sintaxis: lista.copy()
original = [1, [2, 3], 4]
copia = original.copy()

# Uso práctico: Preservar estado original
def procesar_sin_modificar(lista):
    temp = lista.copy()
    temp.sort()
    return temp
```

## Técnicas Avanzadas y Combinaciones

### Slicing con Asignación
```python
# Modificar sección de lista
numeros = [1, 2, 3, 4, 5]
numeros[1:4] = [20, 30, 40]

# Uso práctico: Actualización por lotes
def actualizar_rango(lista, inicio, fin, nuevos_valores):
    lista[inicio:fin] = nuevos_valores
```

### List Comprehension con Métodos
```python
# Combinar métodos en comprensiones
palabras = ["python", "programación", "lista", "métodos"]

# Filtrar y transformar
mayusculas = [p.upper() for p in palabras if len(p) > 5]

# Uso práctico: Procesamiento de datos
def procesar_textos(textos, min_longitud=5):
    return [texto.capitalize() 
            for texto in textos 
            if len(texto) >= min_longitud]
```

## Patrones Comunes y Mejores Prácticas

### Patrón: Filtrado con Preservación
```python
def filtrar_preservando(lista, condicion):
    """Filtra elementos manteniendo la lista original."""
    indices_a_eliminar = []
    for i, elemento in enumerate(lista):
        if not condicion(elemento):
            indices_a_eliminar.append(i)
    
    for i in reversed(indices_a_eliminar):
        lista.pop(i)
```

### Patrón: Acumulación Segura
```python
def agregar_seguro(lista, elemento, max_longitud=100):
    """Agrega elementos de forma segura con límite."""
    if len(lista) >= max_longitud:
        lista.pop(0)  # Elimina el más antiguo
    lista.append(elemento)
```

### Patrón: Búsqueda con Índice Default
```python
def encontrar_o_default(lista, elemento, default=-1):
    """Busca un elemento retornando valor por defecto si no existe."""
    try:
        return lista.index(elemento)
    except ValueError:
        return default
```

## Tips de Optimización

1. Usar métodos incorporados en lugar de bucles cuando sea posible
2. Aprovechar slicing para operaciones por lotes
3. Combinar métodos para reducir iteraciones
4. Considerar el uso de collections.deque para operaciones frecuentes al inicio de la lista

## Consideraciones de Rendimiento

1. `append()` es más rápido que `insert()`
2. `pop()` sin índice es más rápido que con índice
3. `extend()` es más eficiente que múltiples `append()`
4. `index()` tiene complejidad O(n)
