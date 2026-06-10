"""
===============================================================================
       GUÍA PARA EL 1T2: TRASLADO DE PSEINT A PYTHON
===============================================================================
Hola muchachos. Este archivo está diseñado para que vean que Python no es
tan diferente a lo que ya saben de PSeInt. 

CONCEPTOS NUEVOS QUE VERÁN AQUÍ (Scaffolding):
1. 'import': Sirve para traer "herramientas" que no vienen activadas por defecto.
2. 'def': Sirve para crear un "bloque" de código con nombre que podemos usar luego.
3. 'if __name__ == "__main__":': Es simplemente donde el programa empieza a correr.
===============================================================================
"""

# IMPORTAR HERRAMIENTAS
import os  # 'os' nos permite darle órdenes al sistema operativo (como limpiar pantalla)

def limpiar_pantalla():
    # En PSeInt usábamos: Borrar Pantalla
    # En Python, enviamos un comando al sistema:
    if os.name == 'nt': # Si es Windows
        os.system('cls')
    else:               # Si es Mac o Linux
        os.system('clear')

def pausar():
    # Usamos input vacío para que el programa se detenga hasta que presiones Enter
    input("\n[Presiona Enter para continuar...]")

# --- EXPLICACIÓN DE VARIABLES Y TIPOS ---
def explicacion_variables():
    limpiar_pantalla()
    print("1. VARIABLES Y TIPOS DE DATOS")
    print("-----------------------------")
    # PSeInt: Definir nombre Como Cadena
    # PSeInt: nombre <- "Juan"
    
    # Python: No necesitas 'Definir', solo asignas el valor directamente.
    nombre = "Juan"         # Cadena de texto (String)
    edad = 17               # Entero (Integer)
    nota = 8.5              # Decimal (Float)
    aprobado = True         # Lógico (Boolean)
    
    print(f"Nombre: {nombre} | Edad: {edad} | Nota: {nota}")
    print("Nota: Python detecta automáticamente el tipo de dato.")
    pausar()

# --- EXPLICACIÓN DE OPERADORES ---
def explicacion_operadores():
    limpiar_pantalla()
    print("2. OPERADORES LÓGICOS Y ARITMÉTICOS")
    print("-----------------------------------")
    # Aritméticos: +, -, *, / (igual que PSeInt)
    # Exponente: ** (En PSeInt era ^)
    # División Entera: // (da el resultado sin decimales)
    
    num1 = 10
    num2 = 3
    print(f"Suma de {num1} + {num2} = {num1 + num2}")
    print(f"Potencia de {num1} a la {num2} = {num1 ** num2}")
    
    # Lógicos: and (Y), or (O), not (NO)
    tengo_hambre = True
    tengo_comida = False
    print(f"¿Como? (Hambre Y Comida): {tengo_hambre and tengo_comida}")
    pausar()

# --- EXPLICACIÓN DE CONDICIONALES ---
def explicacion_condicionales():
    limpiar_pantalla()
    print("3. CONDICIONALES (SI-ENTONCES)")
    print("------------------------------")
    # PSeInt:
    # Si edad >= 18 Entonces ... Sino ... FinSi
    
    # Python: Usa 'if' y 'else'. IMPORTANTE: Los dos puntos ':' y el espacio (sangría)
    edad = int(input("Dime tu edad: "))
    
    if edad >= 18:
        print("Eres mayor de edad.") # Esta línea tiene sangría (espacios)
    else:
        print("Eres menor de edad.")
    
    print("\n(La identación/sangría le dice a Python qué código va dentro del 'if')")
    pausar()

# --- EXPLICACIÓN DE CICLOS, CONTADORES Y ACUMULADORES ---
def explicacion_ciclos():
    limpiar_pantalla()
    print("4. CICLOS (PARA), CONTADORES Y ACUMULADORES")
    print("-------------------------------------------")
    # En PSeInt: Para i <- 1 Hasta 5 Hacer ...
    
    contador = 0    # Empieza en 0
    acumulador = 0  # Empieza en 0
    
    print("Sumaremos los números del 1 al 5:")
    
    # 'range(1, 6)' significa: empieza en 1 y llega hasta ANTES del 6.
    for i in range(1, 6):
        contador = contador + 1     # Contador
        acumulador = acumulador + i  # Acumulador
        print(f"Vuelta {i}: Contador vale {contador}, Acumulador vale {acumulador}")
    
    pausar()

# --- EXPLICACIÓN DE ARREGLOS (LISTAS) ---
def explicacion_arreglos():
    limpiar_pantalla()
    print("5. ARREGLOS / LISTAS")
    print("--------------------")
    # PSeInt: Dimension alumnos[3]
    
    # En Python se llaman 'Listas' y son muy flexibles.
    alumnos = ["Kevin", "Maria", "Jose"]
    
    print(f"El primer alumno es: {alumnos[0]}") # ¡Ojo! En Python empezamos a contar desde 0.
    print(f"Lista completa: {alumnos}")
    
    # Agregar un elemento nuevo
    nuevo = input("Agrega un nuevo alumno: ")
    alumnos.append(nuevo) # 'append' es una herramienta para añadir al final
    
    print(f"Nueva lista: {alumnos}")
    pausar()

# --- MENÚ PRINCIPAL ---
def menu():
    opcion = ""
    while opcion != "6": # Mientras la opción no sea 6
        limpiar_pantalla()
        print("   TUTORIAL INTERACTIVO PYTHON (1T2)   ")
        print("=======================================")
        print("1. Variables y Tipos de Datos")
        print("2. Operadores")
        print("3. Condicionales")
        print("4. Ciclos (Contadores/Acumuladores)")
        print("5. Arreglos (Listas)")
        print("6. Salir")
        
        opcion = input("\nElige una opción: ")
        
        if opcion == "1":
            explicacion_variables()
        elif opcion == "2":
            explicacion_operadores()
        elif opcion == "3":
            explicacion_condicionales()
        elif opcion == "4":
            explicacion_ciclos()
        elif opcion == "5":
            explicacion_arreglos()
        elif opcion == "6":
            print("¡Sigan practicando, muchachos!")
        else:
            print("Opción no válida.")
            pausar()

# INICIO DEL PROGRAMA
if __name__ == "__main__":
    menu()
