
n, m = map(int, input().split())

left = [0] * (m + 2)
right = [0] * (m + 2)

for i in range(n):
    l, r = map(int, input().split())
    left[l + 1] += 1
    right[r + 1] += 1

counter = 0
for i in range(1, m + 2):
    counter += left[i]
    if counter != right[i]:
        print(i - 1)
        exit()
print(m)
