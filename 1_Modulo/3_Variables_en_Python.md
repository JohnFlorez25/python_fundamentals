# Variables en Python: Declaración, Asignación y Tipos de Datos Básicos

---

## **1. ¿Qué es una Variable?**
Una variable es un contenedor para almacenar datos en la memoria del ordenador. Se utiliza para etiquetar y manipular valores durante la ejecución de un programa.

### **Características de las Variables en Python:**
- No necesitan una declaración explícita del tipo de dato (Python es un lenguaje de tipado dinámico).
- Los nombres de las variables son **sensibles a mayúsculas y minúsculas**.
- Pueden cambiar de tipo durante la ejecución del programa.

---

## **2. Declaración y Asignación**

### **Declarar una Variable**

Para declarar una variable, simplemente escribe un nombre seguido del símbolo `=` y el valor que deseas asignar.

```python
# Ejemplo de declaración y asignación
nombre = "Juan"    # Variable tipo str
edad = 25          # Variable tipo int
altura = 1.75      # Variable tipo float
es_estudiante = True  # Variable tipo bool
```

## **3. Tipos de Datos Básicos**

Python soporta varios tipos de datos básicos que puedes usar en tus programas.

### 3.1. Enteros (int)

Se utilizan para representar números enteros positivos o negativos.

```python
edad = 30
puntos = -15
print(type(edad))  # Salida: <class 'int'>
```

### 3.2. Flotantes (float)

Se utilizan para representar números decimales.

```python
altura = 1.85
pi = 3.14159
print(type(pi))  # Salida: <class 'float'>
```

### 3.3. Cadenas de Texto (str)

Se utilizan para representar texto. Se escriben entre comillas simples o dobles.

```python
mensaje = "Hola, mundo"
letra = 'A'
print(type(mensaje))  # Salida: <class 'str'>
```

### 3.4. Booleanos (bool)

Solo pueden tener los valores True o False. Son útiles para condicionales.

```python
es_mayor_de_edad = True
tiene_descuento = False
print(type(es_mayor_de_edad))  # Salida: <class 'bool'>
```

## **4. Buenas Prácticas al Nombrar Variables**

El uso de nombres claros y consistentes para las variables es esencial para escribir código legible y mantenible. A continuación, se presentan las mejores prácticas para nombrar variables en Python.

---

### **4.1. Usa nombres descriptivos**
Es importante que los nombres de las variables sean intuitivos y reflejen el propósito de la variable. Esto facilita la comprensión del código, especialmente al trabajar en equipo o revisar proyectos después de un tiempo.

```python
# Correcto
velocidad_auto = 60
distancia_recorrida = 120

# Incorrecto
x = 60
y = 120
```

### 4.2. Sigue el formato `snake_case`

En Python, las variables se nombran comúnmente siguiendo el estilo snake_case, donde las palabras se separan por guiones bajos (_). Este formato es recomendado por la [Guía de Estilo de Python PEP-8](https://peps.python.org/pep-0008/).

```python
# Correcto
total_suma = 100
contador_elementos = 25

# Incorrecto
totalSuma = 100       # Estilo camelCase
TotalSuma = 100       # Uso innecesario de mayúsculas
total-suma = 100      # Error de sintaxis
```

> Nota: El uso del formato snake_case asegura consistencia y mejora la legibilidad en el código, alineándose con los estándares de la comunidad Python.

### 4.3. Evita caracteres especiales o espacios

Los nombres de variables no deben contener caracteres especiales como guiones `(-)`, símbolos `(@, #)` o espacios. Estas prácticas causarán errores de sintaxis.


```python
# Correcto
total_suma = 100
es_mi_variable = True

# Incorrecto
total-suma = 100   # Error de sintaxis
es mi variable = True  # Error de sintaxis
```

### 4.4. Usa nombres en minúsculas

Por convención, las variables se nombran en **minúsculas**. Si una variable necesita ser más explícita, utiliza guiones bajos para separar las palabras.

```python
# Correcto
nombre_usuario = "Carlos"
edad_usuario = 30

# Incorrecto
NombreUsuario = "Carlos"  # Evita el uso de mayúsculas innecesarias
EdadUsuario = 30
```

### 4.5. Nombres de constantes en mayúsculas

Cuando declares **constantes**, utiliza letras mayúsculas y separa las palabras con guiones bajos `(_)`. Esto ayuda a diferenciar las constantes de las variables comunes.

```python
# Ejemplo de constantes
PI = 3.14159
VELOCIDAD_LUZ = 299792458  # m/s
```

### 4.6. Evita usar palabras reservadas

Python tiene palabras reservadas que no pueden usarse como nombres de variables (por ejemplo, `if, for, class`). Intentar usarlas generará errores de sintaxis.

```python
# Incorrecto
if = 10  # Error: "if" es una palabra reservada
class = "Python"  # Error: "class" es una palabra reservada

# Correcto
valor_condicional = 10
nombre_clase = "Python"
```

### 4.7. Sé consistente

Mantén un estilo uniforme para el nombrado de variables en todo tu proyecto. Esto mejora la cohesión y facilita el mantenimiento del código.

```python
# Correcto
contador = 0
suma_total = 100

# Incorrecto
contador = 0
sumaTotal = 100  # Mezcla de estilos (snake_case y camelCase)
```

### 5. Ejercicios Prácticos

1. Declara una variable para almacenar tu nombre, edad, y si eres estudiante. Imprime los valores y sus tipos.

2. Escribe un programa que calcule el perímetro de un rectángulo usando variables `base` y `altura`.

**Soluciones:**

```python
# Ejercicio 1
nombre = "Ana"
edad = 22
es_estudiante = True

print("Nombre:", nombre, "- Tipo:", type(nombre))
print("Edad:", edad, "- Tipo:", type(edad))
print("¿Es estudiante?:", es_estudiante, "- Tipo:", type(es_estudiante))

# Ejercicio 2
base = 5
altura = 10
perimetro = 2 * (base + altura)
print("El perímetro del rectángulo es:", perimetro)
```








