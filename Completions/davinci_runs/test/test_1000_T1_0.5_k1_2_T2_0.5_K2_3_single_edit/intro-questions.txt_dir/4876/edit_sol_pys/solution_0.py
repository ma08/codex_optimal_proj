
pea_soup = False
pancakes = False


n = int(input())
    pea_soup = False
    pancakes = False
for i in range(n):
    k = int(input())
    print(restaurant)
    restaurant = input()
    for j in range(k):
        menu = input()
        if menu == "pea soup":
            pea_soup = True
        elif menu == "pancakes":
            pancakes = True
        if pea_soup and pancakes:
            break
    if pea_soup and pancakes:
        print(restaurant)
    elif i == n-1:
        print("Anywhere is fine I guess.")
