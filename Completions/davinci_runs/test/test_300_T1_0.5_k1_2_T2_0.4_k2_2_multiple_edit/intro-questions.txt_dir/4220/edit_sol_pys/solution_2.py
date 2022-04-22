#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os
import re
import json
import datetime
import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.google.com/search?q='
    query = raw_input()
    url = url + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('div', attrs={'class': 'g'})
    for result in search_results:
        title = result.find('h3', attrs={'class': 'r'})
        if title:
            title = title.get_text()
        else:
            title = ''
        url = result.find('a', attrs={'class': 'l'})
        if url:
            url = url['href']
        else:
            url = ''
        description = result.find('span', attrs={'class': 'st'})
        if description:
            description = description.get_text()
        else:
            description = ''
        print(title)
        print(url)
        print(description)
        print('')

if __name__ == '__main__':
    main()
