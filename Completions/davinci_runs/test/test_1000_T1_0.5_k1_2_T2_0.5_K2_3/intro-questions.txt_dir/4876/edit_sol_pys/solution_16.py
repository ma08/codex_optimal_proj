pea_soup = False
pancakes = False

n = int(input())
    pea_soup = False
    pancakes = False
for i in range(n):
    k = int(input())
    restaurant = input()
    for j in range(k):
        menu = input()
        if menu == "pea soup" or menu == "pancakes":  # if the menu is pea soup or pancakes
            if menu == "pea soup":  # if the menu is pea soup
                pea_soup = True  # set pea_soup to True
            else:
                pancakes = True  # if the menu is pancakes set pancakes to True
            if pea_soup and pancakes:  # if pea soup and pancakes are True
                print(restaurant)
                break  # break out of the loop
    else:
        print("Anywhere is fine I guess")  # if pea soup and pancakes aren't True
