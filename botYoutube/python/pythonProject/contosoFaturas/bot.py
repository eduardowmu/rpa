from botcity.core import DesktopBot

def not_found(label):
    print(f"Element not found: {label}")

def cadastroFaturas():
    bot = DesktopBot()
    path_app = "C:/Program Files (x86)/Contoso, Inc/Contoso Invoicing/LegacyInvoicingApp.exe";

    bot.execute(path_app)
    bot.wait(5000)
    bot.maximize_window()

    bot.wait(1000)
    
    if not bot.find( "invoices", matching=0.97, waiting_time=10000):
        not_found("invoices")
    bot.click()
    
    if not bot.find( "new", matching=0.97, waiting_time=10000):
        not_found("new")
    bot.click()
    
    if not bot.find( "date", matching=0.97, waiting_time=10000):
        not_found("date")
    bot.click_relative(73, 6)

    #linhas digitadas manualmente
    bot.type_keys(['home'])
    bot.type_keys(['shift', 'end'])
    bot.paste('01/16/2024')

    bot.tab()
    bot.paste('123456')

    bot.tab()
    bot.paste('edu@gmail.com')

    bot.tab()
    bot.paste('1000')

    if not bot.find( "status-inicio", matching=0.97, waiting_time=10000):
        not_found("status-inicio")
    bot.click_relative(64, 9)

    coluna = 'Ivoiced'

    if coluna == "Univoiced":
        if not bot.find( "Uninvoiced", matching=0.97, waiting_time=10000):
            not_found("Uninvoiced")
        bot.click_relative(79, 28)

    elif coluna == "Ivoiced":
        if not bot.find( "invoiced", matching=0.97, waiting_time=10000):
            not_found("invoiced")
        bot.click_relative(68, 49)

    else:
        if not bot.find( "paid", matching=0.97, waiting_time=10000):
            not_found("paid")
        bot.click_relative(68, 74)
        
    if not bot.find( "salvar", matching=0.97, waiting_time=10000):
        not_found("salvar")
    bot.click()

cadastroFaturas()




