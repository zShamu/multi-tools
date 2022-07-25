from sistema import *
from red import *
#import red

def main():
    salir = False
    while not salir: 
        print('\na- Nombre del PC y su IP \nb- Nombre de otro PC \nc- Nombre de Usuario \nd- Escaneo de Puertos de acuerdo con un rango \ne- Escanear un puerto específico \nf- Cifrar y descifrar un texto generando la llave automáticamente \ng- Cifrar y descifrar un texto solicitando la llave \nh- Obtener el mac address del equipo \ni- Nombre de la Red WIFI Conectada \nj- Listar las Redes WIFI detectas \nx- salir')
        opcion = input('Introduzca la letra de la opción que desea ejecutar: ')
        if opcion == 'a':
            username = getusername()
            print(username)
        elif opcion == 'x': salir = True
        else: print ("Debe introducir la letra referente a alguna de las opciones")

if __name__ == '__main__':
    main()

    """
    try:
        #'gethostbyaddr()' es un metodo que nos sirve para encontrar el hostname de una PC dado su IPv4
        hostinfo = socket.gethostbyaddr(ip)
        print(f'Hostname: {hostinfo[0]}') 
    except:
        print("** ERROR ** \nNo se pudo resolver el nombre del Host")
    """