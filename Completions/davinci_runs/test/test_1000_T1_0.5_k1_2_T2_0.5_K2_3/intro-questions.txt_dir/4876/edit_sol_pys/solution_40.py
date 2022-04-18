

import sys

def read_menus():
    menu = []
    n = int(sys.stdin.readline())
    for i in range(n):
        k = int(sys.stdin.readline())
        menu.append(sys.stdin.readline())
        for j in range(k):
            menu.append(sys.stdin.readline())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if menu[i] == "pea soup" and menu[i + 1] == "pancakes":
            return menu[i - 1]
    return "Anywhere is fine I guess"

def main():
    menu = read_menus()
    print(find_restaurant(menu))

if __name__ == "__main__":
    main()
