from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import telepot
import os

bot = telepot.Bot('5641283166:AAEiLUp81ecbOuE28-OEWfntiVLjGVkwbsk')
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
navegador = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
navegador.get('https://ssw.inf.br/2/rastreamento_pf?')
navegador.find_element(By.XPATH, '//*[@id="cnpjdest"]').send_keys('08276822550')
navegador.find_element(By.XPATH, '//*[@id="btn_rastrear"]').click()
sleep(2)

while True:
    navegador.refresh()
    info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
    bot.sendMessage(1167845071, f'📦O status atual da sua encomenda é:\n\n{info}')
    sleep(7200)