from playwright.sync_api import sync_playwright
import time

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    url = "https://test.pz.cl/"

    while True:
        # Mide el tiempo de carga
        start_time = time.time()
        page.goto(url)
        end_time = time.time()

        # Calcula el tiempo total de carga
        total_time = end_time - start_time
        
        # Imprimir en la consola el resultado
        print(f"Tiempo de carga: {total_time:.2f} segundos - {time.ctime()}")
        
        # Pausa por 1 minuto antes de la próxima medición
        time.sleep(60)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
