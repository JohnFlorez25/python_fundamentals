# Caso de Estudio: Sistema de Tarifas del Metro de Medellín

## Introducción
En Medellín, el sistema de transporte público Metro de Medellín ofrece diferentes tarifas dependiendo de la edad, el tipo de usuario y el horario del servicio. Este caso de estudio presenta un programa en Python que simula la compra de un tiquete según estas condiciones.

---

## Reglas del Sistema de Tarifas
El Metro de Medellín tiene las siguientes tarifas y reglas:

1. **Tarifa plena**: Para usuarios entre 18 y 60 años, el costo es de **2800 COP**.
2. **Tarifa estudiante**: Para estudiantes con carné válido, el costo es de **2000 COP**.
3. **Tarifa adulto mayor**: Para mayores de 60 años, el costo es de **1500 COP**.
4. **Tarifa infantil**: Para menores de 5 años, el viaje es **gratuito**.
5. **Tarifa especial**: Se aplica en horario nocturno (después de las 10 PM) con un recargo del **20%** sobre la tarifa normal.

---

## Código en Python
El siguiente código implementa la lógica para calcular la tarifa según la edad, si el usuario es estudiante y la hora del viaje. Se incluyen comentarios detallados para mejorar la comprensión del código.

```python
# Programa para calcular la tarifa del Metro de Medellín

def calcular_tarifa(edad, es_estudiante, hora):
    """
    Función que calcula la tarifa del metro según la edad del usuario,
    si es estudiante y la hora del día.
    
    Parámetros:
    edad (int): Edad del usuario.
    es_estudiante (bool): Indica si el usuario es estudiante con carné válido.
    hora (int): Hora del día en formato 24 horas.
    
    Retorna:
    str: Mensaje con el costo del viaje.
    """
    tarifa_base = 2800  # Tarifa estándar para adultos
    
    # Determinar la tarifa según la edad y condición de estudiante
    if edad < 5:
        return "Viaje gratuito"  # Niños menores de 5 años viajan gratis
    elif edad >= 60:
        tarifa = 1500  # Tarifa especial para adultos mayores
    elif es_estudiante:
        tarifa = 2000  # Tarifa reducida para estudiantes con carné válido
    else:
        tarifa = tarifa_base  # Tarifa normal para adultos
    
    # Aplicar recargo nocturno si la hora es igual o mayor a 22 (10 PM)
    if hora >= 22:
        tarifa *= 1.2  # Se incrementa en un 20%
    
    return f"El costo del viaje es: {int(tarifa)} COP"

# Solicitar datos al usuario
edad = int(input("Ingrese su edad: "))  # Entrada de la edad como entero
es_estudiante = input("¿Es estudiante con carné válido? (si/no): ").strip().lower() == "si"  # Entrada de booleano
hora = int(input("Ingrese la hora del viaje (en formato 24 horas): "))  # Entrada de la hora como entero

# Calcular y mostrar la tarifa final
resultado = calcular_tarifa(edad, es_estudiante, hora)
print(resultado)
```

---

## Explicación del Código

1. **Definición de la función `calcular_tarifa()`**:
   - Se reciben tres parámetros: `edad`, `es_estudiante` y `hora`.
   - Se determina la tarifa base y se ajusta según las condiciones establecidas.
   - Si el usuario es menor de 5 años, el viaje es gratuito.
   - Si el usuario es mayor de 60 años, se aplica una tarifa reducida.
   - Si el usuario es estudiante con carné válido, también se reduce la tarifa.
   - Si el viaje es después de las 10 PM, se aplica un recargo del 20%.

2. **Entrada de Datos**:
   - Se solicita la edad del usuario como un entero.
   - Se pide si es estudiante con carné válido y se convierte la respuesta en un valor booleano.
   - Se solicita la hora del viaje en formato 24 horas.

3. **Cálculo de la tarifa**:
   - Se llama a la función `calcular_tarifa()` con los valores ingresados.
   - Se muestra el resultado final con el costo del viaje.

---

## Conclusiones
Este programa permite calcular de manera eficiente la tarifa del Metro de Medellín según diferentes criterios. Además, demuestra el uso de estructuras de control como condicionales (`if`, `elif`, `else`), operadores lógicos y relacionales, y la entrada y salida de datos en Python.