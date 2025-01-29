# Funciones en Python y su Uso con Condicionales

## Introducción
Las funciones en Python son bloques de código reutilizables que permiten estructurar programas de manera más modular y eficiente. En combinación con estructuras condicionales, las funciones pueden proporcionar una toma de decisiones automatizada según ciertas condiciones.

---

## Definición de Funciones
Una función en Python se define con la palabra clave `def`, seguida del nombre de la función y los parámetros entre paréntesis.

Ejemplo básico:
```python
def saludo(nombre):
    return f"Hola, {nombre}!"

print(saludo("Carlos"))
```

---

## Uso de Condicionales en Funciones
Las funciones pueden incluir sentencias condicionales (`if`, `elif`, `else`) para tomar decisiones basadas en los argumentos que reciben.

Ejemplo:
```python
def clasificar_edad(edad):
    if edad < 18:
        return "Menor de edad"
    elif 18 <= edad < 65:
        return "Adulto"
    else:
        return "Adulto mayor"

print(clasificar_edad(20))
```

En este caso, la función `clasificar_edad()` determina la categoría de una persona según su edad.

---

## Caso de Estudio: Determinación de Elegibilidad para un Descuento en Transporte
Supongamos que en una ciudad colombiana se quiere determinar si un usuario es elegible para recibir un descuento en el sistema de transporte público según su edad y si es estudiante.

```python
def calcular_descuento(edad, es_estudiante):
    if edad < 5:
        return "Viaje gratuito"
    elif edad >= 65:
        return "Descuento del 50%"
    elif es_estudiante:
        return "Descuento del 30%"
    else:
        return "Tarifa completa"

# Prueba de la función
print(calcular_descuento(20, True))
print(calcular_descuento(70, False))
```

Esta función determina el descuento aplicable a un usuario según su condición de edad y si es estudiante.

---

## Conclusión
Las funciones en Python permiten estructurar mejor los programas, facilitando su mantenimiento y reutilización. El uso de condicionales dentro de funciones ayuda a tomar decisiones dinámicamente y hacer que los programas sean más versátiles. Comprender estos conceptos es fundamental para escribir código eficiente y bien estructurado.

