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