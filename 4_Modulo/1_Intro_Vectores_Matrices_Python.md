# 📊 Introducción a Vectores y Matrices

## 📚 Contenido
1. [Vectores: Conceptos Básicos](#vectores-conceptos-básicos)
2. [Matrices: Conceptos Básicos](#matrices-conceptos-básicos)
3. [Implementación en Python](#implementación-en-python)
4. [Operaciones Básicas](#operaciones-básicas)
5. [Ejercicios Prácticos](#ejercicios-prácticos)

## 🎯 Vectores: Conceptos Básicos

### ¿Qué es un Vector?
Un vector es una estructura de datos que almacena una colección ordenada de elementos del mismo tipo. En matemáticas, se representa como una lista de números y puede ser:
- Unidimensional
- De una dimensión específica (2D, 3D, etc.)
- De magnitud y dirección definidas

### Tipos de Vectores
1. **Vector Fila**: [a₁, a₂, a₃, ..., aₙ]
2. **Vector Columna**: 
   ```
   [a₁]
   [a₂]
   [a₃]
   [...]
   [aₙ]
   ```

### Propiedades de los Vectores
- Orden definido
- Dimensión fija
- Elementos del mismo tipo
- Acceso por índice
- Operaciones matemáticas definidas

## 🔲 Matrices: Conceptos Básicos

### ¿Qué es una Matriz?
Una matriz es una estructura bidimensional que organiza datos en filas y columnas. Se puede ver como una tabla o como un vector de vectores.

### Representación de una Matriz
```
[a₁₁  a₁₂  a₁₃]
[a₂₁  a₂₂  a₂₃]
[a₃₁  a₃₂  a₃₃]
```

### Propiedades de las Matrices
- Dimensión definida (m × n)
- Filas y columnas ordenadas
- Elementos del mismo tipo
- Acceso por dos índices
- Operaciones matriciales definidas

## 💻 Implementación en Python

### Vectores usando Listas

```python
# Vector usando lista simple
vector = [1, 2, 3, 4, 5]

# Acceso a elementos
primer_elemento = vector[0]
ultimo_elemento = vector[-1]

# Modificación de elementos
vector[2] = 10

# Longitud del vector
dimension = len(vector)

print(f"Vector: {vector}")
print(f"Primer elemento: {primer_elemento}")
print(f"Dimensión: {dimension}")
```

### Vectores usando NumPy

```python
import numpy as np

# Crear vector NumPy
vector_np = np.array([1, 2, 3, 4, 5])

# Operaciones vectoriales
vector_doble = vector_np * 2
vector_suma = vector_np + 3

print(f"Vector original: {vector_np}")
print(f"Vector * 2: {vector_doble}")
print(f"Vector + 3: {vector_suma}")
```

### Matrices usando Listas Anidadas

```python
# Matriz usando listas anidadas
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos
elemento = matriz[1][1]  # Fila 1, Columna 1 (valor 5)

# Modificación de elementos
matriz[0][2] = 10  # Modifica el elemento en fila 0, columna 2

# Dimensiones
filas = len(matriz)
columnas = len(matriz[0])

print(f"Matriz:\n{matriz}")
print(f"Elemento [1][1]: {elemento}")
print(f"Dimensiones: {filas}x{columnas}")
```

### Matrices usando NumPy

```python
import numpy as np

# Crear matriz NumPy
matriz_np = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Propiedades de la matriz
print(f"Forma de la matriz: {matriz_np.shape}")
print(f"Dimensión: {matriz_np.ndim}")
print(f"Tamaño: {matriz_np.size}")
```

## ➗ Operaciones Básicas

### Operaciones con Vectores

```python
import numpy as np

# Vectores de ejemplo
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

# Suma de vectores
suma = v1 + v2

# Producto escalar (dot product)
producto_punto = np.dot(v1, v2)

# Multiplicación por escalar
escalar = v1 * 2

print(f"Suma de vectores: {suma}")
print(f"Producto punto: {producto_punto}")
print(f"Vector * 2: {escalar}")
```

### Operaciones con Matrices

```python
import numpy as np

# Matrices de ejemplo
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Suma de matrices
suma = m1 + m2

# Multiplicación de matrices
producto = np.dot(m1, m2)

# Transpuesta
transpuesta = m1.T

print(f"Suma de matrices:\n{suma}")
print(f"Producto de matrices:\n{producto}")
print(f"Matriz transpuesta:\n{transpuesta}")
```

## 🎓 Ejercicios Prácticos

### Ejercicio 1: Crear y Manipular un Vector

```python
# Crear un vector de números del 1 al 5
vector = [1, 2, 3, 4, 5]

# Calcular la suma de todos los elementos
suma = sum(vector)

# Encontrar el valor máximo y mínimo
maximo = max(vector)
minimo = min(vector)

print(f"Suma: {suma}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
```

### Ejercicio 2: Operaciones con Matriz

```python
import numpy as np

# Crear una matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calcular la suma de cada fila
suma_filas = np.sum(matriz, axis=1)

# Calcular el promedio de cada columna
promedio_columnas = np.mean(matriz, axis=0)

print(f"Suma de filas: {suma_filas}")
print(f"Promedio de columnas: {promedio_columnas}")
```

## 📝 Notas Importantes

1. **Diferencias entre Listas y NumPy**
   - Las listas son más flexibles pero menos eficientes
   - NumPy es más rápido para operaciones matemáticas
   - NumPy proporciona más funciones matemáticas

2. **Buenas Prácticas**
   - Usar NumPy para cálculos matemáticos
   - Verificar dimensiones antes de operaciones
   - Mantener consistencia en los tipos de datos
   - Documentar las operaciones complejas

3. **Consideraciones de Rendimiento**
   - NumPy es más eficiente para grandes conjuntos de datos
   - Las operaciones vectorizadas son más rápidas que los bucles
   - El uso de memoria es importante en matrices grandes