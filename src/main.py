from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from .modules.configBrowser import startBrowser
from .modules.coments import list_to_dict_with_index, remove_comments_without_text, remove_line_break_in_lists
from dotenv import load_dotenv
from time import sleep
import json
import sys
import os



# 🔰 variaveis 🔰

load_dotenv() # carrega variaveis de ambiente
URL = os.getenv('URL_DO_PRODUTO', 'https://www.mercadolivre.com.br/')


#______________________________________________________________________________________________________________________
# ❗ iniciando serviços ❗
#______________________________________________________________________________________________________________________

print('🤖 Iniciando Robo 🤖')
BROWSER = startBrowser() # inicia o browser



# abre o site
try:
    BROWSER.get(URL) 
    print(f'🟢 Site aberto com sucesso')
except:
    print('🔴 Erro ao abrir o site, verifique sua conexão com a internet e o link enviado no arquivo .env')
    sys.exit()



NAME_PRODUCT = BROWSER.find_element(By.CLASS_NAME, "ui-pdp-title").text # pega o nome do produto
WAIT = WebDriverWait(BROWSER, 10) # variavel para espera de 10 segundos



sleep(2) # apenas por prevenção



try:
    botao1 = WAIT.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Mostrar todas as opiniões']"))) # botão que abre o modal de comentários
    BROWSER.execute_script("arguments[0].scrollIntoView(block='center', behavior='smooth');", botao1) # vai ate ele
    ActionChains(BROWSER).move_to_element(botao1).click().perform() # clica
    print(f'🟢 Modal de comentários aberto com sucesso')
except:
    print('🔴 Erro ao abrir o modal de comentários, verifique se o produto contem comentarios, ou contate o desenvolvedor')
    sys.exit()



sleep(2) # apenas por prevenção


print()
print(f'Iniciando extração de comentários...')



#_______________________________________________________________________________________________________________________
# 🔰 Selecionando o iframe de comentarios 🔰
#_______________________________________________________________________________________________________________________



try:
    iframe = WAIT.until(EC.presence_of_element_located((By.ID, "ui-pdp-iframe-reviews"))) 
    BROWSER.switch_to.frame(iframe) 
except:
    print('🔴 Erro ao procurar o iframe de comentários, contate o desenvolvedor')


# 🔴 pegando comentarios 🔴
try:
    while True:
        # pega os comentários iniciais
        coments_list = BROWSER.find_elements(By.CLASS_NAME, "ui-review-capability-comments__comment__content")
        previous_quantity_coments = len(coments_list)


        # Rola até o final do modal
        BROWSER.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        sleep(0.8) # apenas por prevenção

        # pega os comentários de novo e compara com os iniciais, se iguais, para o loop
        coments_list = BROWSER.find_elements(By.CLASS_NAME, "ui-review-capability-comments__comment__content")
        last_quantity_coments = len(coments_list)
        if previous_quantity_coments == last_quantity_coments:
            break
    print(f'🟢 Comentarios extraídos com sucesso')
except:
    print('🔴 Erro ao extrair os comentários, verifique se o produto contem comentarios, ou contate o desenvolvedor')
    sys.exit()



# ______________________________________________________________________________________________________________________
# ❗ transformando comentarios em json para consumo ❗
# ______________________________________________________________________________________________________________________



print()
print(f'Transformando comentários em json...')

# tratando comentarios
coments_list = remove_line_break_in_lists(coments_list)
coments_list = remove_comments_without_text(coments_list)

# transforma os comentários em um dicionário
coments_list_dict = list_to_dict_with_index(coments_list) 


# salva os comentários em um arquivo json
with open(f'{NAME_PRODUCT}.json', 'w', encoding='utf-8') as file:
    json.dump(coments_list_dict, file, indent=4, ensure_ascii=False)

print(f'🟢 Comentarios salvos no arquivo {NAME_PRODUCT}.json')


print()
print('🤖 Robo finalizado! 🤖')


# fecha o browser
BROWSER.quit()



