import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/'


def get_html(url):
    response = requests.get(url)
    return response.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('table', id='currency_base_table').find('tbody').find_all('tr')
    for tr in trs:
        tds = tr.find_all('td')
        name = tds[0].text
        price = tds[1].text
        data = {'name': name,
                'price': price}
        write_csv(data)


def write_csv(data):
    with open('file.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['price']))


def main():
    get_data(get_html(url))


if __name__ == '__main__':
    main()
