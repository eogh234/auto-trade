import requests
from bs4 import BeautifulSoup as bs


def get_best_list():
    url = requests.get("https://finance.naver.com/")

    soup = bs(url.text, "html.parser")

    elements = soup.select('#_topItems2 tr.up>th')
    best_list = []

    for elem in elements:
        best_list.append(elem.select_one('a')['href'].split('=')[1])

    print(best_list)

    return best_list
