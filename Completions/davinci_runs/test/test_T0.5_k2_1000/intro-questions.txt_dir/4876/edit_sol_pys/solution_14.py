

def read_menus():
    menu = []
    n = int(input())
    for i in range(n):
        k = int(input())
        menu.append(input())
        for j in range(k):
            menu.append(input())
    return menu

def find_restaurants(menus):
    for i in range(len(menus)):
        if menus[i] == "pea soup" and menus[i + 1] == "pancakes":
            return menus[i - 1]
    return "Anywhere is fine I guess"

def main():
    menus = read_menus()
    print(find_restaurants(menus))

if __name__ == "__main__":
    main()
