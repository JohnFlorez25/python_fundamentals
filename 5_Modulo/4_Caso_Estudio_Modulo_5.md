# Sistema de Gestión Turística Comuna 13

## Contexto del Proyecto

La Comuna 13 de Medellín se ha transformado en uno de los destinos turísticos más importantes de la ciudad, destacándose por sus escaleras eléctricas, grafitis y tours culturales. Para gestionar mejor la información turística y el arte urbano de la zona, se necesita desarrollar un sistema que permita:

1. Gestionar los tours y guías turísticos
2. Registrar y catalogar los grafitis y sus artistas
3. Mantener estadísticas de visitantes
4. Administrar los puntos de interés

## Estructuras de Datos a Utilizar

### 1. Tuplas
Usaremos tuplas para datos que no deben modificarse, como:
- Coordenadas de puntos de interés
- Información básica de los grafitis
- Horarios establecidos de tours

### 2. Listas
Implementaremos listas para colecciones ordenadas y modificables como:
- Registro diario de visitantes
- Tours programados
- Lista de guías disponibles

### 3. Diccionarios
Utilizaremos diccionarios para relacionar información como:
- Catálogo de grafitis y sus artistas
- Información detallada de puntos de interés
- Estadísticas de visitas por tour

## Implementación Paso a Paso

### Paso 1: Definición de Puntos de Interés
```python
# Definimos puntos principales usando tuplas (latitud, longitud, nombre, descripción)
puntos_interes = [
    (6.244377, -75.569633, "Escaleras Eléctricas", "Principal atracción"),
    (6.245233, -75.569821, "Graffiti Tour Start", "Punto de inicio"),
    (6.243988, -75.569235, "Mirador", "Vista panorámica")
]

# Información detallada en diccionario
info_puntos = {
    "Escaleras Eléctricas": {
        "horario": ("06:00", "20:00"),
        "nivel_dificultad": "Bajo",
        "tiempo_estimado": 15,  # minutos
        "servicios": ["Guía", "Fotos", "Hidratación"]
    },
    "Mirador": {
        "horario": ("06:00", "18:00"),
        "nivel_dificultad": "Medio",
        "tiempo_estimado": 25,
        "servicios": ["Guía", "Fotos"]
    }
}
```

### Paso 2: Gestión de Tours y Guías
```python
# Información de guías (tuple para datos fijos)
GuiaTuristico = (
    "nombre",
    "id",
    "idiomas",
    "calificacion",
    "tours_realizados"
)

# Lista de guías activos
guias = [
    {
        "nombre": "Carlos Restrepo",
        "id": "G001",
        "idiomas": ["Español", "Inglés"],
        "calificacion": 4.8,
        "tours_realizados": 150
    },
    {
        "nombre": "Ana Martínez",
        "id": "G002",
        "idiomas": ["Español", "Inglés", "Francés"],
        "calificacion": 4.9,
        "tours_realizados": 200
    }
]

# Registro de tours diarios
tours_diarios = {
    "Graffiti Tour": {
        "duracion": 2.5,  # horas
        "precio": 50000,
        "puntos_visita": [
            "Escaleras Eléctricas",
            "Graffiti Tour Start",
            "Mirador"
        ],
        "horarios": [
            ("09:00", "11:30"),
            ("14:00", "16:30")
        ]
    }
}
```

### Paso 3: Registro de Grafitis
```python
# Catálogo de grafitis usando diccionarios
grafitis = {
    "G001": {
        "titulo": "Esperanza",
        "artista": "Arte13",
        "ubicacion": (6.244123, -75.569456),
        "fecha_creacion": "2022-03-15",
        "tematica": "Transformación social",
        "estado": "Excelente"
    },
    "G002": {
        "titulo": "Memoria",
        "artista": "ColectivoC13",
        "ubicacion": (6.244567, -75.569789),
        "fecha_creacion": "2021-11-20",
        "tematica": "Historia local",
        "estado": "Bueno"
    }
}

# Lista de artistas y sus obras
artistas = {
    "Arte13": {
        "nombre_real": "Juan Pérez",
        "obras": ["G001"],
        "estilo": "Realismo social",
        "contacto": "arte13@email.com"
    },
    "ColectivoC13": {
        "nombre_real": "Colectivo Cultural",
        "obras": ["G002"],
        "estilo": "Mixto",
        "contacto": "colectivoc13@email.com"
    }
}
```

### Paso 4: Registro de Visitantes
```python
# Estructura para registro diario de visitantes
registro_visitantes = {
    "2024-02-01": {
        "total": 245,
        "tours": {
            "Graffiti Tour": 120,
            "Tour Cultural": 85,
            "Tour Histórico": 40
        },
        "origen": {
            "Nacional": 150,
            "Internacional": 95
        }
    }
}

# Lista de registro mensual
registro_mensual = []
```

### Paso 5: Funciones de Análisis
```python
def analizar_flujo_visitantes(registro, fecha):
    """Analiza el flujo de visitantes para una fecha específica."""
    if fecha not in registro:
        return None
    
    datos = registro[fecha]
    analisis = {
        "total_visitantes": datos["total"],
        "tour_mas_popular": max(
            datos["tours"].items(),
            key=lambda x: x[1]
        )[0],
        "porcentaje_internacional": (
            datos["origen"]["Internacional"] / datos["total"]
        ) * 100
    }
    return analisis

def obtener_grafitis_por_artista(artista_id):
    """Obtiene todos los grafitis de un artista específico."""
    if artista_id not in artistas:
        return []
    
    obras_artista = artistas[artista_id]["obras"]
    detalles_obras = []
    
    for obra_id in obras_artista:
        if obra_id in grafitis:
            detalles_obras.append(grafitis[obra_id])
    
    return detalles_obras

def calcular_estadisticas_guia(guia_id):
    """Calcula estadísticas de desempeño de un guía."""
    for guia in guias:
        if guia["id"] == guia_id:
            return {
                "tours_mes": guia["tours_realizados"] // 12,
                "calificacion": guia["idiomas"],
                "nivel_experiencia": 
                    "Experto" if guia["tours_realizados"] > 100
                    else "Intermedio"
            }
    return None
```

## Uso del Sistema

### Ejemplo 1: Registrar Nuevo Tour
```python
def registrar_tour(fecha, tipo_tour, num_visitantes, guia_id):
    """Registra un nuevo tour realizado."""
    if fecha not in registro_visitantes:
        registro_visitantes[fecha] = {
            "total": 0,
            "tours": {},
            "origen": {"Nacional": 0, "Internacional": 0}
        }
    
    registro_visitantes[fecha]["total"] += num_visitantes
    registro_visitantes[fecha]["tours"][tipo_tour] = \
        registro_visitantes[fecha]["tours"].get(tipo_tour, 0) + num_visitantes
```

### Ejemplo 2: Actualizar Estado de Grafiti
```python
def actualizar_estado_grafiti(grafiti_id, nuevo_estado):
    """Actualiza el estado de conservación de un grafiti."""
    if grafiti_id in grafitis:
        grafitis[grafiti_id]["estado"] = nuevo_estado
        return True
    return False
```

## Ventajas del Diseño

1. **Uso de Tuplas**:
   - Coordenadas inmutables
   - Horarios fijos
   - Datos de referencia constantes

2. **Uso de Listas**:
   - Registro ordenado de eventos
   - Colecciones modificables de guías
   - Histórico de visitas

3. **Uso de Diccionarios**:
   - Acceso rápido a información
   - Relaciones entre datos
   - Estadísticas organizadas

## Extensiones Futuras

1. Integración con sistema de reservas
2. Sistema de calificación de tours
3. Mapeo interactivo de grafitis
4. Gestión de eventos especiales

## Conclusiones

Este sistema demuestra cómo diferentes estructuras de datos en Python pueden trabajar juntas para crear una solución completa. 

- Las tuplas proporcionan inmutabilidad donde es necesaria.
- Las listas ofrecen flexibilidad para colecciones cambiantes.
- Los diccionarios permiten relaciones complejas entre datos.

La implementación permite una gestión eficiente de la información turística de la Comuna 13, facilitando tanto la operación diaria como el análisis a largo plazo del impacto turístico en la zona.