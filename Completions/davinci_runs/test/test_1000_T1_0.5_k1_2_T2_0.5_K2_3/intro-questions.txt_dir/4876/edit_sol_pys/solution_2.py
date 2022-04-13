

def pea_soup_pancakes(file):
    num_restaurants = int(file.readline())

    for i in range(num_restaurants):
        num_menu_items = int(file.readline())
        restaurant_name = file.readline()
        menu_items = []
        for j in range(num_menu_items):
            menu_items.append(file.readline())

        if "pea soup" in menu_items and "pancakes" in menu_items:
            print(restaurant_name)
            return

    print("Anywhere is fine I guess")

file = open("file.txt", "r")
pea_soup_pancakes(file)
