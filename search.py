from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
service = Service(ChromeDriverManager().install()) #Instala los drivers necesarios para Chrome

driver = webdriver.Chrome(service=service) #abre el navegador

driver.get("https://www.mercadolibre.com")  # navega a la url

driver.find_element(By.ID,"MX").click() #Encontrar el pais méxico y cliquea 

buscar =  "playstation5" #termino a buscar

elemento_busqueda = driver.find_element(By.ID,"cb1-edit") #encontrar barra de busqueda
elemento_busqueda.clear()  # limpiar caja de texto
elemento_busqueda.send_keys(buscar)  # ingresar texto
elemento_busqueda.submit() #envia los datos de busqueda

driver.find_element(By.XPATH, "//button[@data-testid='action:understood-button']").click() #aceptar las cookies

driver.find_element(By.XPATH,"//span[contains(.,'Nuevo')]").click() #Encontrar el elemento de nuevo y cliquear

driver.find_element(By.XPATH,"//span[contains(.,'Distrito Federal')]").click() #Encontrar ciudad de méxico  y cliquear

driver.find_element(By.ID,":R2m55ee:-display-values").click() #Encontrar el menu para ordenar  y cliquear

driver.find_element(By.XPATH,"//span[contains(.,'Mayor precio')]").click() #Encontrar ciudad de méxico  y cliquear

elementos = driver.find_elements(By.XPATH, "//div[contains(@class,'poly-card__content')]")

for e in elementos[:5]:
    nombre = e.find_element(By.XPATH, ".//h3").text
    precio = e.find_element(By.XPATH, ".//span[contains(@class,'andes-money-amount__fraction')]").text
    print(f"Nombre:{nombre}\n Precio:{precio}")
input("...") 
