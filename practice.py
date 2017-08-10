import requests
import os


def get_current_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return current_dir


def get_txt_list():
    txt_list = []
    current_dir = get_current_dir()
    file_list = os.listdir(current_dir)
    for file in file_list:
        if file.endswith('.txt'):
            txt_list.append(file)
    return txt_list


def translate_it(txt_dict):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    l = str(*txt_dict.keys()) + '-ru'
    print(l)

    params = {
        'key': key,
        'lang': l,
        'text': txt_dict.values(),
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def work_with_file():
    txt_list = get_txt_list()
    for file in txt_list:
        lang = file[0:2].lower()
        with open(file, encoding='utf-8-sig') as file:
            txt_dict = dict(zip([lang], file))
            a = translate_it(txt_dict)
            print(a)


work_with_file()
