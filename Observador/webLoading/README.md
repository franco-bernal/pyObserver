
# Monitor de Carga de Páginas con Playwright

Este proyecto mide el tiempo de carga de una página web cada 1 minuto utilizando **Playwright** en modo **headless**.

## Requisitos

- **Python 3.7+** instalado en tu sistema.
- **pip** (viene con Python).

## Instalación

### 1. Clonar el repositorio (o descargar los archivos)

Descarga o clona este proyecto en tu máquina local.

```bash
git clone https://github.com/usuario/tu-repo.git
cd tu-repo
```

### 2. Crear un entorno virtual (venv)

Un entorno virtual te permite aislar las dependencias del proyecto.

#### En **Linux/macOS**:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### En **Windows**:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las dependencias del proyecto

Con el entorno virtual activado, instala **Playwright** y sus dependencias necesarias:

```bash
pip install playwright
```

Después de instalar Playwright, ejecuta el siguiente comando para instalar los navegadores necesarios:

```bash
playwright install
```

Esto instalará automáticamente los navegadores necesarios (Chromium, Firefox, WebKit) en modo headless.

### 4. Ejecutar el script

Para ejecutar el script que mide el tiempo de carga de la página web, asegúrate de estar en el directorio del proyecto con el entorno virtual activado y ejecuta el siguiente comando:

```bash
python cargaDePagina.py
```

El script medirá el tiempo de carga de la URL definida y la imprimirá en la consola cada 1 minuto.

## Desactivar el entorno virtual

Una vez que termines de trabajar, puedes desactivar el entorno virtual con el siguiente comando:

```bash
deactivate  # Linux/macOS
```

```bash
venv\Scripts\deactivate.bat  # Windows
```

