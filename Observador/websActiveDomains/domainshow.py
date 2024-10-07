import asyncio
import socket

# Lista de dominios a monitorear
dominios = [
    "www.pz.cl",
    "www.brunorossi.cl",
    "www.pollini.cl",
    "www.panamajackchile.cl",
    "www.16hrs.cl",
    "www.mingo.cl",
    "www.zappa.cl"
]

# Función para verificar si un dominio está accesible en el puerto especificado (HTTP o HTTPS)
def verificar_conectividad(dominio, puerto):
    try:
        # Intentar crear una conexión al dominio y puerto con un timeout de 2 segundos
        socket.create_connection((dominio, puerto), timeout=2)
        print(f"{dominio} está accesible en el puerto {puerto}")
        return True
    except socket.error as e:
        print(f"Error al conectarse a {dominio} en el puerto {puerto}: {e}")
        return False

# Función que monitorea los dominios en los puertos 80 (HTTP) y 443 (HTTPS)
async def monitorear_dominios():
    print("Iniciando el monitoreo de dominios...")
    while True:
        for dominio in dominios:
            # Verificar conectividad en el puerto 80 (HTTP)
            if not verificar_conectividad(dominio, 80):
                print(f"ALERTA: Servidor con problemas en HTTP: {dominio}")
            
            # Verificar conectividad en el puerto 443 (HTTPS)
            if not verificar_conectividad(dominio, 443):
                print(f"ALERTA: Servidor con problemas en HTTPS: {dominio}")
        
        await asyncio.sleep(1)  # Esperar 1 segundo antes de la próxima verificación

# Ejecutar el monitoreo
if __name__ == "__main__":
    print("Iniciando la aplicación...")
    asyncio.run(monitorear_dominios())
