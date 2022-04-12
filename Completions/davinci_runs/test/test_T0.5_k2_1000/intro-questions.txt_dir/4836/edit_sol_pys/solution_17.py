

N, W = map(int, input().split())
#N, W = 5, 5
w = list(map(int, input().split())) #weight
#w = [3, 1, 2, 1, 1] #weight

count = 0

while W > 0:
    if w[count] <= W:
        W -= w[count]
        count += 1
    else:
        break

print(count)
