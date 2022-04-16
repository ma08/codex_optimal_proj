
n = int(input())
times = []
for i in range(n):
    times.append(list(map(int, input().split()))) # input data

for i in range(n):
    if times[i][0] <= times[i][1]:
        print("edward is right")
        quit() # if edward is right, print edward is right and quit

print("gunilla has a point")
