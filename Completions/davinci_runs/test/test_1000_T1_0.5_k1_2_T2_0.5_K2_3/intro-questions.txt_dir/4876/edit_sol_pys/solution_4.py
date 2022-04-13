

def pea_soup_pancakes():
    num_restaurants = int(input())

    for i in range(num_restaurants):
        num_menu_items = int(input())  # number of menu items
        restaurant_name = input()  # name of restaurant
        menu_items = []
        for j in range(num_menu_items):  # add menu items to list
            menu_items.append(input())

        if "pea soup" in menu_items and "pancakes" in menu_items:  # check for pea soup and pancakes
            print(restaurant_name)
            return

    print("Anywhere is fine I guess")

pea_soup_pancakes()
