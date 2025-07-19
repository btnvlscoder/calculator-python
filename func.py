import os
import time


def limpiar_pantalla():
    os.system("cls")
    
def sleep():
    time.sleep(2)
    
def pausa():
    input("\nPresiona una tecla para volver al menu principal.")

    
def menu_principal():
    limpiar_pantalla()
    print("Calculadora python")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar.")
    print("4. Dividir")
    print("5. Salir del programa")
    
def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except:
            print("Entrada invalida. Por favor, ingresa un numero entero.")

def sumar():
    limpiar_pantalla()
    n1=pedir_entero("\nIngresa el numero que deseas sumar: ")
    n2=pedir_entero(f"Ingresa el numero que deseas sumar con {n1}: ")

    resultado = (n1 + n2)
    limpiar_pantalla()
    print(f"\nLa suma de {n1} + {n2} es {resultado}.")
    
def restar():
    limpiar_pantalla()
    n1=pedir_entero("\nIngresa el numero que deseas restar: ")
    n2=pedir_entero(f"Ingresa el numero que deseas restar con {n1}: ")

    resultado = (n1 - n2)
    limpiar_pantalla()
    print(f"\nLa resta de {n1} - {n2} es {resultado}.")
    
def multiplicar():
    limpiar_pantalla()
    n1=pedir_entero("\nIngresa el numero que deseas multiplicar: ")
    n2=pedir_entero(f"Ingresa el numero que deseas multiplicar con {n1}: ")

    resultado = (n1 * n2)
    limpiar_pantalla()
    print(f"\nLa multiplicacion de {n1} * {n2} es {resultado}.")
    
def dividir():
    limpiar_pantalla()
    n1=pedir_entero("\nIngresa el numero que deseas dividir: ")
    n2=pedir_entero(f"Ingresa el numero que deseas dividir con {n1}: ")
    if n2 == 0:
        print ("No se puede dividir por 0.")
    else:
        resultado = (n1 / n2)
    limpiar_pantalla()
    print(f"\nLa division de {n1} / {n2} es {resultado}.")