
def pea_soup():
    num_restaurants = int(input())

    for i in range(num_restaurants):
        num_menu_items = int(input())
        restaurant_name = input()
        menu_items = []
        for j in range(num_menu_items):
            menu_items.append(input())
        if "pea soup" in menu_items and "pancakes" in menu_items:
            print(restaurant_name)
            return

    print("Anywhere is fine I guess")

pea_soup()
