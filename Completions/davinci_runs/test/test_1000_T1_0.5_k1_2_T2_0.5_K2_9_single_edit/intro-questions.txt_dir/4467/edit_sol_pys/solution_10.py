import sys
input = sys.stdin.readline



N = int(input())

red = []
blue = []

for i in range(N):
    x, y = map(int, input().split())
    red.append((x, y))

for i in range(N):
    x, y = map(int, input().split())
    blue.append((x, y))

# red.sort(key=lambda x: x[0])
red.sort(key=lambda x: x[1], reverse=True)
blue.sort(key=lambda x: x[0], reverse=True)
blue.sort(key=lambda x: x[1], reverse=True)

count = 0
for i in range(N):
    for j in range(N):
        if red[i][0] < blue[j][0] and red[i][1] < blue[j][1]:
            count += 1
            blue.remove(b)
            break

print(count)
