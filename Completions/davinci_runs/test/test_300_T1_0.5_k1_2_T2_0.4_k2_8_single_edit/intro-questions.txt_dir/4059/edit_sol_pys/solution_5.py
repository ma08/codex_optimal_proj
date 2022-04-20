
N = int(input())

count = 0
for a in range(1, N+1):
    for b in range(1, N+1):
        if N - a*b > 0:
            count += 1

print(count)
