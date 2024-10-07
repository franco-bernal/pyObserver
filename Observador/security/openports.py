import requests
from requests.utils import quote
from bs4 import BeautifulSoup

# URLs a escanear
urls = [
    "https://test.pz.cl",
    "https://test.pz.cl/login",
    "https://test.pz.cl/search?q=test",
]

# Lista de posibles vectores de inyección SQL y XSS
sql_injections = ["'", " OR 1=1 --", "\" OR 1=1 --"]
xss_payloads = ['<script>alert(1)</script>', '"<svg/onload=alert(1)>']

# Guardamos los resultados para el resumen
scan_results = {
    "sql_injection": [],
    "xss": [],
    "security_headers": [],
    "redirects": []
}

# Función para probar inyecciones SQL
def test_sql_injection(url):
    for payload in sql_injections:
        encoded_payload = quote(payload)
        vulnerable_url = f"{url}{encoded_payload}"
        try:
            response = requests.get(vulnerable_url)
            if "SQL" in response.text or "sql" in response.text:
                scan_results["sql_injection"].append(f"Vulnerabilidad SQL en {url} con el payload {payload}")
        except requests.exceptions.RequestException as e:
            scan_results["sql_injection"].append(f"Error al probar SQL injection en {url}: {e}")

# Función para probar vulnerabilidades de XSS
def test_xss(url):
    for payload in xss_payloads:
        encoded_payload = quote(payload)
        try:
            response = requests.get(url, params={"q": encoded_payload})
            if payload in response.text:
                scan_results["xss"].append(f"Vulnerabilidad XSS en {url} con el payload {payload}")
        except requests.exceptions.RequestException as e:
            scan_results["xss"].append(f"Error al probar XSS en {url}: {e}")

# Función para verificar la existencia de cabeceras de seguridad
def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        missing_headers = []

        # Verificar cabeceras importantes
        if 'X-Frame-Options' not in headers:
            missing_headers.append("X-Frame-Options")
        if 'X-Content-Type-Options' not in headers:
            missing_headers.append("X-Content-Type-Options")
        if 'Content-Security-Policy' not in headers:
            missing_headers.append("Content-Security-Policy")
        if 'Strict-Transport-Security' not in headers:
            missing_headers.append("Strict-Transport-Security")

        if missing_headers:
            scan_results["security_headers"].append(f"Las siguientes cabeceras de seguridad faltan en {url}: {', '.join(missing_headers)}")
    except requests.exceptions.RequestException as e:
        scan_results["security_headers"].append(f"Error al verificar cabeceras de seguridad en {url}: {e}")

# Función para verificar redirecciones
def check_redirects(url):
    try:
        response = requests.get(url, allow_redirects=True)
        if len(response.history) > 0:
            scan_results["redirects"].append(f"El sitio {url} redirige a {response.url}")
    except requests.exceptions.RequestException as e:
        scan_results["redirects"].append(f"Error al verificar redirecciones en {url}: {e}")

# Función para generar resumen interpretado para clientes
def generate_summary():
    print("\n------ Resumen del Escaneo ------\n")
    
    if scan_results["sql_injection"]:
        print("Inyección SQL:")
        for result in scan_results["sql_injection"]:
            print(f"- {result}")
    else:
        print("Inyección SQL: No se detectaron vulnerabilidades de inyección SQL.")

    if scan_results["xss"]:
        print("\nVulnerabilidades XSS:")
        for result in scan_results["xss"]:
            print(f"- {result}")
    else:
        print("Vulnerabilidades XSS: No se detectaron vulnerabilidades de XSS.")

    if scan_results["security_headers"]:
        print("\nCabeceras de Seguridad:")
        for result in scan_results["security_headers"]:
            print(f"- {result}")
    else:
        print("Cabeceras de Seguridad: Todas las cabeceras de seguridad están presentes.")

    if scan_results["redirects"]:
        print("\nRedirecciones:")
        for result in scan_results["redirects"]:
            print(f"- {result}")
    else:
        print("Redirecciones: No se detectaron redirecciones inesperadas.")

    print("\n------ Fin del Resumen ------\n")

# Escanear todas las URLs
for url in urls:
    print(f"\nEscaneando {url}...")
    test_sql_injection(url)  # Prueba de inyecciones SQL
    test_xss(url)  # Prueba de XSS
    check_security_headers(url)  # Verificación de cabeceras de seguridad
    check_redirects(url)  # Verificación de redirecciones

# Generar el resumen interpretado
generate_summary()
