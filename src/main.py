from .configBrowser import startBrowser
from dotenv import load_dotenv
import os



# 🔰 variaveis 🔰

load_dotenv() # carrega variaveis de ambiente
URL = os.getenv('URL_DO_PRODUTO', 'https://www.mercadolivre.com.br/')




#______________________________________________________________________________________________________________________
# ❗ iniciando serviços ❗
#______________________________________________________________________________________________________________________

BROWSER = startBrowser()


BROWSER.get(URL)

input("Pressione enter para sair")