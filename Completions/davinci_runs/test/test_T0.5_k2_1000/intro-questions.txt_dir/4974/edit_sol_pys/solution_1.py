
r, n = map(int, input().split()) # r = number of rooms, n = number of rooms already occupied

for i in range(1, r+1): # looping through all rooms
    if i not in map(int, input().split()): # if the room is not occupied
        print(i) # print the room number
        break
else:
    print("too late")
