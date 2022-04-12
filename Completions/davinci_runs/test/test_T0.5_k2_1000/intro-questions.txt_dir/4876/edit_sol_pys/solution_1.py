

def pea_soup():
    restaurant_name = []
    menu_items = []
    num_restaurants = int(input())

    for i in range(num_restaurants):
        num_menu_items = int(input())
        restaurant_name.append(input())
        menu_items.append([])
        for j in range(num_menu_items):
            menu_items[i].append(input())

        if "pea soup" in menu_items[i] and "pancakes" in menu_items[i]:
            print(restaurant_name[i])
            return

    print("Anywhere is fine I guess")

pea_soup()
