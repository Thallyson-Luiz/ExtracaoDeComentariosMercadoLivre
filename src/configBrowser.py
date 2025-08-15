import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options

def startBrowser():
    '''
    Função para iniciar o browser

    variaveis que podem ser mudadas:
    - user_agent_linux: pode ser mudado para um user agent diferente, de sua escolha

    retorna o browser
    '''

    user_agent_linux = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0"

    OPTIONS = Options()
    OPTIONS.add_argument(f"--user-agent={user_agent_linux}")
    OPTIONS.add_argument("--disable-blink-features=AutomationControlled")

    BROWSER = uc.Chrome(options=OPTIONS, headless=False)

    return BROWSER