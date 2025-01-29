# Sentencias `if`, `elif`, `else` en Python

## Introducción
Las sentencias condicionales en Python permiten tomar decisiones dentro de un programa. La estructura `if`, `elif` y `else` se usa para ejecutar distintos bloques de código dependiendo de ciertas condiciones.

Python evalúa una expresión booleana (`True` o `False`) y ejecuta el bloque de código correspondiente.

---

## 1. Estructura de `if`
La estructura básica de una condición en Python es:

```python
if condicion:
    # Bloque de código que se ejecuta si la condicion es verdadera
```

### Ejemplo:

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
```

En este caso, si la variable `edad` es mayor o igual a 18, se imprime el mensaje "Eres mayor de edad".

---

## 2. Uso de `if` y `else`
La sentencia `else` nos permite definir un bloque de código alternativo si la condición del `if` es falsa.

```python
if condicion:
    # Bloque si la condicion es verdadera
else:
    # Bloque si la condicion es falsa
```

### Ejemplo:

```python
edad = 16
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

Si `edad` es menor de 18, se ejecuta el bloque del `else`, mostrando "Eres menor de edad".

---

## 3. Uso de `if`, `elif` y `else`
Cuando hay múltiples condiciones a evaluar, usamos `elif` (else if). Permite definir varias condiciones en serie.

```python
if condicion1:
    # Bloque si condicion1 es verdadera
elif condicion2:
    # Bloque si condicion2 es verdadera
else:
    # Bloque si ninguna de las condiciones anteriores es verdadera
```

### Ejemplo:

```python
nota = 75
if nota >= 90:
    print("Sobresaliente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

Si la `nota` es mayor o igual a 90, se muestra "Sobresaliente". Si es al menos 70, se muestra "Aprobado". En cualquier otro caso, se imprime "Reprobado".

---

## 4. Condiciones Anidadas
Las estructuras condicionales pueden anidarse dentro de otras para evaluar condiciones más complejas.

```python
if condicion1:
    if condicion2:
        # Bloque si ambas condiciones son verdaderas
    else:
        # Bloque si solo condicion1 es verdadera
else:
    # Bloque si condicion1 es falsa
```

### Ejemplo:

```python
edad = 20
tiene_identificacion = True
if edad >= 18:
    if tiene_identificacion:
        print("Puedes ingresar al evento")
    else:
        print("Necesitas una identificación")
else:
    print("Eres menor de edad, no puedes ingresar")
```

Este ejemplo primero verifica si la persona es mayor de edad. Si es así, evalúa si tiene identificación antes de permitirle el acceso.

---

## 5. Expresiones Condicionales en Una Línea (Operador Ternario)
Python permite escribir condicionales en una sola línea mediante una expresión compacta:

```python
resultado = "Aprobado" if nota >= 70 else "Reprobado"
```

Equivalente a:

```python
if nota >= 70:
    resultado = "Aprobado"
else:
    resultado = "Reprobado"
```

### Ejemplo:

```python
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(mensaje)
```

---

## 6. Uso de `and`, `or` y `not` en Condicionales
Los operadores lógicos permiten evaluar múltiples condiciones en una sola expresión:

- `and`: Ambas condiciones deben ser verdaderas.
- `or`: Al menos una condición debe ser verdadera.
- `not`: Invierte el valor de una expresión.

### Ejemplo:

```python
usuario = "admin"
clave = "1234"
if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")
```

---

## 7. Conclusión
Las sentencias `if`, `elif` y `else` son fundamentales en Python para la toma de decisiones dentro de un programa. El uso de operadores lógicos, estructuras anidadas y expresiones condicionales permite manejar condiciones complejas de manera eficiente.

