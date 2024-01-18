from botcity.core import DesktopBot, Backend

bot = DesktopBot()
path = r'H:\\Dados\\MEU_PC\\Meusdoc\\UDEMY\\RPA\\repositorio\\rpa\\botYoutube\\python\\pythonProject\\MyCRM\\app\\MyCRM.exe'

bot.execute(path)
bot.wait(1000)
# UIA é a forma de conexão, que depende do software e do seu SO
bot.connect_to_app(backend=Backend.UIA, path=path)

main_window = bot.find_app_window(title='My CRM (Sample App)')
main_window.menu_select('File -> Clear fields')
main_window.type_keys('%{t} Charles')
main_window.type_keys('%{l} Lima')

#este comando mostra todos os comandos que podemos acessar
#print(main_window.print_control_identifiers())

#genero
main_window.Male.click()

#Cidade
main_window.Edit10.type_keys('Fortaleza')

#Troca de formulários
main_window.Company.select()
main_window.Other.select()
main_window.People.select()
main_window.menu_select('File -> Open')

bot.wait(1000)

main_window.CustomerLookup.Edit2.type_keys('Charles')
main_window.CustomerLookup.Edit3.type_keys('Lima')
main_window.CustomerLookup.OK.click()
main_window.Fechar.click()