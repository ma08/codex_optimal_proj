

with open('input.txt', 'r') as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

    a.sort()

    count = 1
    for i in range(1, n):
        if a[i] != a[i-1]:
            count += 1

print(count)
