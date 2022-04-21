

n = int(input())
l = input()
r = input()

left = []
right = []

for i in range(n):
    left.append((i, l[i]))

for i in range(n):
    right.append((i, r[i]))

left.sort(key=lambda x: (x[1], x[0]))
right.sort(key=lambda x: (x[1], x[0]))

ans = 0

for i in range(n):
    for j in range(n):
        if left[i][1] == right[j][1]:
            ans += 1
            left[i] = (-1, -1)
            right[j] = (-1, -1)
            break

left.sort(key=lambda x: x[1])
right.sort(key=lambda x: x[1])

print(ans)

for i in range(ans):
    print(left[i][0] + 1, right[i][0] + 1)
