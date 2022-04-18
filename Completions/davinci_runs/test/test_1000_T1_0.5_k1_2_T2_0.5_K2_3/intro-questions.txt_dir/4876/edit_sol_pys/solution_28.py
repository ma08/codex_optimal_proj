

n = int(input()) #number of test cases

for i in range(n): #loop through the test cases
    k = int(input()) #number of restaurants
    name = input() #name of the restaurant
    for j in range(k): #loop through all the restaurants
        item = input() #name of the item
        if item == "pea soup": #if the item is pea soup
            for l in range(k): #loop through the restaurants
                item = input()
                if item == "pancakes": #if the item is pancakes
                    print(name)
                    break

            break
