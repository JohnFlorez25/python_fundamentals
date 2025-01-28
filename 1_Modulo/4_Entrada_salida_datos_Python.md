# Entrada y Salida de Datos en Python

---

## **1. Entrada de Datos: `input()`**

En Python, la función `input()` se utiliza para leer datos ingresados por el usuario desde la consola. El valor ingresado siempre será interpretado como una cadena de texto (tipo `str`), incluso si se ingresa un número.

### **Sintaxis Básica:**

```python
variable = input("Mensaje para el usuario: ")
```

- `"Mensaje para el usuario: "` es el texto que se muestra en la consola para pedir la entrada.

- `variable` es donde se almacenará la entrada del usuario.

**Ejemplo:**

```python
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre + "!")
```
**Salida en consola**

```bash
¿Como te llamas? Juan
Hola, Juan!
```

### **Convertir el tipo de Dato:**

Si se desea almacenar un número, es necesario convertir la entrada a un tipo adecuado, como `int` o `float`.

```python
edad = int(input("¿Cuántos años tienes? "))
print("Tienes", edad, "años.")
```

**Salida en consola**

```bash
¿Cuántos años tienes? 25
Tienes 25 años.
```

> Nota: La función `input()` siempre devuelve un tipo `str`. Si necesitamos un número entero, usamos `int()`; si necesitamos un número decimal, usamos `float()`.

## 2. Salida de Datos: `print()`

La función `print()` se utiliza para mostrar información en la consola. Es una de las funciones más utilizadas en Python.

### **Sintaxis Básica:**

```python
print(valor1, valor2, ..., sep=' ', end='\n')
```

- `valor1, valor2, ...`: Los valores que se desean mostrar.
- `sep`: Define el separador entre los valores (por defecto, un espacio).
- `end`: Define qué se imprimirá al final (por defecto, un salto de línea `\n`).

**Ejemplo Básico:**

```python
nombre = "Juan"
edad = 25
print("Mi nombre es", nombre, "y tengo", edad, "años.")
```

**Salida consola:**

```bash
Mi nombre es Juan y tengo 25 años.
```

### Personalizar separadores y fin de línea:

El parámetro `sep` permite cambiar el separador entre los valores, mientras que el parámetro end permite personalizar lo que aparece al final del `print()`.

```python
print("Hola", "Mundo", sep="-")  # Cambia el espacio por un guion
print("Esto es una línea.", end=" ")  # No salta de línea
print("Esto sigue en la misma línea.")
```

**Salida en consola:"**

```bash
Hola-Mundo
Esto es una línea. Esto sigue en la misma línea.
```

## 3. Resumen

- **Entrada**: Utiliza input() para capturar la entrada del usuario desde la consola. Recuerda que la entrada es siempre una cadena de texto (str).
- 
- **Salida**: Utiliza print() para mostrar información en la consola. Puedes personalizar cómo se imprimen los valores con los parámetros sep y end.

## 4. Salida de Datos: `print()` - Estilos Avanzados

En Python, existen diferentes formas de mostrar datos con la función `print()`. Aunque la concatenación de cadenas usando `+` es común, hay métodos más avanzados y recomendados que facilitan la legibilidad del código y evitan problemas con la concatenación de tipos distintos. A continuación, exploraremos tres estilos principales: el uso de **f-strings**, el uso de **`str.format()`** y el uso de **variables intermedias**.

---

### **4.1. Uso de f-strings (Formato Literal de Cadenas)**

Las **f-strings** (disponibles desde Python 3.6) son la forma más eficiente y legible de insertar expresiones dentro de cadenas de texto. Para usarlas, simplemente se coloca una `f` antes de las comillas de la cadena y las variables o expresiones dentro de `{}`.

#### **Sintaxis Básica:**

```python
f"Texto {variable} más texto"
```

**Ejemplo:**

```python
nombre = "Juan"
edad = 25
altura = 1.75

# Uso de f-string
print(f"Mi nombre es {nombre}, tengo {edad} años y mido {altura} metros.")
```

**Salida en consola:**
```bash
Mi nombre es Juan, tengo 25 años y mido 1.75 metros.
```

**Ventajas de f-strings:**

- Más rápido y eficiente en comparación con otros métodos de formateo.
- Permite insertar variables y expresiones directamente dentro de la cadena, lo que mejora la legibilidad.
- La sintaxis es más limpia y directa.

### **4.2. Uso de `str.format()`**

El método `str.format()` es otra forma popular de formatear cadenas en Python, y es compatible con versiones anteriores a Python 3.6.

**Sintaxis Básica:**

```python
"Texto {} más texto".format(variable)
```

**Ejemplo:**
```python
nombre = "Ana"
edad = 30
altura = 1.68

# Uso de str.format()
print("Mi nombre es {}, tengo {} años y mido {} metros.".format(nombre, edad, altura))
```

**Salida en consola:**
```bash
Mi nombre es Ana, tengo 30 años y mido 1.68 metros.
```

**Ventajas de `str.format()`:**

- Compatible con versiones anteriores de Python.
- Permite usar índices y nombres de parámetros para mayor flexibilidad.


**Ejemplo con índices:**

```python
print("Mi nombre es {0}, tengo {1} años y mido {2} metros.".format(nombre, edad, altura))
```

**Salida en consola:**
```bash
Mi nombre es Ana, tengo 30 años y mido 1.68 metros.
```

**Ejemplo con parámetros nombrados:**

```python
print("Mi nombre es {nombre}, tengo {edad} años y mido {altura} metros.".format(nombre=nombre, edad=edad, altura=altura))
```

**Salida en consola:**
```bash
Mi nombre es Ana, tengo 30 años y mido 1.68 metros.
```



### 4.3. Uso de Variables Intermedias

En situaciones donde se tienen múltiples expresiones o valores que requieren ser procesados antes de ser impresos, es útil almacenar estos valores en **variables intermedias** y luego usarlas con `print()`.

**Ejemplo:**

```python
nombre = "Carlos"
edad = 28
altura = 1.80

# Variables intermedias
descripcion = f"Mi nombre es {nombre}, tengo {edad} años y mido {altura} metros."

# Usamos una variable intermedia para la salida
print(descripcion)
```

**Salida en consola:**
```bash
Mi nombre es Carlos, tengo 28 años y mido 1.80 metros.
```

**Ventajas del uso de variables intermedias:**


- **Claridad:** Si tienes varias operaciones o valores que necesitas combinar, usarlas en una variable intermedia puede hacer que el código sea más legible.
  
- **Reusabilidad:** Puedes reutilizar la variable intermedia en varios puntos del código si es necesario.
