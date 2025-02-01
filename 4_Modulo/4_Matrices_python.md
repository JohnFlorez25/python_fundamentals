# 🔲 Matrices en Python: Listas Anidadas

## 📚 Contenido
1. [¿Qué es una Matriz en Python?](#qué-es-una-matriz-en-python)
2. [Creación de Matrices](#creación-de-matrices)
3. [Acceso a Elementos](#acceso-a-elementos)
4. [Iteración de Matrices](#iteración-de-matrices)
5. [Ejercicios Prácticos](#ejercicios-prácticos)

## ¿Qué es una Matriz en Python?

Una matriz en Python se implementa como una lista de listas, donde cada lista interna representa una fila de la matriz. Es una estructura de datos bidimensional que organiza elementos en filas y columnas.

### Estructura Básica
```python
# Matriz 3x3
matriz = [
    [1, 2, 3],  # Fila 0
    [4, 5, 6],  # Fila 1
    [7, 8, 9]   # Fila 2
]
```

## 📝 Creación de Matrices

### 1. Creación Manual
```python
# Matriz 2x3
matriz_2x3 = [
    [1, 2, 3],
    [4, 5, 6]
]

# Matriz 3x2
matriz_3x2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]
```

### 2. Creación por Comprensión
```python
# Matriz 3x3 con valores incrementales
matriz = [[i + j*3 + 1 for i in range(3)] for j in range(3)]
print(matriz)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Matriz 3x3 inicializada con ceros
matriz_ceros = [[0 for j in range(3)] for i in range(3)]
print(matriz_ceros)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 3. Creación con Bucles
```python
# Crear matriz 3x3 con entrada del usuario
matriz = []
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Ingrese valor para posición [{i}][{j}]: "))
        fila.append(valor)
    matriz.append(fila)
```

## 🎯 Acceso a Elementos

### 1. Acceso Directo
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos individuales
elemento = matriz[1][2]  # Fila 1, Columna 2 (valor: 6)
primera_fila = matriz[0]  # [1, 2, 3]
ultimo_elemento = matriz[2][2]  # 9

print(f"Elemento [1][2]: {elemento}")
print(f"Primera fila: {primera_fila}")
print(f"Último elemento: {ultimo_elemento}")
```

### 2. Modificación de Elementos
```python
# Modificar un elemento específico
matriz[0][1] = 10  # Modifica el elemento en fila 0, columna 1

# Modificar una fila completa
matriz[1] = [10, 11, 12]

# Modificar una columna
for i in range(len(matriz)):
    matriz[i][0] = 0  # Modifica la primera columna
```

### 3. Obtención de Dimensiones
```python
# Obtener número de filas
filas = len(matriz)

# Obtener número de columnas
columnas = len(matriz[0])

print(f"Dimensiones: {filas}x{columnas}")
```

## 🔄 Iteración de Matrices

### 1. Iteración por Elementos
```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Método 1: Bucles anidados con índices
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"Elemento [{i}][{j}]: {matriz[i][j]}")

# Método 2: Bucles for anidados directos
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Nueva línea después de cada fila
```

### 2. Iteración por Filas
```python
# Procesar cada fila
for fila in matriz:
    suma_fila = sum(fila)
    print(f"Suma de la fila: {suma_fila}")

# Procesar filas con índice
for i, fila in enumerate(matriz):
    print(f"Fila {i}: {fila}")
```

### 3. Iteración por Columnas
```python
# Procesar cada columna
for j in range(len(matriz[0])):
    columna = [matriz[i][j] for i in range(len(matriz))]
    print(f"Columna {j}: {columna}")

# Calcular suma de columnas
sumas_columnas = []
for j in range(len(matriz[0])):
    suma = sum(matriz[i][j] for i in range(len(matriz)))
    sumas_columnas.append(suma)
```

## 💻 Ejercicios Prácticos

### Ejercicio 1: Suma de Matrices
```python
def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        return None  # Las matrices deben tener las mismas dimensiones
    
    resultado = []
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[0])):
            fila.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila)
    return resultado

# Ejemplo de uso
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
resultado = sumar_matrices(m1, m2)
print(f"Resultado de la suma:\n{resultado}")
```

### Ejercicio 2: Buscar Elemento
```python
def buscar_elemento(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == elemento:
                return (i, j)  # Retorna la posición si encuentra el elemento
    return None  # Retorna None si no encuentra el elemento

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
posicion = buscar_elemento(matriz, 5)
print(f"El elemento 5 está en la posición: {posicion}")
```

### Ejercicio 3: Matriz Transpuesta
```python
def transponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = [[0 for i in range(filas)] for j in range(columnas)]
    
    for i in range(filas):
        for j in range(columnas):
            transpuesta[j][i] = matriz[i][j]
    
    return transpuesta

# Ejemplo de uso
matriz = [[1, 2, 3], [4, 5, 6]]
transpuesta = transponer_matriz(matriz)
print(f"Matriz transpuesta:\n{transpuesta}")
```

## 📝 Notas Importantes

1. **Buenas Prácticas**
   - Verificar dimensiones antes de operar con matrices
   - Manejar errores cuando las dimensiones no coinciden
   - Documentar las funciones que manipulan matrices

2. **Consideraciones de Rendimiento**
   - Las listas anidadas son más lentas que NumPy para operaciones matemáticas
   - Para cálculos intensivos, considerar usar NumPy
   - La memoria aumenta cuadráticamente con el tamaño de la matriz

3. **Depuración Común**
   - Índices fuera de rango
   - Dimensiones incorrectas
   - Referencias a listas (copias vs referencias)