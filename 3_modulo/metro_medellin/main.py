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