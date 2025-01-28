# Caso de Estudio: Sistema Simple de Préstamo Bancario

# ------------------------------
# 1. Variables: declaración, asignación y tipos de datos básicos

# Declaramos las variables que usaremos en el cálculo del préstamo.
# El monto del préstamo, la tasa de interés y el tiempo en años son todos valores numéricos.
# Usamos tipos de datos: float (para tasas y montos) y int (para tiempo)

monto_prestamo = 5000  # El monto del préstamo en dinero (float)
tasa_interes = 0.05    # Tasa de interés anual (5%) (float)
tiempo = 3             # El tiempo en años (int)

# Variables booleanas para validar si el préstamo es aprobado
es_cliente_vip = False   # Si el cliente es VIP o no
tiene_buen_historial = True  # Si el cliente tiene un buen historial crediticio

# 2. Entrada y salida de datos (`input()` y `print()`)

# Solicitamos los datos al usuario:
monto_prestamo = float(input("Introduce el monto del préstamo: "))  # Entrada de monto en formato flotante
tasa_interes = float(input("Introduce la tasa de interés anual (en decimal): "))  # Entrada de tasa de interés en formato flotante
tiempo = int(input("Introduce el tiempo del préstamo en años: "))  # Entrada del tiempo en formato entero

# Mostramos los datos ingresados:
print(f"Datos del préstamo: Monto = {monto_prestamo}, Tasa de Interés = {tasa_interes}, Tiempo = {tiempo} años")

# 3. Operaciones básicas: aritméticas, relacionales y lógicas

# Calculamos el interés simple utilizando la fórmula: I = P * r * t
interes = monto_prestamo * tasa_interes * tiempo  # Operación aritmética

# Calculamos el monto total a pagar al final del préstamo: Monto Total = P + Interés
monto_total = monto_prestamo + interes  # Operación aritmética

# Validación para asegurar que el préstamo es aprobado:
# Si el cliente es VIP o tiene buen historial, el préstamo se aprueba.
prestamo_aprobado = es_cliente_vip or tiene_buen_historial  # Operación lógica

# Operación relacional para verificar si el monto total excede un límite
limite = 5000000  # Establecemos un límite para el préstamo
excede_limite = monto_total > limite  # Operación relacional

# Mostramos los resultados:
print(f"\nInterés del préstamo: {interes}")
print(f"Monto total a pagar: {monto_total}")

# Evaluamos si el préstamo es aprobado
if prestamo_aprobado:
    print("\n¡El préstamo ha sido aprobado!")
else:
    print("\nEl préstamo no ha sido aprobado.")

# Verificamos si el monto total excede el límite
if excede_limite:
    print("\nEl monto total excede el límite permitido para este préstamo.")
else:
    print("\nEl monto total está dentro del límite permitido para este préstamo.")
