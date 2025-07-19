from func import *

while True:
    limpiar_pantalla()
    menu_principal()
    try:
        opc=pedir_entero("\nSelecciona la operacion que desea realizar: ")
        if opc == 1:
            sumar()
            pausa()
        elif opc == 2:
            restar()
            pausa()
            
        elif opc == 3:
            multiplicar()
            pausa()
            
        elif opc == 4:
            dividir()
            pausa()
            
        elif opc == 5:
            limpiar_pantalla()
            print("Saliendo del sistema...")
            input("Presiona para salir")
            sleep()
            break
    except:
        print("Opcion ingresada no existe")