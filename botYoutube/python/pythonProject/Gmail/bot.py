#plugins do gmail
from botcity.plugins.gmail import BotGmailPlugin

#variável que receberá nossa credencial
credentials = r"C:\Users\eduardowmu\Desktop\Meusdoc\UDEMY\"

#recebe a instancia do nosso gmail plugin
gmail = BotGmailPlugin(credentials, 'ewmurakoshi@gmail.com')

#iremos ler as msgs existentes. O parametro do metodo são critérios 
#necessários para obtermos o que desejamos
mensagens = gmail.search_messages(criteria='subject:teste RPA')

#caso aconteça de receber emails todos com mesmo assunto:
for msg in mensagens:
    #assunto
    print(msg.subject)
    #remetente
    print(msg.from_)
    #mensagem de texto do email
    print(msg.text)
