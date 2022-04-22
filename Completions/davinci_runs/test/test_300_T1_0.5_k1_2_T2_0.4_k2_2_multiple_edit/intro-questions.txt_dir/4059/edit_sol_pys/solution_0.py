N, M = map(int, input().split())
count = 0

if N == 1 and M == 1:
    print(1)
    exit()

if N == 1 or M == 1:
    print(max(N, M) - 2)
    exit()

print(count)
