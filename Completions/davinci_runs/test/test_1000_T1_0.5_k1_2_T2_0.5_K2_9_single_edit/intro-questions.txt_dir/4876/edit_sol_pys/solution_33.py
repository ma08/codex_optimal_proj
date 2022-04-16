

n = int(input()) #number of test cases

for i in range(n):
    k = int(input()) #number of menu items
    name = input() #name of restaurant
    for j in range(k):
        item = input() #menu item
        if item == "pea soup":
            for l in range(k):
                item = input() #menu item
                if item == "pancakes":
                    print(name) #print name of restaurant
                    break
            break
