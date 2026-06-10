"""
===============================================================================
       GUÍA INTERACTIVA DE PROGRAMACIÓN: DE PSEINT A PYTHON (1T2)
===============================================================================
Python es un lenguaje de programación de alto nivel, interpretado y de
propósito general. Se caracteriza por su legibilidad y simplicidad.

Reglas y Características Básicas:
1. Identación: En Python, los espacios al inicio de la línea son obligatorios
   para definir bloques de código (en lugar de 'FinSi' o 'FinPara').
2. Sensible a Mayúsculas: 'Variable' y 'variable' son distintas.
3. Tipado Dinámico: No necesitas declarar el tipo de dato de una variable.
===============================================================================
"""

import time
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\n[Presiona Enter para continuar...]")

def intro():
    limpiar_pantalla()
    print("¡Bienvenidos muchachos del 1T2!")
    print("Hoy vamos a ver cómo lo que aprendieron en PSeInt se traduce a Python.")
    pausar()

def variables_y_tipos():
    limpiar_pantalla()
    print("--- 1. VARIABLES Y TIPOS DE DATOS ---")
    
    # PSEINT:
    # Definir nombre Como Cadena
    # nombre <- "Estudiante"
    
    # PYTHON:
    nombre = "Estudiante" # String (Texto)
    edad = 18            # Integer (Entero)
    promedio = 9.5       # Float (Decimal)
    es_estudiante = True # Boolean (Lógico)

    print(f"En Python no usamos 'Definir'. Simplemente asignamos:")
    print(f"nombre = '{nombre}' (Tipo: {type(nombre).__name__})")
    print(f"edad = {edad} (Tipo: {type(edad).__name__})")
    print(f"promedio = {promedio} (Tipo: {type(promedio).__name__})")
    print(f"es_estudiante = {es_estudiante} (Tipo: {type(es_estudiante).__name__})")
    
    pausar()

def operadores():
    limpiar_pantalla()
    print("--- 2. OPERADORES ---")
    
    print("Aritméticos: +, -, *, /, // (división entera), % (módulo), ** (potencia)")
    print("Lógicos: and (Y), or (O), not (NO)")
    print("Relacionales: == (Igual), != (Diferente), >, <, >=, <=")
    
    a = 10
    b = 3
    print(f"\nEjemplo: a = {a}, b = {b}")
    print(f"Suma (a + b): {a + b}")
    print(f"Potencia (a ** b): {a ** b}")
    print(f"¿Es a mayor que b? (a > b): {a > b}")
    
    pausar()

def condicionales():
    limpiar_pantalla()
    print("--- 3. CONDICIONALES ---")
    
    # PSEINT:
    # Si edad >= 18 Entonces
    #   Escribir "Eres mayor de edad"
    # Sino
    #   Escribir "Eres menor"
    # FinSi
    
    # PYTHON:
    print("PSeInt usa 'Si...Entonces...Sino...FinSi'. Python usa 'if...else:' y espacios.")
    
    user_edad = int(input("Ingresa tu edad para probar: "))
    
    if user_edad >= 18:
        print(">> Resultado: Eres mayor de edad (¡Bienvenido al club!)")
    else:
        print(">> Resultado: Eres menor de edad (Aún te falta un poco)")
    
    pausar()

def ciclos_y_contadores():
    limpiar_pantalla()
    print("--- 4. CICLOS, CONTADORES Y ACUMULADORES ---")
    
    # PSEINT (Para):
    # Para i <- 1 Hasta 5 Con Paso 1 Hacer ... FinPara
    
    print("Python usa 'for i in range(inicio, fin):' para repetir.")
    
    contador = 0
    acumulador = 0
    
    print("\nSimulando una suma de los números del 1 al 5:")
    for i in range(1, 6):
        contador += 1           # Contador: contador = contador + 1
        acumulador += i         # Acumulador: acumulador = acumulador + i
        print(f"Iteración {i}: Contador={contador}, Acumulador={acumulador}")
        time.sleep(0.5)
        
    print(f"\nTotal acumulado: {acumulador}")
    pausar()

def arreglos_listas():
    limpiar_pantalla()
    print("--- 5. ARREGLOS (LISTAS EN PYTHON) ---")
    
    # PSEINT:
    # Dimension nombres[3]
    # nombres[1] <- "Ana"
    
    # PYTHON:
    # Las listas son dinámicas y empiezan en índice 0.
    frutas = ["Manzana", "Bananos", "Uvas"]
    
    print(f"Lista original: {frutas}")
    nueva_fruta = input("Agreguemos una fruta a la lista: ")
    frutas.append(nueva_fruta)
    
    print(f"\nAhora la lista tiene {len(frutas)} elementos:")
    for i, fruta in enumerate(frutas):
        print(f" Índice {i}: {fruta}")
        
    pausar()

def main():
    while True:
        limpiar_pantalla()
        print("========================================")
        print("    MENÚ PRINCIPAL - TUTORIAL 1T2       ")
        print("========================================")
        print("1. Variables y Tipos de Datos")
        print("2. Operadores")
        print("3. Condicionales (Si/Entonces)")
        print("4. Ciclos, Contadores y Acumuladores")
        print("5. Arreglos (Listas)")
        print("6. Salir")
        
        opcion = input("\nSelecciona una opción (1-6): ")
        
        if opcion == '1': variables_y_tipos()
        elif opcion == '2': operadores()
        elif opcion == '3': condicionales()
        elif opcion == '4': ciclos_y_contadores()
        elif opcion == '5': arreglos_listas()
        elif opcion == '6': 
            print("\n¡Hasta luego, muchachos! Sigan programando.")
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

if __name__ == "__main__":
    intro()
    main()
