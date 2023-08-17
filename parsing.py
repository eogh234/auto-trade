import requests
from bs4 import BeautifulSoup as bs


def get_best_list():
    symbol_name_list = []
    symbol_code_list = []

    url = requests.get("https://finance.naver.com/")

    soup = bs(url.text, "html.parser")

    elements = soup.select('#_topItems2 tr.up>th')
    best_list = []

    for elem in elements:
        best_list.append(
            [elem.find('a').text, elem.select_one('a')['href'].split('=')[1]])

    for name, code in best_list:
        symbol_name_list.append(name)
        symbol_code_list.append(code)

    print(symbol_name_list)

    return symbol_code_list
