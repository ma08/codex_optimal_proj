from itertools import permutations

N, M = map(int, input().split())
for i in permutations(range(10), N):
    if all(i[s - 1] == c for s, c in (map(int, input().split()) for _ in range(M))):
        print(i)
        exit()
print(-1)
