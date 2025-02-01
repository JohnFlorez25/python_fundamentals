# 🐍 Listas en Python - Guía Completa

## 📚 Contenido
1. [Introducción a las Listas](#introducción-a-las-listas)
2. [Creación de Listas](#creación-de-listas)
3. [Acceso a Elementos](#acceso-a-elementos)
4. [Modificación de Listas](#modificación-de-listas)
5. [Métodos Comunes](#métodos-comunes)
6. [Ejercicios Prácticos](#ejercicios-prácticos)

## 📖 Introducción a las Listas

Las listas en Python son estructuras de datos que permiten almacenar múltiples elementos en una única variable. Características principales:

- Ordenadas: mantienen el orden de inserción
- Mutables: se pueden modificar después de su creación
- Permiten elementos duplicados
- Pueden contener diferentes tipos de datos
- Se indexan desde 0

## 🛠️ Creación de Listas

### Formas básicas de crear listas:

```python
# Lista vacía
lista_vacia = []
lista_vacia2 = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "pera", "uva"]

# Lista mixta
mixta = [1, "hola", 3.14, True]

# Lista usando range()
numeros = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Lista por comprensión
cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Lista con elementos repetidos
repetidos = [0] * 3  # [0, 0, 0]
```

## 🎯 Acceso a Elementos

### Indexación Simple

```python
frutas = ["manzana", "pera", "uva", "naranja", "plátano"]

# Acceso positivo (desde el inicio)
print(frutas[0])  # manzana
print(frutas[2])  # uva

# Acceso negativo (desde el final)
print(frutas[-1])  # plátano
print(frutas[-2])  # naranja

# Error común
# print(frutas[10])  # IndexError: list index out of range
```

### Slicing (Rebanado)

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sintaxis: lista[inicio:fin:paso]
print(numeros[2:5])    # [2, 3, 4]
print(numeros[:3])     # [0, 1, 2]
print(numeros[7:])     # [7, 8, 9]
print(numeros[::2])    # [0, 2, 4, 6, 8]
print(numeros[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## ✏️ Modificación de Listas

### Modificar elementos individuales

```python
colores = ["rojo", "verde", "azul"]

# Modificar por índice
colores[1] = "amarillo"
print(colores)  # ["rojo", "amarillo", "azul"]

# Modificar múltiples elementos
colores[0:2] = ["negro", "blanco"]
print(colores)  # ["negro", "blanco", "azul"]
```

### Añadir y eliminar elementos

```python
numeros = [1, 2, 3]

# Añadir al final
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]

# Insertar en posición específica
numeros.insert(1, 1.5)
print(numeros)  # [1, 1.5, 2, 3, 4]

# Eliminar por valor
numeros.remove(1.5)
print(numeros)  # [1, 2, 3, 4]

# Eliminar por índice
del numeros[0]
print(numeros)  # [2, 3, 4]

# Extraer y devolver el último elemento
ultimo = numeros.pop()
print(ultimo)    # 4
print(numeros)   # [2, 3]
```

## 🔧 Métodos Comunes de Listas

### Métodos para Agregar Elementos
```python
lista = [1, 2, 3]

# append(): Agrega un elemento al final
lista.append(4)
print(lista)  # [1, 2, 3, 4]

# insert(): Inserta un elemento en una posición específica
lista.insert(1, 1.5)  # insert(posición, elemento)
print(lista)  # [1, 1.5, 2, 3, 4]

# extend(): Agrega elementos de un iterable al final
lista.extend([5, 6])
print(lista)  # [1, 1.5, 2, 3, 4, 5, 6]
```

### Métodos para Eliminar Elementos
```python
lista = [1, 2, 2, 3, 4, 4, 5]

# remove(): Elimina la primera ocurrencia de un elemento
lista.remove(2)
print(lista)  # [1, 2, 3, 4, 4, 5]

# pop(): Elimina y retorna un elemento por su índice
elemento = lista.pop(1)  # Sin índice elimina el último
print(elemento)  # 2
print(lista)    # [1, 3, 4, 4, 5]

# clear(): Elimina todos los elementos
lista.clear()
print(lista)  # []
```

### Métodos de Ordenamiento
```python
lista = [3, 1, 4, 1, 5, 9, 2, 6]

# sort(): Ordena la lista in-place
lista.sort()  # Ascendente
print(lista)  # [1, 1, 2, 3, 4, 5, 6, 9]

lista.sort(reverse=True)  # Descendente
print(lista)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sort() con key function
palabras = ['perro', 'gato', 'elefante']
palabras.sort(key=len)  # Ordena por longitud
print(palabras)  # ['gato', 'perro', 'elefante']

# reverse(): Invierte el orden de los elementos
lista.reverse()
print(lista)  # [1, 1, 2, 3, 4, 5, 6, 9]
```

### Métodos de Búsqueda e Información

```python
numeros = [1, 2, 2, 3, 4, 4, 5]

# Longitud de la lista
print(len(numeros))  # 7

# Contar ocurrencias
print(numeros.count(2))  # 2

# Encontrar índice
print(numeros.index(3))  # 3

# Verificar existencia
print(2 in numeros)  # True
print(8 in numeros)  # False
```

### Métodos de Ordenamiento

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Ordenar la lista (modifica la original)
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Ordenar en reversa
numeros.sort(reverse=True)
print(numeros)  # [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

# Crear nueva lista ordenada (no modifica la original)
desordenada = [3, 1, 4, 1, 5]
ordenada = sorted(desordenada)
print(desordenada)  # [3, 1, 4, 1, 5]
print(ordenada)     # [1, 1, 3, 4, 5]

# Invertir lista
numeros.reverse()
print(numeros)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Métodos de Combinación

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Concatenar listas
combinada = lista1 + lista2
print(combinada)  # [1, 2, 3, 4, 5, 6]

# Extender una lista
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5, 6]
```

## 💻 Ejercicios Prácticos

1. **Ejercicio Básico: Crear y Modificar**
```python
# Crear una lista de 5 frutas
frutas = ["manzana", "pera", "uva", "naranja", "plátano"]

# Modificar la tercera fruta
frutas[2] = "kiwi"

# Añadir una fruta al final
frutas.append("mango")

print(frutas)
```

2. **Ejercicio Intermedio: Manipulación de Lista**
```python
# Crear lista de números del 1 al 10
numeros = list(range(1, 11))

# Eliminar números pares
for numero in numeros[:]:  # [:] crea una copia para iterar
    if numero % 2 == 0:
        numeros.remove(numero)

print(numeros)  # [1, 3, 5, 7, 9]
```

3. **Ejercicio Avanzado: Análisis de Datos**
```python
temperaturas = [20, 25, 23, 22, 28, 27, 21]

# Calcular promedio
promedio = sum(temperaturas) / len(temperaturas)

# Encontrar temperatura máxima y mínima
maxima = max(temperaturas)
minima = min(temperaturas)

print(f"Promedio: {promedio:.2f}")
print(f"Máxima: {maxima}")
print(f"Mínima: {minima}")
```

## 📝 Notas Importantes

1. Las listas son referencias
```python
lista1 = [1, 2, 3]
lista2 = lista1  # Ambas variables apuntan a la misma lista
lista2[0] = 100
print(lista1)  # [100, 2, 3]

# Para crear una copia independiente
lista2 = lista1.copy()  # o lista1[:]
```

2. Buenas prácticas
- Usar nombres descriptivos para las listas
- Mantener tipos de datos consistentes dentro de una lista
- Verificar índices antes de acceder a elementos
- Considerar el uso de métodos incorporados en lugar de bucles cuando sea posible

## 🔍 Tips y Trucos

1. **Invertir una lista**
```python
numeros = [1, 2, 3, 4, 5]
invertida = numeros[::-1]  # [5, 4, 3, 2, 1]
```

2. **Eliminar duplicados**
```python
numeros = [1, 2, 2, 3, 3, 4, 5, 5]
sin_duplicados = list(set(numeros))  # [1, 2, 3, 4, 5]
```

3. **Crear lista de números pares**
```python
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

4. **Aplanar una lista de listas**
```python
lista_anidada = [[1, 2], [3, 4], [5, 6]]
aplanada = [num for sublist in lista_anidada for num in sublist]
# [1, 2, 3, 4, 5, 6]
```