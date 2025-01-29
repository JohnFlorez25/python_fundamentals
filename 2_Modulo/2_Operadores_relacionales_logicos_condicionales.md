# Operadores Relacionales y Lógicos en Condiciones en Python

## Introducción
Los operadores relacionales y lógicos permiten construir expresiones condicionales más complejas en Python. Se utilizan principalmente dentro de sentencias `if`, `elif` y `else` para evaluar múltiples condiciones y tomar decisiones más precisas en un programa.

---

## 1. Operadores Relacionales
Los operadores relacionales comparan dos valores y devuelven un valor booleano (`True` o `False`). Estos son:

| Operador  | Descripción              | Ejemplo (`a = 5`, `b = 10`) |
|-----------|--------------------------|-----------------------------|
| `==`      | Igual a                   | `a == b` → `False`          |
| `!=`      | Diferente de              | `a != b` → `True`           |
| `>`       | Mayor que                 | `a > b` → `False`           |
| `<`       | Menor que                 | `a < b` → `True`            |
| `>=`      | Mayor o igual que         | `a >= b` → `False`          |
| `<=`      | Menor o igual que         | `a <= b` → `True`           |

### Ejemplo en un `if`:
```python
edad = 20
if edad >= 18:
    print("Eres mayor de edad")
```
Aquí, la condición `edad >= 18` devuelve `True`, por lo que se ejecuta la instrucción dentro del `if`.

---

## 2. Operadores Lógicos
Los operadores lógicos permiten combinar múltiples condiciones.

| Operador  | Descripción                      | Ejemplo (`a = 5`, `b = 10`, `c = 15`) |
|-----------|----------------------------------|--------------------------------------|
| `and`     | Devuelve `True` si ambas son `True` | `(a < b) and (b < c)` → `True`  |
| `or`      | Devuelve `True` si al menos una es `True` | `(a > b) or (b < c)` → `True`  |
| `not`     | Niega la condición               | `not (a > b)` → `True`            |

### Ejemplo con `and`, `or`, y `not`:
```python
usuario = "admin"
clave = "1234"

if usuario == "admin" and clave == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")
```
Aquí, la condición `usuario == "admin" and clave == "1234"` debe ser completamente `True` para permitir el acceso.

Otro ejemplo con `not`:
```python
activo = False
if not activo:
    print("El usuario está inactivo")
```
`not activo` invierte el valor `False` a `True`, por lo que la condición se cumple y se ejecuta el `print()`.

---

## 3. Uso combinado de operadores relacionales y lógicos
Podemos combinar estos operadores para hacer evaluaciones más avanzadas.

```python
edad = 25
trabaja = True

if edad > 18 and trabaja:
    print("Es mayor de edad y tiene empleo")
```
Aquí, `edad > 18` y `trabaja` deben ser `True` para que se ejecute el mensaje.

Otro ejemplo con `or`:
```python
nota = 85
if nota >= 90 or nota >= 80:
    print("Aprobaste con buena nota")
```
Si `nota` es mayor o igual a 90 **o** mayor o igual a 80, se ejecuta la salida.

---

## Conclusión
Los operadores relacionales y lógicos son fundamentales para la toma de decisiones en Python. Su correcto uso permite escribir programas más eficientes y estructurados. Al combinarlos dentro de condicionales, podemos evaluar múltiples escenarios y obtener un mayor control en la ejecución del código.

