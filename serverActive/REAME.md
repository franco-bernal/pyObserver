# Servicio para revisar status de servidor y observar web.
desde servidor_a, monitorear servidor_b

''' Se debe puede instalar entorno virual para instalar los package '''



##### index.html | se necesita cambiar la ip | es para tener graficamente el rendimiento de las páginas
poner en servidor observador
##### servidor_a | se necesita cambiar ip.  crear venv | es para detonar acciones si el servidor se cae. se debe agregar la configuracion | es quien se conecta al websocket
poner en servidor observador
##### servidor_b | también se debe crear venv | este es el que abre la conexion websockete
poner en servidor emisor de estadisticas(servidor observado)

## Instalación

### 1. Crear el entorno virtual

Un entorno virtual te permitirá aislar las dependencias de este proyecto. Sigue estos pasos para crear y activar el entorno virtual:

#### Linux/MacOS
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Activar el entorno virtual
### En Linux/MacOS:

```bash
Copiar código
source venv/bin/activate
```
### En Windows:
```bash
Copiar código
venv\Scripts\activate
```

