
N = int(input())  # 2

red = []
blue = []

for i in range(N):
    x, y = map(int, input().split())  # (1,2) (2,1)
    red.append((x, y))

for i in range(N):
    x, y = map(int, input().split())  # (3,3) (4,2)
    blue.append((x, y))

red.sort(key=lambda x: x[0])  # (1,2) (2,1)
red.sort(key=lambda x: x[1])  # (2,1) (1,2)
blue.sort(key=lambda x: x[0])  # (3,3) (4,2)
blue.sort(key=lambda x: x[1])  # (4,2) (3,3)

count = 0
for r in red:
    for b in blue:
        if r[0] < b[0] and r[1] < b[1]:
            count += 1
            blue.remove(b)
            break

print(count)
