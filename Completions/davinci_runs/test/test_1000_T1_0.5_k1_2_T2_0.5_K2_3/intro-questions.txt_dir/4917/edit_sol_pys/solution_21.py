


n = int(input())
times = []
for i in range(n):
    times.append(list(map(int, input().split())))

for i in range(n):
    if times[i][0] <= times[i][1]:
        print("Edward is right")
        quit()

print("Gunilla has a point")
