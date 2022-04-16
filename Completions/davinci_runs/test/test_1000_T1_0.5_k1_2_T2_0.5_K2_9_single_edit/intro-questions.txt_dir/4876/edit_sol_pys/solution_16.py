


import sys

def read_menu():
    menu = []
    n = int(input())
    for i in range(n):
        k = int(input())
        menu.append(input())
        for j in range(k):
            menu.append(input())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if menu[i] == "pea soup" and menu[i + 1] == "pancakes":
            return menu[i - 1]
    return "Anywhere is fine I guess"

def main():
    menu = read_menu()
    print(find_restaurant(menu))

if __name__ == "__main__":
    main()
