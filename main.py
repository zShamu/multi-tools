from sistema import *
from redes import *
#import red

def main():
    salir = False
    while not salir: 
        print('\na- Obtener nombre de Usuario \nb- Obtener nombre de este PC y su IP \nc- Obtener nombre de otro PC mediante su IP \nd- Obtener el mac address de este equipo \ne- Obtener nombre de la red WIFI conectada \nf- Listar las redes WIFI detectas \ng- Escanear un puerto específico \nh- Escaneo de puertos de acuerdo a un rango \nx- salir')

        #Se solicita una opcion
        opcion = input('Introduzca la letra de la opción que desea ejecutar: ')

        #Switch entre opciones
        if opcion == 'a':
            username = getusername()
            print(username)

        elif opcion == 'b':
            hostinfo = gethostnameandip()
            print(f'Nombre de esta PC es: {hostinfo[1]}')
            print(f'Dirección IP de esta PC es: {hostinfo[0]}')

        elif opcion == 'c':
            direccion = input('Introduzca la dirección IPv4 (X.X.X.X) del destino: ')
            try:
                pcname = gethostnamebyip(direccion)
                print(f'El nombre de la pc con dirección {direccion} es {pcname}')
            except:
                print('Introduzca una dirección válida.')
        
        elif opcion == 'd':
            getmacaddr()

        # elif opcion == 'i':
        #     ip = input('Introduzca la dirección IPv4 (X.X.X.X) del destino: ')
        #     port = input('Introduzca el puerto a escanear: ')

        #     if portscan(ip, port): 
        #         print(f'El puerto {port} está abierto') 
        #     else: 
        #         print(f'El puerto {port} está cerrado')

        # elif opcion == 'j':
        #     ip = input('Introduzca la dirección IPv4 (X.X.X.X) del destino: ')
        #     portini = int(input('Introduzca el puerto de inicio: '))
        #     portfin = int(input('Introduzca el puerto final: '))

        #     portrangescan(ip, portini, portfin)

        elif opcion == 'x': salir = True
        else: print ("Debe introducir la letra referente a alguna de las opciones")

if __name__ == '__main__':
    main()