# 🚇 Caso de Estudio: Sistema Metro de Medellín
## Análisis de Flujo de Pasajeros y Optimización de Rutas

## 📝 Descripción del Problema

El Metro de Medellín necesita analizar el flujo de pasajeros en sus diferentes líneas y estaciones para optimizar la frecuencia de trenes y la distribución de recursos. Se requiere un sistema que:

1. Gestione la información de las estaciones por línea
2. Analice el flujo de pasajeros por hora
3. Calcule las rutas más congestionadas
4. Determine los tiempos de espera promedio
5. Identifique las horas pico por estación

## 💾 Estructura del Proyecto

```
metro_medellin/
│
├── datos/
│   ├── estaciones.py
│   └── flujo_pasajeros.py
│
├── analisis/
│   ├── calculo_flujo.py
│   └── rutas.py
│
├── utilidades/
│   └── helpers.py
│
└── main.py
```

## 📁 Archivos y su Contenido

### 1. datos/estaciones.py
```python
"""
Módulo que contiene la información de las estaciones del Metro de Medellín
"""

# Líneas del metro (A y B)
LINEA_A = ["Niquía", "Bello", "Madera", "Acevedo", "Tricentenario", "Caribe",
           "Universidad", "Hospital", "Prado", "Parque Berrío", "San Antonio",
           "Alpujarra", "Exposiciones", "Industriales", "Poblado", "Aguacatala",
           "Ayurá", "Envigado", "Itagüí", "Sabaneta", "La Estrella"]

LINEA_B = ["San Antonio", "Cisneros", "Suramericana", "Estadio", "Floresta",
           "Santa Lucía", "San Javier"]

# Matriz de conexiones entre estaciones (1: conectadas, 0: no conectadas)
CONEXIONES = [
    [1, 1, 0, 0, 0],  # Ejemplo simplificado
    [1, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 1, 1]
]

# Tiempos promedio entre estaciones en minutos
TIEMPOS_ENTRE_ESTACIONES = {
    ("Niquía", "Bello"): 3,
    ("Bello", "Madera"): 4,
    # ... más tiempos
}
```

### 2. datos/flujo_pasajeros.py
```python
"""
Módulo que contiene los datos de flujo de pasajeros
"""

# Matriz de flujo de pasajeros por hora y estación
# Filas: horas (6am-10pm)
# Columnas: estaciones
FLUJO_PASAJEROS = [
    [100, 150, 200, 300, 250],  # 6am
    [500, 600, 700, 800, 750],  # 7am
    [800, 900, 1000, 1200, 1100],  # 8am
    # ... más horas
]

# Horas pico definidas
HORAS_PICO = [
    (6, 9),   # Mañana
    (16, 19)  # Tarde
]

# Capacidad máxima por estación
CAPACIDAD_ESTACIONES = {
    "San Antonio": 5000,
    "Parque Berrío": 4000,
    # ... más estaciones
}
```

### 3. analisis/calculo_flujo.py
```python
"""
Módulo para análisis de flujo de pasajeros
"""
import numpy as np
from datos.flujo_pasajeros import FLUJO_PASAJEROS, HORAS_PICO

def calcular_flujo_hora_pico(matriz_flujo):
    """
    Calcula el flujo promedio en horas pico
    """
    matriz = np.array(matriz_flujo)
    horas_pico_manana = matriz[6:9]  # 6am-9am
    horas_pico_tarde = matriz[16:19]  # 4pm-7pm
    
    promedio_manana = np.mean(horas_pico_manana, axis=0)
    promedio_tarde = np.mean(horas_pico_tarde, axis=0)
    
    return promedio_manana, promedio_tarde

def identificar_estaciones_saturadas(flujo_actual, capacidad):
    """
    Identifica estaciones que superan su capacidad
    """
    estaciones_saturadas = []
    for estacion, cap in capacidad.items():
        if flujo_actual.get(estacion, 0) > cap:
            estaciones_saturadas.append(estacion)
    return estaciones_saturadas

def calcular_distribucion_carga():
    """
    Calcula la distribución de carga por línea
    """
    matriz_flujo = np.array(FLUJO_PASAJEROS)
    carga_total = np.sum(matriz_flujo, axis=0)
    return carga_total
```

### 4. analisis/rutas.py
```python
"""
Módulo para análisis de rutas
"""
from datos.estaciones import CONEXIONES, TIEMPOS_ENTRE_ESTACIONES

def encontrar_ruta_optima(origen, destino, conexiones):
    """
    Implementa algoritmo para encontrar la ruta más eficiente
    """
    # Implementación de algoritmo de búsqueda de ruta
    # (por ejemplo, Dijkstra)
    pass

def calcular_tiempo_ruta(ruta):
    """
    Calcula el tiempo total de una ruta
    """
    tiempo_total = 0
    for i in range(len(ruta)-1):
        tiempo_total += TIEMPOS_ENTRE_ESTACIONES.get((ruta[i], ruta[i+1]), 0)
    return tiempo_total

def analizar_congestion_ruta(ruta, flujo_actual):
    """
    Analiza el nivel de congestión en una ruta
    """
    nivel_congestion = []
    for estacion in ruta:
        nivel_congestion.append(flujo_actual.get(estacion, 0))
    return nivel_congestion
```

### 5. utilidades/helpers.py
```python
"""
Módulo con funciones de utilidad
"""
import numpy as np
from datetime import datetime, time

def formatear_hora(hora_24):
    """
    Convierte hora formato 24 a formato 12 horas
    """
    return time(hour=hora_24).strftime("%I:%M %p")

def calcular_promedio_movil(datos, ventana=3):
    """
    Calcula el promedio móvil de una serie de datos
    """
    return np.convolve(datos, np.ones(ventana)/ventana, mode='valid')

def generar_reporte(datos, formato="texto"):
    """
    Genera un reporte en el formato especificado
    """
    if formato == "texto":
        return "\n".join([f"{k}: {v}" for k, v in datos.items()])
    # Agregar más formatos según necesidad
```

### 6. main.py
```python
"""
Módulo principal que integra todas las funcionalidades
"""
from datos import estaciones, flujo_pasajeros
from analisis import calculo_flujo, rutas
from utilidades import helpers

def main():
    # Análisis de flujo en horas pico
    flujo_manana, flujo_tarde = calculo_flujo.calcular_flujo_hora_pico(
        flujo_pasajeros.FLUJO_PASAJEROS
    )
    
    # Identificar estaciones saturadas
    estaciones_saturadas = calculo_flujo.identificar_estaciones_saturadas(
        dict(zip(estaciones.LINEA_A, flujo_manana)),
        flujo_pasajeros.CAPACIDAD_ESTACIONES
    )
    
    # Análisis de distribución de carga
    distribucion = calculo_flujo.calcular_distribucion_carga()
    
    # Generar reporte
    reporte = {
        "Flujo Promedio Mañana": flujo_manana.tolist(),
        "Flujo Promedio Tarde": flujo_tarde.tolist(),
        "Estaciones Saturadas": estaciones_saturadas,
        "Distribución de Carga": distribucion.tolist()
    }
    
    print(helpers.generar_reporte(reporte))

if __name__ == "__main__":
    main()
```

## 🔍 Uso del Sistema

### Ejemplo 1: Análisis de Flujo en Hora Pico
```python
from analisis.calculo_flujo import calcular_flujo_hora_pico
from datos.flujo_pasajeros import FLUJO_PASAJEROS

flujo_manana, flujo_tarde = calcular_flujo_hora_pico(FLUJO_PASAJEROS)
print(f"Flujo promedio mañana: {flujo_manana}")
print(f"Flujo promedio tarde: {flujo_tarde}")
```

### Ejemplo 2: Identificación de Rutas Congestionadas
```python
from analisis.rutas import analizar_congestion_ruta
from datos.estaciones import LINEA_A

ruta = ["Niquía", "Bello", "Madera"]
congestion = analizar_congestion_ruta(ruta, {"Niquía": 500, "Bello": 700, "Madera": 600})
print(f"Niveles de congestión en la ruta: {congestion}")
```

### Ejemplo 3: Generación de Reportes
```python
from utilidades.helpers import generar_reporte

datos_reporte = {
    "Estación más congestionada": "San Antonio",
    "Hora pico máxima": "7:30 AM",
    "Flujo máximo": 1200
}

print(generar_reporte(datos_reporte))
```

## 📊 Análisis de Datos

El sistema permite realizar diversos análisis:

1. **Patrones de Flujo**
   - Identificación de horas pico
   - Tendencias por día de la semana
   - Flujo por estación

2. **Optimización de Recursos**
   - Distribución de personal
   - Frecuencia de trenes
   - Capacidad de estaciones

3. **Planificación**
   - Predicción de demanda
   - Mantenimiento preventivo
   - Mejoras de infraestructura

## 🔧 Extensiones Futuras

1. Integración con sistema de tiempo real
2. Análisis predictivo de flujo
3. Visualización interactiva de datos
4. API para consultas externas
5. Sistema de alertas automáticas

## 📝 Notas Técnicas

- El sistema utiliza NumPy para cálculos eficientes
- Los datos se estructuran en matrices para facilitar el análisis
- Se implementa programación modular para mejor mantenimiento
- Cada módulo tiene responsabilidades específicas
- Se incluyen docstrings y comentarios para documentación