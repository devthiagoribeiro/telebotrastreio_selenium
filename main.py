from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import telepot
import os

ON_HEROKU = os.environ.get('ON_HEROKU')

if ON_HEROKU:
    # get the heroku port
    port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995
else:
    port = 3000

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
    while True:
        navegador.refresh()
        new_info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
        if new_info != info:
            info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
            bot.sendMessage(1167845071, f'📦O status atual da sua encomenda é:\n\n{info}')
        sleep(10)