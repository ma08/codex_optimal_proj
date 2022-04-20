

n, k = map(int, input().split())

snacks = [0] * n

for i in range(k):
    d = int(input())
    for a in map(int, input().split()):
        snacks[a-1] += 1

print(snacks.count(0))