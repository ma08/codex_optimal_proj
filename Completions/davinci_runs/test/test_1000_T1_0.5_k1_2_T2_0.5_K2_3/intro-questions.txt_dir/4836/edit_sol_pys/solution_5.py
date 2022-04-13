

N, C = map(int, input().split()) # N is number of items, C is the capacity of the bag
#N, C = 5, 5
w = list(map(int, input().split())) # w is the weight of the items
#w = [3, 1, 2, 1, 1]

count = 0

while C > 0:
    if w[count] <= C:
        C -= w[count]
        count += 1
    else:
        break

print(count)
