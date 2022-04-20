

N, K = map(int, input().split())

# Initialize a list of length N+1, with each element being a set of length 0.
snuke_snacks = [set() for _ in range(N+1)]

for i in range(K):
    d = int(input())
    for snack in map(int, input().split()):
        snuke_snacks[snack].add(i)

print(sum(1 for snuke in snuke_snacks[1:] if len(snuke) == 0))