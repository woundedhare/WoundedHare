def weather_mode(w_id: int):
    """
    Функция weather_mode: преобразует id погоды из полученного через обращение к сайту json-словаря
     в конкретное описание погоды
     Args: w_id(int) - id-код погоды из json-словаря
     returns: погода в виде кортежа, (словесная формулировка и id стикера)
     """
    if w_id // 100 == 2:
        return 'Гроза', 'CAACAgIAAxkBAAEKPY9k-ZLJ8EuU-OdjKtYbR2NdTgVMowACzAADUomRI-7bk7Ej6bZAMAQ'
    elif w_id // 100 == 3:
        return 'Морось', 'CAACAgIAAxkBAAEKPC5k-G_6snoZaEjTi3XRYUSdz9FRDwACyQADUomRI2QzL5Ov-ocxMAQ'
    elif w_id // 100 == 5:
        return 'Дождь', 'CAACAgIAAxkBAAEKPC5k-G_6snoZaEjTi3XRYUSdz9FRDwACyQADUomRI2QzL5Ov-ocxMAQ'
    elif w_id // 100 == 6:
        return 'Снег', 'CAACAgIAAxkBAAEKPExk-HHiez1YMElZw5lbGOBsNYfuDQACygADUomRIz3-U_49GT0EMAQ'
    elif w_id // 100 == 7:
        return 'Туман', 'CAACAgIAAxkBAAEKO_xk-F9vDZScHHW-hPrdQE1ODU56RQACaQEAAqZESAt_3dxMvA3vCTAE'
    elif w_id == 800:
        return 'Ясно', 'CAACAgIAAxkBAAEKPEZk-HGMveO49Wa1BfVg0C3gr8iRKgAC1wADUomRIxJisMdoFAViMAQ'
    elif w_id == 801:
        return 'Малооблачно', 'CAACAgIAAxkBAAEKPYVk-ZJCWT1sd-QOyGQb2Mb8xf_AsQAC3QADUomRI3cuYMokvdLeMAQ'
    elif w_id == 802:
        return 'Переменная облачность', 'CAACAgIAAxkBAAEKPBpk-GJVIuo-e44n2xlKD_SElM11FwAC2QADUomRI3oKNLvLNvkUMAQ'
    elif w_id == 803:
        return 'Переменная облачность', 'CAACAgIAAxkBAAEKPJhk-IwlMzQrDtqBGC2WM1y65XzwLQACywADUomRIw-_9TwlPXeIMAQ'
    else:
        return 'Облачно', 'CAACAgIAAxkBAAEKPBFk-GHNI1ApprvzpeeJ5euh5KDB0wACxgADUomRIzmUbbF6xf1YMAQ'
