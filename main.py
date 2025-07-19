from func import *

while True:
    limpiar_pantalla()
    menu_principal()
    try:
        opc=int(input("\nSelecciona la operacion que desea realizar: "))
        if opc == 1:
            sumar()
            input("\nPresiona una tecla para volver al menu principal.")
        elif opc == 2:
            restar()
            input("\nPresiona una tecla para volver al menu principal.")
    except:
        print("Opcion ingresada no existe")