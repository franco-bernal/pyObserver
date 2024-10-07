import requests

# Lista de configuraciones a probar (bots, origen, navegador, IP bloqueada, cabeceras adicionales, etc.)
configuraciones = [
    {"name": "Solicitud normal", "headers": {}},
    {"name": "GoogleBot", "headers": {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}},
    {"name": "AdsBot-Google", "headers": {"User-Agent": "Mozilla/5.0 (compatible; AdsBot-Google; +http://www.google.com/adsbot.html)"}},
    {"name": "Simulación de origen desde google.com", "headers": {"Origin": "https://google.com"}},
    {"name": "Solicitud desde un navegador", "headers": {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}},
    {"name": "Simulación de navegador móvil", "headers": {"User-Agent": "Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PPR1.180610.009) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36"}},

    # Nuevas cabeceras y configuraciones adicionales
    {"name": "Solicitud con Referer", "headers": {"Referer": "https://google.com"}},
    {"name": "Solicitud con X-Requested-With", "headers": {"X-Requested-With": "XMLHttpRequest"}},
    {"name": "Simulación de IP bloqueada", "headers": {"X-Forwarded-For": "192.168.1.1"}},
    {"name": "Cloudflare-Challenge", "headers": {"User-Agent": "Mozilla/5.0 (compatible; Cloudflare-Challenge; +https://www.cloudflare.com/)"}},

    # Diferentes métodos HTTP
    {"name": "Solicitud POST en vez de GET", "method": "post", "headers": {}},
    
    # Cache-Control y Retry-After
    {"name": "Cache-Control: No-Cache", "headers": {"Cache-Control": "no-cache"}},
    {"name": "Simulación Retry-After", "headers": {"Retry-After": "5"}},

    # Simulación de conexión lenta (esto simula un tiempo de espera en la respuesta)
    {"name": "Conexión lenta simulada", "headers": {}, "timeout": 10},

    # Cambiar de HTTP/1.1 a HTTP/2
    {"name": "Solicitud con HTTP/1.1", "headers": {"Connection": "keep-alive"}},
    {"name": "Solicitud con HTTP/2", "headers": {"Upgrade": "h2c"}},

    # Cambiar el tipo de contenido en la solicitud
    {"name": "Solicitud con Content-Type application/json", "headers": {"Content-Type": "application/json"}},
    {"name": "Solicitud con Content-Type text/html", "headers": {"Content-Type": "text/html"}},

    # Prueba de idioma
    {"name": "Solicitud con idioma español", "headers": {"Accept-Language": "es-ES,es;q=0.9"}},
    {"name": "Solicitud con idioma inglés", "headers": {"Accept-Language": "en-US,en;q=0.9"}},

    # Combinaciones avanzadas
    {"name": "Combinación avanzada con cache y idioma", "headers": {
        "Cache-Control": "no-store",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }}
]

# URL que deseas verificar
url = "https://test.pz.cl"

# Verifica el estado HTTP para cada configuración
for config in configuraciones:
    try:
        method = config.get("method", "get")
        timeout = config.get("timeout", 5)
        response = requests.request(method, url, headers=config["headers"], timeout=timeout)
        print(f"{response.status_code} | {config['name']} - Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error en {config['name']}: {e}")
