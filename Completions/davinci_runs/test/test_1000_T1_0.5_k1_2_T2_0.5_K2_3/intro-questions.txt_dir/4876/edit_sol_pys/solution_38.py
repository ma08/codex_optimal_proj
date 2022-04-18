

pea_soup = False
pancakes = False
n = int(input())
for i in range(n):
    k = int(input())
    restaurant = input()
    for j in range(k):
        menu = input()
        if menu == "pea soup" or menu == "pancakes":
            if menu == "pea soup":
                pea_soup = True
            else:
                pancakes = True
            if pea_soup and pancakes:
                print(restaurant)
                break
    if pea_soup is False or pancakes is False:
        print("Anywhere is fine I guess.")
