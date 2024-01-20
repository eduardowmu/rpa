from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager

def main():
    bot = WebBot()

    #se o comando abaixo for False, o navegador será aberto, caso
    #contrário, ficará em segundo plano e não veremos nada
    bot.headless = False
    bot.browser = Browser.CHROME

    bot.driver_path = ChromeDriverManager().install()

    bot.browse("https://www.botcity.dev")


    # Wait 3 seconds before closing
    bot.wait(3000)

    bot.maximize_window()
    bot.wait(3000)
    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
