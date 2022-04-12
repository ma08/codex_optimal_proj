

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
    for i in range(0, len(menu), 2):
        if menu[i] == "pea soup" and "pancakes" in menu[i + 1]:
            return menu[i]
    return "Anywhere is fine I guess"

def main():
    menu = read_menu()
    print(find_restaurant(menu))

if __name__ == "__main__":
    main()
