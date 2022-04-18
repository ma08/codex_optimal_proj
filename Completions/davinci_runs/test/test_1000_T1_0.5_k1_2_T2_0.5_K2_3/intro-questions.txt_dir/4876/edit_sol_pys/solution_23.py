

n = int(input())
for i in range(n):
    k = int(input())
    restaurants = []
    for j in range(k):
        menu = input()
        if menu == "pea soup":
            restaurants.append(menu)
        elif menu == "pancakes":
            restaurants.append(menu)
    if len(restaurants) == 0:
        print(restaurants[0])
    else:
        print("Anywhere is fine I guess")
