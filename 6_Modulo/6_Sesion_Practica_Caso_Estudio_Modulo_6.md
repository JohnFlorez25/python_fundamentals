# Sesión Práctica Módulo 6: Extensiones Pony Fútbol

## Estructura de Carpetas Propuesta

```
pony_futbol/
│
├── modelos/
│   ├── __init__.py
│   ├── persona.py         # Clase base existente
│   ├── jugador.py        # Clase existente
│   ├── equipo.py         # Clase existente
│   ├── partido.py        # Clase existente
│   ├── arbitro.py        # ¡NUEVO!
│   └── premio.py         # ¡NUEVO!
│
├── servicios/
│   ├── __init__.py
│   ├── eliminatorias.py  # ¡NUEVO!
│   ├── estadisticas.py   # ¡NUEVO!
│   └── premiacion.py     # ¡NUEVO!
│
├── util/
│   ├── __init__.py
│   ├── menu.py          # ¡NUEVO! Gestión de menús por consola
│   └── validacion.py    # ¡NUEVO! Validación de entradas
│
└── main.py
```

## 1. Sistema de Eliminatorias
### Archivo: servicios/eliminatorias.py

Este módulo debe gestionar las fases eliminatorias del torneo. Piensa en:
- Octavos de final
- Cuartos de final
- Semifinal
- Final

```python
# eliminatorias.py
class SistemaEliminatorias:
    """
    Tu tarea:
    1. Crear método para generar llaves (equipos que se enfrentan)
    2. Manejar el avance de equipos ganadores
    3. Controlar resultados de cada fase
    """
    def __init__(self, equipos_clasificados):
        # Aquí debes inicializar las estructuras necesarias
        pass
    
    def generar_llaves(self):
        # Implementa la lógica para emparejar equipos
        pass
    
    def registrar_resultado(self, partido):
        # Registra el ganador y actualiza la siguiente fase
        pass
    
    def obtener_proxima_fase(self):
        # Retorna los partidos de la siguiente fase
        pass

# ¡Ahora es tu turno!
# Sugerencia: Usa listas o diccionarios para manejar las fases
```

## 2. Gestión de Árbitros
### Archivo: modelos/arbitro.py

Los árbitros son parte fundamental del torneo. Necesitamos gestionar:
- Información personal
- Partidos asignados
- Reportes de tarjetas

```python
# arbitro.py
from .persona import Persona

class Arbitro(Persona):
    """
    Tu tarea:
    1. Heredar correctamente de Persona
    2. Agregar atributos específicos de árbitros
    3. Crear métodos para gestión de partidos
    """
    def __init__(self, nombre, documento, fecha_nacimiento):
        # Completa el constructor
        pass
    
    def asignar_partido(self, partido):
        # Implementa la asignación a un partido
        pass
    
    def registrar_tarjeta(self, jugador, tipo_tarjeta, minuto):
        # Implementa el registro de tarjetas
        pass

# ¡Ahora es tu turno!
# Sugerencia: Piensa qué información necesita un árbitro
```

## 3. Sistema de Premiaciones
### Archivo: servicios/premiacion.py

Necesitamos gestionar diferentes premios como:
- Goleador del torneo
- Mejor portero
- Juego limpio
- Mejor jugador

```python
# premiacion.py
class SistemaPremios:
    """
    Tu tarea:
    1. Definir tipos de premios
    2. Crear método para calcular ganadores
    3. Generar reportes de premiación
    """
    def __init__(self):
        # Inicializa las estructuras para premios
        pass
    
    def actualizar_estadisticas(self, partido):
        # Actualiza estadísticas relevantes para premios
        pass
    
    def determinar_ganadores(self):
        # Calcula los ganadores de cada categoría
        pass

# ¡Ahora es tu turno!
# Sugerencia: Usa diccionarios para llevar el conteo
```

## 4. Reportes Estadísticos
### Archivo: servicios/estadisticas.py

Necesitamos generar reportes sobre:
- Goles por equipo
- Tarjetas
- Rendimiento de jugadores
- Asistencia a partidos

```python
# estadisticas.py
class GeneradorEstadisticas:
    """
    Tu tarea:
    1. Crear diferentes tipos de reportes
    2. Calcular estadísticas por equipo/jugador
    3. Generar resúmenes del torneo
    """
    def generar_reporte_equipo(self, equipo):
        # Genera estadísticas de un equipo
        pass
    
    def generar_reporte_jugador(self, jugador):
        # Genera estadísticas de un jugador
        pass
    
    def generar_reporte_torneo(self):
        # Genera resumen general del torneo
        pass

# ¡Ahora es tu turno!
# Sugerencia: Organiza los datos en formato fácil de leer
```

## 6. Módulo Principal: Menú

Este módulo gestionará la interacción con el usuario a través de la consola.

```python
# util/menu.py
class MenuConsola:
    def __init__(self):
        self.opciones = {
            1: ("Ver Equipos", self.mostrar_equipos),
            2: ("Ver Eliminatorias", self.mostrar_eliminatorias),
            3: ("Gestionar Árbitros", self.menu_arbitros),
            4: ("Ver Premiaciones", self.mostrar_premiaciones),
            5: ("Generar Reportes", self.menu_reportes),
            6: ("Salir", exit)
        }
    
    def mostrar_menu(self):
        while True:
            print("\n=== TORNEO PONY FÚTBOL ===")
            for key in self.opciones:
                print(f"{key}. {self.opciones[key][0]}")
            
            try:
                opcion = int(input("\nSeleccione una opción: "))
                if opcion in self.opciones:
                    self.opciones[opcion][1]()
                else:
                    print("Opción no válida")
            except ValueError:
                print("Por favor, ingrese un número válido")
```

## 7. Archivo Principal

```python
### main.py
from util.menu import MenuConsola
from modelos.arbitro import Arbitro
from servicios.eliminatorias import SistemaEliminatorias
from servicios.premiacion import SistemaPremios
from servicios.estadisticas import GeneradorEstadisticas

def main():
    menu = MenuConsola()
    print("¡Bienvenido al Sistema de Gestión del Torneo Pony Fútbol!")
    menu.mostrar_menu()

if __name__ == "__main__":
    main()
```

## Reglas de Negocio Básicas

1. **Sistema de Menús**:
   - Menús claros y numerados
   - Validación de entradas
   - Opción para volver al menú anterior
   - Mensajes de confirmación

2. **Gestión de Datos**:
   - Validación antes de guardar
   - Confirmación de cambios importantes
   - Mensajes de error claros
   - Persistencia de datos entre sesiones