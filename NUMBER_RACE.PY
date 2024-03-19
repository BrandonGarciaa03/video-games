from random import randint
import os 
menu_status = true
opt_status = true 

def main_menu():
 while menu_status:
    os.system('clear')
    print("---MENU---")
    print("[1]. Play")
    print("[2]. Help")
    print("[3]. About us")
    print("[4]. Exit")
    while opt_status:
        opt = input("elija una opcion")
        if opt < 1 or opt >4:
            print("opcion no valida")
        else:
              opt_status=False  


   

    if opt == '4':
        break



#Main
os.system('clear')
print("Cargando...")
# key = input("presione lo que queira ")   esta es otra opcion para cambiar el texto de presione cualqueir tecla para contiuar 
os.system("pause")
main_menu()