import os
from data.datos import lista_menu
from Programas.sumas import sumar2
# limpiar terminal
os. system("cls")

estado = True

while estado:
    print("|+---------------------------+|")
    print("|MORATAYA                 2025|")
    print("|                             |") 
    print(f"|[1]: {lista_menu[0]}      |") 
    print(f"|[2]: {lista_menu[1]}     |")
    print(f"|[3]: {lista_menu[2]}    |")
    print(F"|[4]: {lista_menu[3]}|")
    print(f"|[5]: {lista_menu[4]}                 |")
    print(f"|[0]: salir                   |")
   
    #respuesta del dato ingresado
    r = int(input("¨[?]: "))
  
    #pregunta si el dato ingresado es una opcion disponible 
    if r ==0:
        estado = False
    elif r == 1:
        sumar2()
    
    # limpiar terminal 
    #os. system("cls")

# codigo fuera del bucle, se ejecuta si el bucle deja de ser verdadero 
print("[saliendo del programa...]") 



