from os import system
system("cls")

usuario = []
datos = {}
Friends = {}
volu = {"Volumen": 50}
sensibi = {"sensibilidad": 50}
Brillo = {"Brillo": 50}

def login():
    system("cls")
    while True:
        try:
            opcion = input("""---------------Bienvenido a World Dead--------------- \n              Login \n             Register \n              salir \n = """)
            if opcion == "login":
                inicio()
            elif opcion == "register":
                register()
            elif opcion == "salir":
                break
        except:
            print("Opcion no valida")    
        finally:
            break   
def inicio():
    system("cls")
    while True:
        try:
            if input("ingrese usuario: ") != usuario[0] or str(input("ingrese password: ")) !=  usuario[1] or main():
                print("Usuario no existente")
        except:
            opcion = str(input("Usuario no existente desea volver? \n :"))
        if opcion == "si":
            login()
        elif opcion == "no":
            continue
def register():
    system("cls")
    while True:
        try:
            print("ingrese su usuario y contraseña")
            user = input(": ")
            password = input(": ")
            usuario.append(user)
            usuario.append(password)
            login()
        except:
            print("Dato no valido")
def añadir_nombre():
    system("cls")
    while True:
        try:
            cantidad = int(input("ingrese la cantidad de usuario: "))
            for i in range(cantidad):
                nombres = str(input("ingrese el nombre: "))
                uid = int(input("ingrese el Uid: "))
                datos[nombres] = uid
            opc = str(input("Desea volver al menu? \n: "))
            if opc == "si":
                main()
            elif opc == "no":
                añadir_nombre()
        except:
            opcion = str(input("Dato no valido desea volver? \n :"))
            if opcion == "si":
                main()
            elif opcion == "no":
                continue
def modificar():
    system("cls")
    while True:
        try:
            pregunta = str(input("Cual nombre desea modificar?: "))
            new_name = str(input("ingrese el nuevo nombre: "))
            datos[new_name] = datos[pregunta]
            pregunta_2 = str(input("Desea modificar su numero de Documento: "))
            if pregunta_2 == "si":
                new_phone = input("ingrese el nuevo numero de Documento: ")
                datos[new_name] = new_phone
                datos.pop(pregunta)
                op = str(input("Desea volver al menu? \n: "))
                if op == "si":
                    main()
                elif op == "no":
                    modificar()
            elif pregunta_2 == "no":
                main()
        except KeyError:
            print("Nombre o Documento no encontrado")
def lista():
    system("cls")
    while True:
        try:
            favorite = str(input("Lista de amigos (1)\nLista de amigos favoritos (2)\n="))
            if favorite == "1":
                lis()
            elif favorite == "2":
                lista_favorite()
        except:
            print("ERROR")
def lis():
    system ("cls")
    while True:
        try:
            print(f"los datos son \n {datos}")
            o = str(input("Desea volver al menu? \n: "))
            if o == "si":
                main()
            elif o == "no":
                lista()
        except:
            print("Dato no valido")
def lista_favorite():
    system ("cls")
    while True:
        try:
            print(f"los datos son \n {Friends}")
            o = str(input("Desea volver al menu? \n: "))
            if o == "si":
                main()
            elif o == "no":
                lista()
        except:
            print("Dato no valido")
def borrar():
    system("cls")
    while True:
        try:
            print("Que contacto desea borrar?")
            no = str(input())
            se = str(input("Estas seguro?: "))
            if se == "si":
                datos.pop(no)
                print("Desea volver al menu? \n:")
                opcion = str(input(": "))
                if opcion =="si":
                    main()
                elif opcion == "no":
                    borrar()
        except:
            opcion = str(input("Dato no existente desea volver? \n :"))
            if opcion == "si":
                main()
            elif opcion == "no":
                continue
def buscar():
    system("cls")
    while True:
        try:
            print(f"{datos}\n{datos}")
            p = input("Escriba el contacto que desea buscar\n: ")
            u = int(input("Escriba el Uid\n: "))
            if u != datos[p]:
                print("El Uid no coinside")
                buscar()
            try:
                print(f"nombre: {p} Uid: {datos[p]}")
            except KeyError:
                print("no se encontro el contacto")
            o = input("Desea agregarlo a favoritos? \n: ")
            if o == "si":
                datos.pop(p)
                Friends[p] = u
                main()
            elif o == "no":
                main()
        except:
            opcion = str(input("Persona no encontrada desea volver? \n :"))
            if opcion == "si":
                main()
            elif opcion == "no":
                continue
def opciones():
    system ("cls")
    while True:
        try:
            opc = str(input("------Opciones------\n---Volumen      (1)---\n---sensibilidad (2)---\n---brillo       (3)--- \n---salir        (4)\nElija una opcion \n="))
            if opc == "1":
                volumen()
            elif opc == "2":
                sensibilidad()
            elif opc == "3":
                brillo()
            elif opc == "4":
                main()
        except:
            print("ERROR")
def volumen():
    while True:
        try:
            print(volu)
            volum = "Volumen"
            cat = int(input("cuanto volumen desea? \n ="))
            if cat > 100 and cat < 0 :
                print("")
                continue
            else:
                volu[volum] = cat
                opciones()
        except:
            break
def sensibilidad():
    while True:
        try:
            print(sensibi)
            sensi = "sensibilidad"
            cat = int(input("cuanto volumen desea? \n ="))
            if cat > 100 and cat < 0 :
                print("")
                continue
            else:
                volu[sensi] = cat
                opciones()
        except:
            break
def brillo():
    while True:
        try:
            print(Brillo)
            bri = "Brillo"
            cat = int(input("cuanto volumen desea? \n ="))
            if cat > 100 and cat < 0 :
                print("")
                continue
            else:
                volu[bri] = cat
                opciones()
        except:
            break
def main():
    system("cls")
    while True:
        try:
            print("__________________")
            print("       MENU       ")
            print("__________________")
            print("añadir amigo   (1)")
            print("modificar      (2)")
            print("lista          (3)")
            print("Borrar         (4)")
            print("Buscar         (5)")
            print("optiones       (6)")
            print("Cerrar sesion  (7)")
            opcion = str(input("Elija una opcion \n = "))
            if opcion == "1":
                añadir_nombre()
            elif opcion == "2":
                modificar()
            elif opcion == "3":
                lista()
            elif opcion == "4":
                borrar()
            elif opcion == "5":
                buscar()
            elif opcion == "7":
                login() 
            elif opcion == "6":
                opciones()
        except:
            print("Opcion no existente")   
if __name__ == "__main__":
    login()