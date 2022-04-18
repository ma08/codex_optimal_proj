# n = int(input())
# keywords = set()
# for i in range(n):
#     keyword = input().lower().replace("-", " ")
#     keywords.add(keyword)
# print(len(keywords))

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     h1 = soup.find('div', id='home-welcome').find('h1').text
#     return h1
#
#
# def main():
#     url = 'https://www.python.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='pagination-pages').find_all('a', class_='pagination-page')[-1].get('href')
    total_pages = pages.split('=')[1].split('&')[0]
    return int(total_pages)


def main():
    url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/nastolnye_igrovye_kompyutery?p=1&q=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80'
    base_url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/nastolnye_igrovye_kompyutery?'
    page_part = 'p='
    query_part = '&q=%D0%B8%D0%B3%D1%80%D0%BE%D0%B2%D1%8B%D0%B9+%D0%BA%D0%BE%D0%BC%D0%BF%D1%8C%D1%8E%D1%82%D0%B5%D1%80'
    total_pages = get_total_pages(get_html(url))
    for i in range(1, 3):
        url_gen = base_url + page_part + str(i) + query_part
        print(url_gen)


if __name__ == '__main__':
    main()
