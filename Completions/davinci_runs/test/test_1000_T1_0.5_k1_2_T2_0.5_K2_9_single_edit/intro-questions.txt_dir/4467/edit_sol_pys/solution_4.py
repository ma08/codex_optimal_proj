

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
# red.sort(key=lambda x: x[1])
# blue.sort(key=lambda x: x[0])
blue.sort(key=lambda x: x[1])

count = 0
for r in red:
    for b in blue:
        if r[0] < b[0] and r[1] < b[1]:
            count += 1
            blue.remove(b)
            break

print(count)
