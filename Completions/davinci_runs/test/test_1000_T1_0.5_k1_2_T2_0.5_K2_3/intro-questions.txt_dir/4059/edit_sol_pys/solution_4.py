
N = int(input())

count = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        c = N - a - b
        if c > 0 and a != b and b != c and a != c:
            count += 1

print(count)
