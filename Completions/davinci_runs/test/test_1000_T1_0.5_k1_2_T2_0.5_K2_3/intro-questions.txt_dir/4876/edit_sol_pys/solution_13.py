

import re

def get_menu():
    menu = []
    k = int(input())
    for i in range(k):
        menu.append(input())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if re.search(r'\bpea soup\b', menu[i]) and re.search(r'\bpancakes\b', menu[i]) and re.search(r'\b[a-zA-Z]+\b', menu[i]):
            return menu[0]
    return 'Anywhere is fine I guess'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        menu = get_menu()
        print(find_restaurant(menu))
