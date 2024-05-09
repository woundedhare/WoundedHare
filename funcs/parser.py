import requests
import json


def parser(url: str) -> str:
    """
    Функция-парсер, получает адрес и выводит из соотвествующих мест в json-словаре шутку
    Args: url(str) - адрес сайта с шутками
    """
    req = requests.get(url)
    jsn_dict = json.loads(req.text)
    return jsn_dict['setup']+'\n\n'+jsn_dict['punchline']