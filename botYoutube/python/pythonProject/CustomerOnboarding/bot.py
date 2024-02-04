from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import requests
#para leitura de arquivos
import pandas as pd

from botcity.web.util import element_as_select

#link do botão de download do arquivo, da página:
#https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html
url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/customer-onboarding-challenge.csv'
r = requests.get(url, allow_redirects=True)
open('customer-onboarding-challenge.csv', 'wb').write(r.content)

dados = pd.read_csv('customer-onboarding-challenge.csv', sep=',')

bot = WebBot()
#se o comando abaixo for False, o navegador será aberto, caso
#contrário, ficará em segundo plano e não veremos nada
bot.headless = False
bot.browser = Browser.CHROME
bot.driver_path = ChromeDriverManager().install()

bot.browse("https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html")
#bot.browse("https://www.botcity.dev")
# Wait 3 seconds before closing
bot.wait(2000)
bot.maximize_window()
bot.wait(2000)

for colunas in dados.itertuples():
    bot.find_element('customerName', By.ID).send_keys(colunas[1])
    bot.find_element('customerID', By.ID).send_keys(colunas[2])
    bot.find_element('primaryContact', By.ID).send_keys(colunas[3])
    bot.find_element('street', By.ID).send_keys(colunas[4])
    bot.find_element('city', By.ID).send_keys(colunas[5])
    #para um tipo seletor
    state = bot.find_element(selector='state', by=By.ID)
    state = element_as_select(state)
    state.select_by_value(value=colunas[6])
    bot.find_element('zip', By.ID).send_keys(colunas[7])
    bot.find_element('email', By.ID).send_keys(colunas[8])
    #para os radiobuttons
    if colunas[9] == 'YES':
        bot.find_element('activeDiscountYes', By.ID).click()
    else:
        bot.find_element('activeDiscountNo', By.ID).click()

    #para o checkbox
    if colunas[10] == 'NO':
        bot.find_element('NDA', By.ID).click()

    bot.find_element('submit_button', By.ID).click()

bot.wait(1000)
bot.screenshot('Accuracy.png')
bot.wait(5000)

# Finish and clean up the Web Browser
# You MUST invoke the stop_browser to avoid
# leaving instances of the webdriver open
bot.stop_browser()


# def not_found(label):
#     print(f"Element not found: {label}")



