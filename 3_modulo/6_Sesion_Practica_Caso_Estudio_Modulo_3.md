# Caso de Estudio: Modularización en la Gestión de Pacientes en un Hospital

## Contexto:

Eres parte del equipo de desarrollo de software de un hospital en Medellín, Colombia. El hospital busca mejorar la gestión de sus pacientes mediante la automatización de ciertos procesos. En esta tarea, los estudiantes deberán diseñar e implementar un sistema modular que permita gestionar la información de los pacientes, calcular el costo del tratamiento y aplicar descuentos cuando corresponda.

## Requisitos del Sistema:

### **1. Modularización del Código**
El sistema debe estar estructurado en módulos separados para mejorar la organización y reutilización del código. Se sugiere dividir el sistema en los siguientes archivos Python:

1. **`main.py`**: Archivo principal que orquesta la ejecución del programa.
2. **`pacientes.py`**: Contendrá funciones relacionadas con la gestión de pacientes.
3. **`calculos.py`**: Implementará las funciones para calcular costos y descuentos.
4. **`interfaz.py`**: Gestionará la entrada y salida de datos con el usuario.

### **2. Entrada de Datos:**
El sistema deberá solicitar al usuario la siguiente información:

- Nombre del paciente.
- Edad del paciente.
- Duración de la estancia en días.
- Costo por día del tratamiento.

### **3. Procesamiento y Cálculos:**

- El sistema calculará el costo total del tratamiento multiplicando el número de días por el costo diario.
- Si el paciente tiene **más de 65 años**, se aplicará un **descuento del 10%** sobre el costo total.
- Se deben implementar estructuras de control como **ciclos `for` o `while`** para manejar múltiples pacientes.
- Se hará uso de **`break` y `continue`** cuando sea necesario para mejorar la lógica de entrada de datos.

### **4. Salida de Datos:**

El sistema debe mostrar la siguiente información:

- Nombre del paciente.
- Costo total del tratamiento antes y después del descuento (si aplica).
- Un mensaje indicando si el paciente tiene derecho al descuento por ser adulto mayor.

## **Objetivos de Aprendizaje:**

- Aplicar el principio de **modularización** en Python.
- Implementar **ciclos `for` y `while`** para el manejo de múltiples pacientes.
- Usar **`break` y `continue`** para optimizar la lógica de entrada de datos.
- Dividir el código en archivos separados para mejorar su organización y mantenimiento.

---

## **Tareas para los Estudiantes:**

1. **Diseñar los módulos sugeridos (`pacientes.py`, `calculos.py`, `interfaz.py`)** y definir qué funciones deben incluir.
2. **Escribir el código en cada módulo, asegurándose de cumplir con los requisitos.**
3. **Usar ciclos `for` o `while`** para permitir el registro de múltiples pacientes.
4. **Utilizar `break` y `continue`** donde sea necesario para manejar errores en la entrada de datos.
5. **Probar el sistema en `main.py`** e integrar los módulos correctamente.

---

## **Guía para la Solución**

Para ayudar en el diseño del sistema, se sugieren algunas funciones clave que podrían implementarse en los módulos:

### **Módulo `pacientes.py`**
- `registrar_paciente()`: Solicita y almacena los datos de un paciente.
- `mostrar_informacion_paciente(paciente)`: Muestra la información del paciente.

### **Módulo `calculos.py`**
- `calcular_costo(estancia, costo_diario)`: Calcula el costo total sin descuento.
- `aplicar_descuento(costo, edad)`: Aplica el descuento si el paciente es mayor de 65 años.

### **Módulo `interfaz.py`**
- `solicitar_datos()`: Solicita los datos de entrada al usuario y los devuelve en un diccionario.
- `mostrar_resultados(paciente, costo_total, descuento_aplicado)`: Presenta los resultados en pantalla.

Los estudiantes deberán estructurar y codificar la solución en función de estos lineamientos, asegurándose de aplicar correctamente la modularización y las estructuras de control en Python.