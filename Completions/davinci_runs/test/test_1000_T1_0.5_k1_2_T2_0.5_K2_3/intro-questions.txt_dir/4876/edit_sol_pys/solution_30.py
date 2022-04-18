

n = int(input())
restaurant = []

for i in range(n):
    k = int(input())
    menu = []
    for j in range(k+1):
        menu.append(input())
    restaurant.append(menu)

for restaurant in restaurant:
    if "pea soup" in restaurant and "pancakes" in restaurant and "pancakes" in restaurant: 
        print (restaurant[0]) 
        break
else:
    print ("Anywhere is fine I guess")
