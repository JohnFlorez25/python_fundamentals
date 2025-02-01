# Control de Ciclos con `break` y `continue` en Python

## Introducción
Cuando trabajamos con ciclos en Python, a veces es necesario modificar su flujo de ejecución. Para esto, existen dos instrucciones clave:

- `break`: Termina el ciclo inmediatamente.
- `continue`: Salta la iteración actual y pasa a la siguiente.

En esta unidad, exploraremos su uso con ejemplos prácticos.

---

## Uso de `break`
La instrucción `break` se usa dentro de un bucle para detener su ejecución cuando se cumple una condición específica. Es útil cuando se necesita salir de un `for` o `while` antes de que finalice de forma natural.

### Ejemplo con `for`
```python
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        print("Se alcanzó el número 5, se detiene el ciclo.")
        break
```
**Salida:**
```
1
2
3
4
5
Se alcanzó el número 5, se detiene el ciclo.
```
En este caso, cuando `numero` llega a 5, el `break` termina el bucle `for` inmediatamente.

### Ejemplo con `while`
```python
contador = 1
while contador <= 10:
    print(contador)
    if contador == 6:
        print("Deteniendo el ciclo en 6.")
        break
    contador += 1
```
**Salida:**
```
1
2
3
4
5
6
Deteniendo el ciclo en 6.
```
Aquí, el `break` detiene la ejecución cuando `contador` es igual a 6.

---

## Uso de `continue`
La instrucción `continue` se usa para omitir la ejecución del código restante dentro del ciclo y pasar directamente a la siguiente iteración.

### Ejemplo con `for`
```python
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)
```
**Salida:**
```
1
3
5
7
9
```
El `continue` hace que los números pares no se impriman.

### Ejemplo con `while`
```python
contador = 0
while contador < 10:
    contador += 1
    if contador % 3 == 0:
        continue  # Salta los múltiplos de 3
    print(contador)
```
**Salida:**
```
1
2
4
5
7
8
10
```
Los múltiplos de 3 son omitidos debido al `continue`.

---

## Comparación entre `break` y `continue`

| Instrucción  | Descripción |
|-------------|-------------|
| `break`     | Finaliza el ciclo inmediatamente. |
| `continue`  | Omite la iteración actual y pasa a la siguiente. |

**Ejemplo combinado:**
```python
for numero in range(1, 10):
    if numero == 5:
        print("Se detiene el ciclo en 5.")
        break  # Termina el ciclo
    elif numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)
```
**Salida:**
```
1
3
Se detiene el ciclo en 5.
```

---

## Conclusión
Las instrucciones `break` y `continue` permiten un mayor control en la ejecución de los ciclos en Python. Se usan para optimizar el flujo de iteraciones y mejorar la eficiencia del código. Es importante utilizarlas correctamente para evitar errores lógicos en los programas.

---

## Ejercicio propuesto
Escribe un programa que solicite números al usuario y los sume. Si el usuario introduce un número negativo, el programa debe ignorarlo (`continue`). Si introduce un `0`, el programa debe terminar (`break`) y mostrar la suma total.

