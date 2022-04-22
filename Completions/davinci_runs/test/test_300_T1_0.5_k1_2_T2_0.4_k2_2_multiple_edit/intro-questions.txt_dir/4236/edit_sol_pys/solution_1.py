
n, m = map(int, input().split())  # n = number of elements, m = number of operations

left = [0] * (m + 1)  # number of elements in the left side
right = [0] * (m + 1)  # number of elements in the right side

for i in range(n):
    l, r = map(int, input().split())
    left[l] += 1
    right[r] += 1

counter = 0
for i in range(1, m + 1):
    if left[i] == right[i]:
        counter += 1
    elif left[i] > right[i]:
        print(counter)
        break
else:
    print(counter)
