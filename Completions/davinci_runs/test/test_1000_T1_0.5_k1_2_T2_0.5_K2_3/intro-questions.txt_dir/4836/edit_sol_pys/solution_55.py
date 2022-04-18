
n, c = map(int, input().split()) # n = number of cows, c = capacity of the truck
w = list(map(int, input().split())) # w = list of weights of cows

eaten = 0
curr = 0
w.sort()

for x in w:
    if curr + x <= c:
        curr += x
        eaten += 1
print(eaten)
