
pea_soup = False
pancakes = False
n = int(input())
for i in range(n):
    k = int(input())
    restaurant = input()
    for _ in range(k):
        menu = input()
        if menu == "pea soup" or menu == "pancakes":
            pea_soup = True if menu == "pea soup" else False
            pancakes = True if menu == "pancakes" else False
            if pea_soup and pancakes:
                print(restaurant)
                break
    else:
        print("Anywhere is fine I guess")
