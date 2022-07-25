import socket
import time
import uuid
import subprocess

def gethostnameandip():
    #Obtener nombre e ip de PC host
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)

    return (ip, hostname)

def gethostnamebyip(ip: str):
    # Obtener hostname con la ip
    #'gethostbyaddr()' es un metodo que nos sirve para encontrar el hostname de una PC dado su IPv4
    hostinfo = socket.gethostbyaddr(ip)

    return hostinfo[0]

def getmacaddr():
    #Imprimimos la salida de la Dirección Mac.
    print ("La dirección MAC del equipo es : ", end="")

    #Implementamos el uso de getnode() + format(). Para obtener la dirección Mac.
    print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
    for ele in range(0,8*6,8)][::-1]))

def connectedwifi():
    # Nombre de la Red WIFI Conectada
    red = subprocess.check_output(['netsh','wlan','show','interface']).decode('utf-8',errors = 'ignore')
    red = red.replace('\r','')
    return red

def availablewifi():
    # Listar las Redes WIFI detectas
    detected = subprocess.run(["netsh", "wlan", "show", "network"], capture_output = True, text = True).stdout
    return detected 

##Escaneo de puerto
# def portscan(targetip: str, puerto: bytes):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     #Verificamos estado de puerto
#     try:
#         s.connect((targetip, puerto)) 
#         return True
#     except:
#         return False

# def portrangescan(target: str, puertoini, puertostop) -> None:
#     #Se imprime el comienzo del escaneo puerto del host.
#     targetip = socket.gethostbyname(target) 
#     print('Empezando a escanear host: ', targetip) 

#     #Iniciamos tiempo de escaneo  
#     inicia = time.time()

#     #Asignamos un rango en específico a escanear y su condición a imprimir.
#     for port in range(puertoini, puertostop): 
#         if portscan(targetip, port): 
#             print(f'El puerto {port} está abierto') 
#         else: 
#             print(f'El puerto {port} está cerrado') 
#     #Imprimimos el tiempo que ha pasado desde la ejecución del programa.
#     acaba = time.time() 
#     print(f'Timpo transcurrido {acaba-inicia:.2f} segundos')

