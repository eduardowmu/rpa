from botcity.plugins.googledrive import BotGoogleDrivePlugin

#variável que receberá nossa credencial
#credentials = r"C:\Users\eduardowmu\Desktop\Meusdoc\UDEMY\"

googleDrive = BotGoogleDrivePlugin(credentials)

#identificando o arquivo a fazer upload
#idFolder = googleDrive.search_folder_by_name('BotGoogleDrive')

#Processos para Upload ao Google Drive
#caminho do arquivo
#filePath = 'H:/Dados/MEU_PC/Meusdoc/UDEMY/RPA/repositorio/rpa/botYoutube/python/pythonProject/GoogleDrive/imagens/imagem_01.jpg'

#fazendo o upload
#googleDrive.upload_file(file_path=filePath, parent_folder_id=idFolder, file_name='imagem_01.jpg')

#Processos para Download a partir do Google Drive
idFile = googleDrive.search_file_by_name('imagem_02.jpg')
filePath = 'H:/Dados/MEU_PC/Meusdoc/UDEMY/RPA/repositorio/rpa/botYoutube/python/pythonProject/GoogleDrive/imagens/imagem_02.jpg'
googleDrive.download_file(file_id=idFile, file_path=filePath)