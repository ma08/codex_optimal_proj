

n = int(input()) # number of houses
x = list(map(int, input().split())) # location of houses

min_houses = max(x) - min(x) + 1 # minimum number of cameras
max_houses = n # maximum number of cameras

for i in range(n): # loop through the locations of houses
    if x[i] == 1:
        max_houses -= 1 # if house is at the beginning of the street, you can place a camera at the house
    if x[i] == n:
        max_houses -= 1 # if house is at the end of the street, you can place a camera at the house

print(min_houses, max_houses)
