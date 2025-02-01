def es_hora_valida(hora):
    """Valida que la hora ingresada esté entre 0 y 23."""
    return 0 <= hora < 24

def es_edad_valida(edad):
    """Valida que la edad sea un número positivo."""
    return edad >= 0