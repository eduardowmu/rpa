# #{image:"views"}

"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""
import datetime

# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")
    
    # configurando nossos alertas/NO CASO DE INFORMAÇÃO
    maestro.alert(
        task_id=execution.task_id,
        title="BotYoutube - Inicio",
        message="Estamos iniciando o processo",
        alert_type=AlertType.INFO
    )

    bot = DesktopBot()
    bot.browse("https://www.youtube.com/watch?v=1bJ4_FDIKy0&list=RDCMUCEmDI96PRniiegjkSmrpZaQ&index=27")

    # Implement here your logic...
    while not bot.find( "unlike", matching=0.97, waiting_time=10000):
        not_found("unlike")
    bot.click()
    like = 1
    
    while not bot.find( "like", matching=0.97, waiting_time=10000):
        not_found("like")
    bot.click()
    like = like + 1

    maestro.new_log_entry(activity_label="LikeLogs", 
                          values={"data_hora": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                                  "canal": "Youtube", "likes_unlikes": like})

    #Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()


