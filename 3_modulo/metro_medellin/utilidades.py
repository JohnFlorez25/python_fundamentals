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