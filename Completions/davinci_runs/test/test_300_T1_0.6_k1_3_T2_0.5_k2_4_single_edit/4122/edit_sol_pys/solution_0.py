

H, n = [int(x) for x in input().split()] #input
d = [int(x) for x in input().split()] #input

for i in range(n):
    H += d[i] #attack
    if H <= 0: #check if he is dead
        print(i + 1)
        break
else:
    print(-1)
