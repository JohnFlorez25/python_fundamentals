# Operaciones Básicas en Python

---

## **1. Operaciones Aritméticas**

Las operaciones aritméticas en Python son fundamentales para realizar cálculos matemáticos. Python soporta las operaciones comunes como suma, resta, multiplicación, división, entre otras.

### **1.1. Operadores Aritméticos:**

- **Suma (`+`)**: Suma dos valores.
- **Resta (`-`)**: Resta el segundo valor al primero.
- **Multiplicación (`*`)**: Multiplica dos valores.
- **División (`/`)**: Realiza la división flotante de dos valores.
- **División Entera (`//`)**: Realiza la división de enteros, eliminando el residuo.
- **Módulo (`%`)**: Devuelve el residuo de una división.
- **Exponenciación (`**`)**: Eleva un número a la potencia de otro.

### **1.2. Ejemplos de Operaciones Aritméticas:**

```python
a = 10
b = 5

# Suma
print(a + b)  # Salida: 15

# Resta
print(a - b)  # Salida: 5

# Multiplicación
print(a * b)  # Salida: 50

# División
print(a / b)  # Salida: 2.0

# División Entera
print(a // b)  # Salida: 2

# Módulo
print(a % b)  # Salida: 0

# Exponenciación
print(a ** b)  # Salida: 100000
```

## 2. Operaciones Relacionales

Las operaciones relacionales son usadas para comparar dos valores y devolver un resultado booleano (`True` o `False`), dependiendo de si la comparación es verdadera o falsa.

### 2.1. Operadores Relacionales:

- Igual a `(==)`: Compara si dos valores son iguales.
- Diferente a `(!=)`: Compara si dos valores son diferentes.
- Mayor que `(>)`: Compara si el primer valor es mayor que el segundo.
- Menor que `(<)`: Compara si el primer valor es menor que el segundo.
- Mayor o igual que `(>=)`: Compara si el primer valor es mayor o igual que el segundo.
- Menor o igual que `(<=)`: Compara si el primer valor es menor o igual que el segundo.

### 2.2. Ejemplos de Operaciones Relacionales:

```python
a = 10
b = 5

# Igual a
print(a == b)  # Salida: False

# Diferente a
print(a != b)  # Salida: True

# Mayor que
print(a > b)   # Salida: True

# Menor que
print(a < b)   # Salida: False

# Mayor o igual que
print(a >= b)  # Salida: True

# Menor o igual que
print(a <= b)  # Salida: False
```

## 3. Operaciones Lógicas

Las operaciones lógicas se utilizan para combinar expresiones booleanas (verdaderas o falsas). Son esenciales para la toma de decisiones y control de flujo en el programa.

### 3.1. Operadores Lógicos:

- Y lógico `(and)`: Devuelve `True` solo si ambas expresiones son `True`.
- O lógico `(or)`: Devuelve `True` si al menos una de las expresiones es `True`.
- No lógico `(not)`: Invierte el valor de la expresión booleana (si es `True`, devuelve `False` y viceversa).

### 3.2. Ejemplos de Operaciones Lógicas:

```python
a = True
b = False

# Y lógico (and)
print(a and b)  # Salida: False

# O lógico (or)
print(a or b)   # Salida: True

# No lógico (not)
print(not a)    # Salida: False
```

### 3.3. Operadores Lógicos con Condiciones

También puedes usar operadores lógicos con condiciones para tomar decisiones basadas en múltiples condiciones.

```python
edad = 20
permiso = True

# Verificando si la persona tiene la edad suficiente y el permiso
if edad >= 18 and permiso:
    print("Acceso concedido")
else:
    print("Acceso denegado")
```

