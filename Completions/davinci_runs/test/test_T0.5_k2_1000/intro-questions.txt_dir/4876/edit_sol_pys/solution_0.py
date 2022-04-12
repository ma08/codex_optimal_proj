
import re

def get_menu():
    menu = []
    for i in range(int(input())):
        menu.append(raw_input())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if re.search(r'\bpea soup\b', menu[i]) and re.search(r'\bpancakes\b', menu[i]):
            return menu[i]
    return 'Anywhere is fine I guess'

if __name__ == '__main__':
    for i in range(int(input())):
        menu = get_menu()
        print(find_restaurant(menu))
