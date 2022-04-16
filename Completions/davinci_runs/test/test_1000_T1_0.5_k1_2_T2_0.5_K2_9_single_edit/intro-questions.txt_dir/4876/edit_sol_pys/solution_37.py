

import sys

def read_menu():
    menu = []
    n = int(input())
    for i in range(n):
        menu.append(input().split())
    return menu

def find_restaurant(menu):
    for i in range(len(menu) - 1):
        if menu[i][0] == "pea soup" and menu[i + 1][0] == "pancakes":
            return menu[i - 1][0]
    return "Anywhere is fine I guess"

def main():
    menu = read_menu()
    print(find_restaurant(menu))

if __name__ == "__main__":
    main()
