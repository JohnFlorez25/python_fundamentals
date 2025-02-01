# 🚇 Ejercicios Prácticos: Sistema Metro de Medellín
## Para Estudiantes de Primer Semestre

## 🎯 Objetivo
Practicar el uso de listas y matrices en Python mediante ejercicios sencillos basados en el sistema del Metro de Medellín.

## 📝 Ejercicio 1: Lista de Estaciones
**Archivo:** `estaciones.py`

### Parte 1: Crear y mostrar lista de estaciones
```python
# Crear una lista con 5 estaciones de la línea A
estaciones_linea_a = ["Niquía", "Bello", "Madera", "Acevedo", "Tricentenario"]

# Tarea 1: Imprimir todas las estaciones
def mostrar_estaciones(lista_estaciones):
    for estacion in lista_estaciones:
        print(estacion)

# Tarea 2: Contar el número de estaciones
def contar_estaciones(lista_estaciones):
    return len(lista_estaciones)
```

### Parte 2: Práctica
1. Agregar 3 estaciones más a la lista
2. Mostrar la primera y última estación
3. Buscar si una estación existe en la lista

## 📝 Ejercicio 2: Registro de Pasajeros
**Archivo:** `pasajeros.py`

```python
# Lista con el número de pasajeros por hora (6 AM a 10 AM)
pasajeros_por_hora = [100, 350, 500, 320, 150]

# Tarea 1: Calcular total de pasajeros
def calcular_total_pasajeros(lista_pasajeros):
    return sum(lista_pasajeros)

# Tarea 2: Encontrar hora más congestionada
def encontrar_hora_pico(lista_pasajeros):
    hora_pico = lista_pasajeros.index(max(lista_pasajeros))
    return hora_pico + 6  # Sumamos 6 porque empezamos a contar desde las 6 AM
```

### Práctica:
1. Calcular el promedio de pasajeros
2. Encontrar la hora con menos pasajeros
3. Mostrar las horas con más de 300 pasajeros

## 📝 Ejercicio 3: Matriz Simple de Dos Estaciones
**Archivo:** `registro_diario.py`

```python
# Matriz: 2 estaciones x 3 horas
# Cada fila es una estación, cada columna una hora
registro_pasajeros = [
    [100, 200, 150],  # Estación 1: 7AM, 8AM, 9AM
    [120, 250, 180]   # Estación 2: 7AM, 8AM, 9AM
]

# Tarea 1: Mostrar pasajeros por estación y hora
def mostrar_registro(matriz):
    for estacion in range(len(matriz)):
        print(f"Estación {estacion + 1}:")
        for hora in range(len(matriz[estacion])):
            print(f"  {hora + 7}:00 - {matriz[estacion][hora]} pasajeros")

# Tarea 2: Calcular total por estación
def total_por_estacion(matriz):
    totales = []
    for estacion in matriz:
        totales.append(sum(estacion))
    return totales
```

### Práctica:
1. Agregar una hora más (10 AM) a cada estación
2. Calcular el promedio de pasajeros por hora
3. Encontrar la hora más ocupada de cada estación

## 📝 Ejercicio 4: Precios de Tiquetes
**Archivo:** `tiquetes.py`

```python
# Lista de precios de diferentes tipos de tiquetes
precios = {
    "unitario": 2650,
    "integrado": 3400,
    "estudiante": 2450
}

# Lista de ventas por tipo
ventas = [10, 5, 8]  # unitario, integrado, estudiante

# Tarea 1: Calcular el total recaudado
def calcular_recaudo(precios_tiquetes, cantidad_ventas):
    total = 0
    tipos = list(precios_tiquetes.keys())
    for i in range(len(tipos)):
        total += precios_tiquetes[tipos[i]] * cantidad_ventas[i]
    return total
```

### Práctica:
1. Agregar un nuevo tipo de tiquete
2. Calcular el promedio de ventas
3. Encontrar el tipo de tiquete más vendido

## 🎮 Mini-Proyecto Final
Crear un programa simple que:
1. Muestre un menú con opciones:
   - Ver estaciones
   - Ver pasajeros por hora
   - Calcular total de ventas
   - Salir

```python
# main.py
def mostrar_menu():
    print("\n=== Metro de Medellín ===")
    print("1. Ver estaciones")
    print("2. Ver pasajeros por hora")
    print("3. Calcular total de ventas")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            # Llamar función de estaciones
            pass
        elif opcion == "2":
            # Llamar función de pasajeros
            pass
        elif opcion == "3":
            # Llamar función de ventas
            pass
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")
```

## 🌟 Tips para los Ejercicios

1. **Paso a Paso**
   - Primero hacer que funcione
   - Luego mejorar el código
   - Finalmente agregar características extras

2. **Pruebas Simples**
   - Probar con datos pequeños
   - Verificar resultados manualmente
   - Imprimir valores intermedios

3. **Errores Comunes**
   - Revisar índices de listas
   - Cuidar la indentación
   - Verificar tipos de datos

## ✅ Entregables

Para cada ejercicio entregar:
1. Código comentado
2. Ejemplos de uso
3. Pruebas con diferentes datos