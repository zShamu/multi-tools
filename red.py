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

#Programamos la definición del puerto de escaneo.
def portscan(targetip: str, puerto: bytes):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Verificamos estado de puerto
    try:
        s.connect((targetip, puerto)) 
        return True
    except:
        return False

def portrangescan(target: str, puerto: bytes, rango: int):
    #Se imprime el comienzo del escaneo puerto del host.
    targetip = socket.gethostbyname(target) 
    print('Empezando a escanear host: ', targetip) 

    #Iniciamos tiempo de escaneo  
    inicia = time.time()

    #Asignamos un rango en específico a escanear y su condición a imprimir.
    for puerto in range(rango): 
        if portscan(puerto): 
            print(f'El puerto {puerto} está abierto') 
        else: 
            print(f'El puerto {puerto} está cerrado') 
    #Imprimimos el tiempo que ha pasado desde la ejecución del programa.
    acaba = time.time() 
    print(f'Timpo transcurrido {acaba-inicia:.2f} segundos')


elif opcion == 'd':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        #Realizamos la primera impresión que sería el objetivo = "localhost".
        target = input('Qué quieres escanear?: ') 

        #Se imprime el comienzo del escaneo puerto del host.
        target_ip = socket.gethostbyname(target) 
        print('Empezando a escanear host:', target_ip) 
        
        #Programamos la definición del puerto de escaneo.
        def port_scan(port): 
            try: 
                s.connect((target_ip, port)) 
                return True
            except: 
                return False
        
        
        inicia = time.time() 

        #Asignamos un rango en específico a escanear y su condición a imprimir.
        for port in range(20): 
            if port_scan(port): 
                print(f'El puerto {port} está abierto') 
            else: 
                print(f'El puerto {port} está cerrado') 

        #Imprimimos el tiempo que ha pasado desde la ejecución del programa.
        acaba = time.time() 
        print(f'Timpo transcurrido {acaba-inicia:.2f} segundos')

    elif opcion == 'e':
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        #Realizamos la primera impresión que sería el objetivo = "localhost".
        target = input('Qué quieres escanear?: ') 

        #Se imprime el comienzo del escaneo puerto del host asignado.
        t_IP = socket.gethostbyname(target) 
        print("Empezando a escanear el host", t_IP) 
        
        #Programamos la definición del puerto de escaneo.
        def port_scan(port): 
            try: 
                s.connect((t_IP, port)) 
                return True
            except: 
                return False
        
        #Asignamos el puerto específico a escanear y su condición a imprimir. *135 está abierto
        port = int(input("Ingrese el numero de puerto a escanear: ")) 
        
        if port_scan(port): 
            print('Port', port, 'is open') 
        else: 
            print("port", port, "is closed")

elif opcion == 'h':
        #Imprimimos la salida de la Dirección Mac.
        print ("La Dirección MAC del equipo es : ", end="")

        #Implementamos el uso de getnode() + format(). Para obtener la dirección Mac.
        print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
        for ele in range(0,8*6,8)][::-1]))

    elif opcion == 'i':
        # Nombre de la Red WIFI Conectada
        red = subprocess.check_output(['netsh','wlan','show','interface']).decode('utf-8',errors='ignore')
        red = red.replace('\r',"")
        print(red)
    
    elif opcion == 'j':
        # Listar las Redes WIFI detectas
        redes= subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True).stdout
        print(redes)