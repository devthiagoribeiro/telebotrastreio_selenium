from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import telepot
import os

channelid = os.environ.get('CHANNEL_ID')
cpf = os.environ.get('CPF')
bot_token = os.environ.get('BOT_TOKEN') #telepot.Bot('5641283166:AAEiLUp81ecbOuE28-OEWfntiVLjGVkwbsk')
bot = telepot.Bot(bot_token)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
navegador = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
# navegador = webdriver.Chrome(executable_path=chromedriver_autoinstaller.install())
navegador.get('https://ssw.inf.br/2/rastreamento_pf?')
navegador.find_element(By.XPATH, '//*[@id="cnpjdest"]').send_keys(cpf)
navegador.find_element(By.XPATH, '//*[@id="btn_rastrear"]').click()
sleep(2)
while True:
    navegador.refresh()
    info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
    bot.sendMessage(channelid, f'📦O status atual da sua encomenda é:\n\n{info}')
    new_info = info
    while new_info == info:
        navegador.refresh()
        new_info = navegador.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[3]/table[2]/tbody/tr[2]/td[3]/p[1]').text
        sleep(240)