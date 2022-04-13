import re

def get_menu():
    menu = []
    k = int(input()) # number of restaurants
    for i in range(k): # for each restaurant
        menu.append(input())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if re.search(r'pea soup', menu[i]) and re.search(r'pancakes', menu[i]): # if pea soup and pancakes are on the same menu
            return menu[i]
    return 'Anywhere is fine I guess'

if __name__ == '__main__':
    n = int(input()) # number of test cases
    for i in range(n):
        menu = get_menu()
        print(find_restaurant(menu))
