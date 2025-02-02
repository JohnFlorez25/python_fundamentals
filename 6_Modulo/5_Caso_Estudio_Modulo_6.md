# Sistema de Gestión Torneo Pony Fútbol Medellín
## Un Caso de Estudio con Programación Orientada a Objetos en Python

## Contexto del Proyecto

El Festival Pony Fútbol es uno de los torneos infantiles más importantes de Colombia, realizado en Medellín. Para gestionar este torneo, necesitamos un sistema que permita administrar equipos, jugadores, partidos y estadísticas, implementando los principios de la programación orientada a objetos.

## Implementación del Sistema

### 1. Clase Base Persona

```python
class Persona:
    """Clase base para todas las personas relacionadas con el torneo."""
    
    def __init__(self, nombre, documento, fecha_nacimiento):
        self.__nombre = nombre
        self.__documento = documento
        self.__fecha_nacimiento = fecha_nacimiento
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def documento(self):
        return self.__documento
    
    def obtener_info(self):
        return f"Nombre: {self.__nombre}, Documento: {self.__documento}"
```

### 2. Clase Jugador

```python
class Jugador(Persona):
    """Clase para representar a un jugador del torneo."""
    
    def __init__(self, nombre, documento, fecha_nacimiento, posicion, numero):
        super().__init__(nombre, documento, fecha_nacimiento)
        self.__posicion = posicion
        self.__numero = numero
        self.__goles = 0
        self.__tarjetas_amarillas = 0
        self.__tarjetas_rojas = 0
    
    def anotar_gol(self):
        self.__goles += 1
        return f"¡Gol de {self.nombre}! Total: {self.__goles}"
    
    def recibir_tarjeta(self, tipo):
        if tipo.lower() == "amarilla":
            self.__tarjetas_amarillas += 1
        elif tipo.lower() == "roja":
            self.__tarjetas_rojas += 1
    
    def obtener_estadisticas(self):
        return {
            "goles": self.__goles,
            "amarillas": self.__tarjetas_amarillas,
            "rojas": self.__tarjetas_rojas
        }
```

### 3. Clase Equipo

```python
class Equipo:
    """Clase para gestionar un equipo participante."""
    
    def __init__(self, nombre, ciudad, categoria):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__categoria = categoria
        self.__jugadores = []
        self.__partidos_jugados = 0
        self.__victorias = 0
        self.__empates = 0
        self.__derrotas = 0
        self.__goles_favor = 0
        self.__goles_contra = 0
    
    def agregar_jugador(self, jugador):
        if len(self.__jugadores) < 18:  # Máximo 18 jugadores por equipo
            self.__jugadores.append(jugador)
            return f"{jugador.nombre} agregado al equipo {self.__nombre}"
        return "Equipo completo"
    
    def actualizar_estadisticas(self, goles_favor, goles_contra):
        self.__partidos_jugados += 1
        self.__goles_favor += goles_favor
        self.__goles_contra += goles_contra
        
        if goles_favor > goles_contra:
            self.__victorias += 1
        elif goles_favor < goles_contra:
            self.__derrotas += 1
        else:
            self.__empates += 1
    
    def obtener_puntos(self):
        return (self.__victorias * 3) + self.__empates
    
    def obtener_estadisticas(self):
        return {
            "nombre": self.__nombre,
            "PJ": self.__partidos_jugados,
            "PG": self.__victorias,
            "PE": self.__empates,
            "PP": self.__derrotas,
            "GF": self.__goles_favor,
            "GC": self.__goles_contra,
            "Puntos": self.obtener_puntos()
        }
```

### 4. Clase Partido

```python
class Partido:
    """Clase para gestionar un partido del torneo."""
    
    def __init__(self, local, visitante, fecha, estadio):
        self.__equipo_local = local
        self.__equipo_visitante = visitante
        self.__fecha = fecha
        self.__estadio = estadio
        self.__goles_local = 0
        self.__goles_visitante = 0
        self.__estado = "Programado"
        self.__incidencias = []
    
    def registrar_gol(self, jugador, minuto, equipo):
        if self.__estado == "En Juego":
            if equipo == self.__equipo_local:
                self.__goles_local += 1
            else:
                self.__goles_visitante += 1
            
            jugador.anotar_gol()
            self.__incidencias.append({
                "tipo": "Gol",
                "jugador": jugador.nombre,
                "minuto": minuto
            })
    
    def iniciar_partido(self):
        self.__estado = "En Juego"
        return f"Partido iniciado en {self.__estadio}"
    
    def finalizar_partido(self):
        self.__estado = "Finalizado"
        self.__equipo_local.actualizar_estadisticas(
            self.__goles_local, self.__goles_visitante)
        self.__equipo_visitante.actualizar_estadisticas(
            self.__goles_visitante, self.__goles_local)
        return self.obtener_resultado()
    
    def obtener_resultado(self):
        return f"{self.__equipo_local.nombre} {self.__goles_local} - {self.__goles_visitante} {self.__equipo_visitante.nombre}"
```

### 5. Clase Torneo

```python
class Torneo:
    """Clase principal para gestionar el torneo Pony Fútbol."""
    
    def __init__(self, año, sede):
        self.__año = año
        self.__sede = sede
        self.__equipos = {}
        self.__partidos = []
        self.__tabla_posiciones = []
    
    def registrar_equipo(self, equipo):
        self.__equipos[equipo.nombre] = equipo
        return f"Equipo {equipo.nombre} registrado en el torneo"
    
    def programar_partido(self, local, visitante, fecha, estadio):
        if local in self.__equipos and visitante in self.__equipos:
            partido = Partido(
                self.__equipos[local],
                self.__equipos[visitante],
                fecha,
                estadio
            )
            self.__partidos.append(partido)
            return "Partido programado exitosamente"
        return "Uno o ambos equipos no están registrados"
    
    def actualizar_tabla(self):
        self.__tabla_posiciones = sorted(
            self.__equipos.values(),
            key=lambda x: (
                x.obtener_puntos(),
                x.obtener_estadisticas()["GF"] - x.obtener_estadisticas()["GC"]
            ),
            reverse=True
        )
    
    def obtener_tabla_posiciones(self):
        self.actualizar_tabla()
        tabla = []
        for pos, equipo in enumerate(self.__tabla_posiciones, 1):
            stats = equipo.obtener_estadisticas()
            tabla.append(f"{pos}. {stats['nombre']} - {stats['Puntos']} pts")
        return tabla
```

## Ejemplo de Uso del Sistema

```python
# Crear torneo
torneo_2024 = Torneo(2024, "Medellín")

# Crear equipos
envigado = Equipo("Envigado FC", "Envigado", "Sub-12")
nacional = Equipo("Atlético Nacional", "Medellín", "Sub-12")

# Registrar equipos en el torneo
torneo_2024.registrar_equipo(envigado)
torneo_2024.registrar_equipo(nacional)

# Crear y registrar jugadores
jugador1 = Jugador("Juan Pérez", "1001", "2012-05-15", "Delantero", 9)
jugador2 = Jugador("Carlos López", "1002", "2012-03-20", "Mediocampista", 10)

envigado.agregar_jugador(jugador1)
nacional.agregar_jugador(jugador2)

# Programar partido
torneo_2024.programar_partido(
    "Envigado FC",
    "Atlético Nacional",
    "2024-02-01",
    "Polideportivo Sur"
)

# Simular partido
partido = torneo_2024.partidos[-1]
partido.iniciar_partido()
partido.registrar_gol(jugador1, 15, envigado)
partido.registrar_gol(jugador2, 30, nacional)
resultado = partido.finalizar_partido()

print(resultado)
print("\nTabla de Posiciones:")
for posicion in torneo_2024.obtener_tabla_posiciones():
    print(posicion)
```

## Funcionalidades Principales

1. **Gestión de Jugadores**:
   - Registro de datos personales
   - Seguimiento de estadísticas individuales
   - Control de tarjetas y goles

2. **Gestión de Equipos**:
   - Registro de plantilla
   - Estadísticas del equipo
   - Puntos y posición en el torneo

3. **Gestión de Partidos**:
   - Programación de encuentros
   - Registro de incidencias
   - Actualización automática de estadísticas

4. **Gestión del Torneo**:
   - Tabla de posiciones
   - Calendario de partidos
   - Estadísticas generales

## Extensiones Futuras

1. Implementar sistema de eliminatorias
2. Agregar gestión de árbitros
3. Incluir sistema de premiaciones
4. Generar reportes estadísticos
5. Implementar interfaz gráfica

Este sistema demuestra los principios fundamentales de POO:
- Encapsulamiento (atributos privados con __)
- Herencia (Jugador hereda de Persona)
- Abstracción (interfaces claras para cada clase)
- Polimorfismo (métodos como obtener_info)