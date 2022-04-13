
def read_menu():
    menu = []
    n = int(input())
    for i in range(n):
        k = int(input())
        menu.append(input())
        for j in range(k):
            menu.append(input())
    return menu

def find_restaurant(menu, food1, food2):
    for i in range(len(menu)):
        if menu[i] == food1 and menu[i + 1] == food2:
            return menu[i - 1]
    return "Anywhere is fine I guess"

def main():
    menu = read_menu()
    print(find_restaurant(menu, "pea soup", "pancakes"))

if __name__ == "__main__":
    main()
