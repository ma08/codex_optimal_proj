

n, m = map(int, input().split())

left = [0] * (m)
right = [0] * (m)

for i in range(n):
    l, r = map(int, input().split())
    left[l] += 1
    right[r] += 1

counter = 0
for i in range(m):
    if left[i] == right[i]:
        counter += 1
    elif left[i] > right[i]:
        print(counter)
        break
else:
    print(counter)
