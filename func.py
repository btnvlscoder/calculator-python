import os

def limpiar_pantalla():
    os.system("cls")
    
def menu_principal():
    limpiar_pantalla()
    print("Calculadora python")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar.")
    print("4. Dividir")
    print("5. Salir del programa")
    
def sumar():
    limpiar_pantalla()
    n1=int(input("\nIngresa el numero que deseas sumar: "))
    n2=int(input(f"Ingresa el numero que deseas sumar con {n1}: "))
    
    resultado = (n1 + n2)
    limpiar_pantalla()
    print(f"\nLa suma de {n1} + {n2} es {resultado}.")
    
def restar():
    limpiar_pantalla()
    n1=int(input("\nIngresa el numero que deseas restar: "))
    n2=int(input(f"Ingresa el numero que deseas sumrestarar con {n1}: "))

    resultado = (n1 - n2)
    limpiar_pantalla()
    print(f"\nLa suma de {n1} - {n2} es {resultado}.")