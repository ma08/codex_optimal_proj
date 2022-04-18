

n = int(input())
restaurants = []

for i in range(n):
    k = int(input())
    menu = []
    for j in range(k):
        menu.append(input())
    restaurants.append(menu)

for restaurant in restaurants:
    if "pea soup" in restaurant and "pancakes" in restaurant and restaurant[-1] != "pea soup":
        print (restaurant[0])
        break
else:
    print ("Anywhere is fine I guess")
