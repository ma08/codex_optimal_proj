

#-----Solution-----

#get number of restaurants
numRestaurants = int(input())

#declare variables
restaurantName = ""

#loop through restaurants
for i in range(0,numRestaurants):
    #get number of menu items
    numMenuItems = int(input())

    #get restaurant name and menu items
    restaurantName = input()
    for j in range(0,numMenuItems):
        menuItem = menuItem.lower()
        menuItem = input()
        #check if pea soup and pancake are in the menu
        if "pea soup" in menuItem and "pancake" in menuItem:
            break
    #break out of loop if pea soup and pancake are in the menu
    if "pea soup" in menuItem and "pancake" in menuItem:
        break

#print restaurant name if pea soup and pancake are in the menu
if "pea soup" in menuItem and "pancake" in menuItem:
    print(restaurantName)
#print message if pea soup and pancake are not in the menu
else:
    print("Anywhere is fine I guess")
