from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import requests

#link do botão de download do arquivo, da página:
#https://developer.automationanywhere.com/challenges/automationanywherelabs-customeronboarding.html
url = 'https://aai-devportal-media.s3.us-west-2.amazonaws.com/challenges/customer-onboarding-challenge.csv'
r = requests.get(url, allow_redirects=True)
open('customer-onboarding-challenge.csv', 'wb').write(r.content)


# bot = WebBot()
#se o comando abaixo for False, o navegador será aberto, caso
#contrário, ficará em segundo plano e não veremos nada
# bot.headless = False
# bot.browser = Browser.CHROME
# bot.driver_path = ChromeDriverManager().install()
# bot.browse("https://www.botcity.dev")
# Wait 3 seconds before closing
# bot.wait(3000)
# bot.maximize_window()
# bot.wait(3000)
# Finish and clean up the Web Browser
# You MUST invoke the stop_browser to avoid
# leaving instances of the webdriver open
# bot.stop_browser()


def not_found(label):
    print(f"Element not found: {label}")



