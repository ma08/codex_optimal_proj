# coding: utf-8

import sys

def read_menu():
    menu = []
    n = int(input())
    for i in range(n):
        k = int(input())
        menu.append(input().split())
        for j in range(k):
            menu.append(input().split())
    return menu

def find_restaurant(menu):
    for i in range(len(menu)):
        if "pea soup" in menu[i] and "pancakes" in menu[i + 1]:
            return menu[i - 1][0]
    return "Anywhere is fine I guess"

def main():
    menu = read_menu()
    print(find_restaurant(menu))

if __name__ == "__main__":
    main()
