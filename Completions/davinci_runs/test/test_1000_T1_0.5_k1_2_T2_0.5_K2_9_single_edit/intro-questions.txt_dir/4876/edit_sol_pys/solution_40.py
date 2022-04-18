
import re

def get_menu():
    menu = []
    for i in range(int(input())):
        menu.append(input())
    return menu

def find_restaurant(menu):
    for i in menu:
        if re.search(r'\bpea soup\b', i) and re.search(r'\bpancakes\b', i):
            return menu[menu.index(i)]
    return 'Anywhere is fine I guess'

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        menu = get_menu()
        print(find_restaurant(menu))
