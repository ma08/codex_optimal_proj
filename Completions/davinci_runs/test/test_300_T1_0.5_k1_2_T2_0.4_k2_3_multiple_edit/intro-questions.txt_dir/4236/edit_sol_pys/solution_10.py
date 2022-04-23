

n, m = map(int, input().split())

l = [0] * (m + 1)
r = [0] * (m + 1)

for i in range(n):
    left, right = map(int, input().split())
    l[left] += 1
    r[right] += 1

counter = 0
for i in range(1, m + 1):
    if left[i] == right[i]:
        counter += 1
    elif left[i] > right[i]:
        print(counter)
        break
else:
    print(counter)
