from botcity.core import DesktopBot
import pandas as pd

def not_found(label):
    print(f"Element not found: {label}")

dados = pd.read_excel('H:\\Dados\\MEU_PC\\Meusdoc\\UDEMY\RPA\\repositorio\\Contoso+Coffee+Shop+Invoices.xlsx')

bot = DesktopBot()

path_app = "C:/Program Files (x86)/Contoso, Inc/Contoso Invoicing/LegacyInvoicingApp.exe";

bot.execute(path_app)
bot.wait(5000)
bot.maximize_window()

bot.wait(1000)

if not bot.find( "invoices", matching=0.97, waiting_time=10000):
    not_found("invoices")
bot.click()

def cadastroFaturas(data, conta, contato, valor, status):
    
    if not bot.find( "new", matching=0.97, waiting_time=10000):
        not_found("new")
    bot.click()
    
    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(73, 6)

    #linhas digitadas manualmente
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    bot.paste(data)

    bot.tab()
    bot.paste(conta)

    bot.tab()
    bot.paste(contato)

    bot.tab()
    bot.paste(valor)

    if not bot.find( "status-inicio", matching=0.97, waiting_time=10000):
        not_found("status-inicio")
    bot.click_relative(64, 9)

    coluna = status

    if coluna == "Uninvoiced":
        if not bot.find( "Uninvoiced", matching=0.97, waiting_time=10000):
            not_found("Uninvoiced")
        bot.click_relative(79, 28)

    elif coluna == "Invoiced":
        if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
            not_found("invoiced")
        bot.click_relative(68, 49)

    else:
        if not bot.find( "paid", matching=0.97, waiting_time=10000):
            not_found("paid")
        bot.click_relative(68, 74)

for coluna in dados.itertuples():
    cadastroFaturas(str(coluna[1]), str(coluna[2]), str(coluna[3]), str(coluna[4]), str(coluna[5]))

bot.wait(1000)

if not bot.find("salvar", matching=0.97, waiting_time=10000):
    not_found("salvar")
bot.click()

# poderiamos ter feito esse mesmo codigo abaixo da seguinte maneira:
#bot.alt_f4()
if not bot.find( "fechar", matching=0.97, waiting_time=10000):
    not_found("fechar")
bot.click_relative(53, 6)