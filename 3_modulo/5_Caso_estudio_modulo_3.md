# Caso de Estudio: Sistema de Tarifas del Metro de Medellín

## Introducción
Este caso de estudio se ha modularizado en múltiples archivos para mejorar la organización y reutilización del código.

---

## Estructura del Proyecto

```
metro_medellin/
│── main.py             # Programa principal
│── tarifas.py          # Módulo para calcular tarifas
│── validaciones.py     # Módulo para validaciones de entrada
│── utilidades.py       # Módulo con funciones auxiliares
```

---

## Contenido de los Módulos

### 1. `tarifas.py` - Cálculo de tarifas
```python
# tarifas.py

def calcular_tarifa(edad, es_estudiante, hora):
    """Calcula la tarifa del metro según la edad, si es estudiante y la hora."""
    tarifa_base = 2800
    
    if edad < 5:
        return 0  # Viaje gratuito
    elif edad > 60:
        return 1500  # Tarifa adulto mayor
    elif es_estudiante:
        return 2000  # Tarifa estudiante
    
    tarifa_final = tarifa_base
    
    if hora >= 22:
        tarifa_final *= 1.2  # Recargo nocturno
    
    return round(tarifa_final, 2)
```

### 2. `validaciones.py` - Validaciones de Entrada
```python
# validaciones.py

def es_hora_valida(hora):
    """Valida que la hora ingresada esté entre 0 y 23."""
    return 0 <= hora < 24

def es_edad_valida(edad):
    """Valida que la edad sea un número positivo."""
    return edad >= 0
```

### 3. `utilidades.py` - Funciones Auxiliares
```python
# utilidades.py

def obtener_dato_numerico(mensaje, validacion):
    """Solicita un número al usuario y valida su rango."""
    while True:
        try:
            valor = int(input(mensaje))
            if validacion(valor):
                return valor
            else:
                print("Valor fuera de rango. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")
```

### 4. `main.py` - Programa Principal
```python
# main.py

import tarifas
import validaciones
import utilidades

def main():
    """Función principal del programa."""
    print("Bienvenido al sistema de tarifas del Metro de Medellín")
    
    edad = utilidades.obtener_dato_numerico("Ingrese su edad: ", validaciones.es_edad_valida)
    es_estudiante = input("¿Tiene carné de estudiante? (s/n): ").strip().lower() == 's'
    hora = utilidades.obtener_dato_numerico("Ingrese la hora del viaje (0-23): ", validaciones.es_hora_valida)
    
    tarifa = tarifas.calcular_tarifa(edad, es_estudiante, hora)
    
    print(f"La tarifa a pagar es: {tarifa} COP")

if __name__ == "__main__":
    main()
```

---

## Explicación de la Modularización

1. **`tarifas.py`**: Contiene la lógica para calcular la tarifa, asegurando un código más limpio y reutilizable.
2. **`validaciones.py`**: Se encarga de verificar que los datos ingresados por el usuario sean correctos.
3. **`utilidades.py`**: Implementa funciones auxiliares que permiten reutilizar código para solicitar y validar datos.
4. **`main.py`**: Es el punto de entrada del programa, coordina la ejecución e interactúa con el usuario.

Esta estructura modular facilita la escalabilidad y mantenimiento del código, siguiendo el principio de "Divide y vencerás".

---

## Ejecución del Programa
Para ejecutar el programa, se debe correr `main.py` desde la terminal:

```sh
python main.py
```