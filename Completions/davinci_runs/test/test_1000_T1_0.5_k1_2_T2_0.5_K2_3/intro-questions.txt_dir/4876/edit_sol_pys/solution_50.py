

n = int(input())
for i in range(n):
    k = int(input())
    restaurants = []
    for j in range(k):
        menu = raw_input()
        restaurants.append(menu)
    if "pea soup" in restaurants and "pancakes" in restaurants:
        print(restaurants[0])
    else:
        print("Anywhere is fine I guess")
