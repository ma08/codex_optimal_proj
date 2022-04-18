

n = int(input())
restaurants = []

for i in range(n):
    k = int(input())
    menu = []
    for j in range(k):
        menu.append(input())
    restaurants.append(menu)

for restaurant in restaurants:
    if "pea soup" in restaurant[1:] and "pancakes" in restaurant[1:]:
        print (restaurant[0])
        break
else:
    print ("Anywhere is fine I guess")
