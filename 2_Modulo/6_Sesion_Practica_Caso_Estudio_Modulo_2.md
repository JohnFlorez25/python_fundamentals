# Sesión Práctica: Sistema de Tarifas del Metro de Medellín

## Objetivos de Aprendizaje
- Comprender el uso de funciones en Python
- Practicar con estructuras condicionales
- Trabajar con diferentes tipos de datos
- Implementar lógica de negocio real

## Ejercicio 1: Verificación de Tarifa Estudiante
Implementa una función que verifique si un estudiante califica para la tarifa especial basándose en múltiples criterios.

```python
def verificar_estudiante(edad, tiene_carne, promedio_notas):
    """
    Verifica si un estudiante califica para la tarifa especial.
    
    Criterios:
    - Edad entre 12 y 25 años
    - Debe tener carné vigente
    - Promedio de notas superior a 3.0
    """
    # Tu código aquí
    pass

# Casos de prueba
print(verificar_estudiante(20, True, 4.5))  # Debe retornar True
print(verificar_estudiante(30, True, 4.0))  # Debe retornar False
print(verificar_estudiante(18, False, 4.0)) # Debe retornar False
```

## Ejercicio 2: Calculadora de Descuentos
Crea una función que calcule descuentos adicionales basados en la frecuencia de uso del metro.

```python
def calcular_descuento(viajes_mes, tarifa_base):
    """
    Calcula el descuento según la cantidad de viajes mensuales:
    - 0-10 viajes: sin descuento
    - 11-20 viajes: 5% descuento
    - 21-30 viajes: 10% descuento
    - Más de 30 viajes: 15% descuento
    
    Retorna la tarifa con descuento
    """
    # Tu código aquí
    pass

# Casos de prueba
print(calcular_descuento(5, 2800))   # Debe retornar 2800
print(calcular_descuento(15, 2800))  # Debe retornar 2660
print(calcular_descuento(25, 2800))  # Debe retornar 2520
```

## Ejercicio 3: Sistema de Puntos de Fidelidad
Implementa un sistema que calcule puntos de fidelidad basados en el uso del metro.

```python
def calcular_puntos_fidelidad(viajes_mes, uso_hora_valle, pago_anticipado):
    """
    Calcula los puntos de fidelidad según:
    - Cada viaje otorga 10 puntos base
    - Viajes en hora valle (10AM-4PM) otorgan 5 puntos extra
    - Pago anticipado del mes otorga 100 puntos extra
    
    Retorna el total de puntos
    """
    # Tu código aquí
    pass

# Casos de prueba
print(calcular_puntos_fidelidad(10, True, True))    # Debe retornar 250
print(calcular_puntos_fidelidad(10, False, False))  # Debe retornar 100
```

## Ejercicio 4: Validador de Horarios Especiales
Crea una función que determine si aplica tarifa especial según el horario y día.

```python
def es_horario_especial(hora, dia_semana):
    """
    Determina si aplica tarifa especial:
    - Lunes a viernes: 10PM-4AM
    - Sábados: después de 2PM
    - Domingos: todo el día
    
    Parámetros:
    hora: int (formato 24 horas)
    dia_semana: str ('lunes', 'martes', etc.)
    
    Retorna: bool
    """
    # Tu código aquí
    pass

# Casos de prueba
print(es_horario_especial(23, "lunes"))     # Debe retornar True
print(es_horario_especial(14, "sabado"))    # Debe retornar True
print(es_horario_especial(10, "domingo"))   # Debe retornar True
print(es_horario_especial(14, "martes"))    # Debe retornar False
```

## Ejercicio 5: Integración Final
Crea un sistema completo que integre todas las funcionalidades anteriores.

```python
def calcular_tarifa_completa(edad, es_estudiante, hora, dia_semana, viajes_mes, pago_anticipado):
    """
    Calcula la tarifa final considerando todos los factores:
    - Tipo de usuario (estudiante, adulto mayor, etc.)
    - Horario especial
    - Descuentos por frecuencia
    - Puntos de fidelidad
    
    Retorna un diccionario con:
    - tarifa_final
    - puntos_ganados
    - descuento_aplicado
    """
    # Tu código aquí
    pass

# Caso de prueba
resultado = calcular_tarifa_completa(
    edad=20,
    es_estudiante=True,
    hora=15,
    dia_semana="lunes",
    viajes_mes=25,
    pago_anticipado=True
)
print(resultado)
```

## Retos Adicionales
1. Implementa un sistema de alertas que notifique cuando un usuario está cerca de alcanzar un nuevo nivel de descuento
2. Añade validación de datos para todos los inputs
3. Implementa un sistema de caducidad para los puntos de fidelidad
4. Crea un generador de reportes mensuales de uso y ahorro

## Consejos para la Resolución
- Comienza con pruebas simples y ve aumentando la complejidad
- Usa comentarios para documentar tu lógica
- Verifica los casos límite
- Considera la legibilidad del código
- Implementa manejo de errores cuando sea necesario