import os

def getusername() -> str:
        #Almacenamos el nombre de usuario mediante la veariable 'environ'
        username = os.environ['USERNAME']
        #Imprimimos el username 
        return username