

N, K = list(map(int, input().split()))
snacks = []
for _ in range(K):
    snacks.append(list(map(int, input().split()))[1:])

# print(N, K)
# print(snacks)

snacks = [snack - 1 for snacks in snacks for snack in snacks]
# print(snacks)

print(N - len(set(snacks)))