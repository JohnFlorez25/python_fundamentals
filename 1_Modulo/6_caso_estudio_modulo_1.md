# Caso de Estudio: Gestión de Pacientes en un Hospital

**Contexto:**

Eres parte del equipo de desarrollo de software de un hospital en Medellín, Colombia. El hospital está comenzando a automatizar algunos de sus procesos y, como primer paso, debes desarrollar un sistema simple para gestionar los pacientes en el hospital. Este sistema debe permitir registrar la información básica de los pacientes, calcular el costo del tratamiento según la duración de la estancia y mostrar un mensaje indicando si el paciente tiene derecho a un descuento por ser adulto mayor.

## Requisitos:

**1. Entrada de Datos:**

- El sistema debe solicitar al usuario:
- El nombre del paciente.
- La edad del paciente.
- La duración de su estancia en días.
- El costo por día del tratamiento.

**2. Cálculos y Condiciones:**

- El sistema calculará el costo total del tratamiento multiplicando el número de días por el costo diario.

- **Descuento por edad:**

- - Si el paciente es mayor de 65 años, se le aplica un descuento del 10% sobre el costo total del tratamiento.
El costo total con o sin descuento será mostrado.

**3. Salida de Datos:**

- El sistema debe imprimir:
- - El nombre del paciente.
- - El costo total del tratamiento antes y después del descuento (si aplica).
- - Un mensaje que indique si el paciente tiene derecho al descuento por ser adulto mayor.

## Objetivos:

- Practicar el uso de variables para almacenar los datos.
-Utilizar operaciones aritméticas para calcular el costo total.
- Implementar una validación para aplicar el descuento basado en la edad del paciente.
Utilizar entrada y salida de datos con `input()` y `print()`.