from selenium.webdriver.remote.webelement import WebElement

def list_to_dict_with_index(coments_list: list[str]) -> list[dict]:
    """
    parametros: 
        coments_list: lista de comentários

    retorna:
        coments_list_dict: dicionário com os comentários
    """

    coments_list_dict = [] 

    # transforma os comentários em um dicionário
    for i, coment in enumerate(coments_list):
        coment_dict = {
            'number': i,
            'coment': coment
        }
        coments_list_dict.append(coment_dict)

    return coments_list_dict

def remove_comments_without_text(coments_list: list[str]) -> list:
    """
    parametros: 
        coment_list: lista de comentários

    retorna:
        lista_vazia: lista de comentários sem comentários vazios
    """

    lista_vazia = []
    for coment in coments_list:
        if coment == '':
            continue
        lista_vazia.append(coment)

    return lista_vazia

def remove_line_break_in_lists(coments_list: list[WebElement]) -> list:
    """
    parametros: 
        coment_list: lista de comentários

    retorna:
        coment_list: lista de comentários sem quebras de linha
    """
    return [(coment.get_attribute('innerHTML') or '').replace('\n', '') for coment in coments_list]
