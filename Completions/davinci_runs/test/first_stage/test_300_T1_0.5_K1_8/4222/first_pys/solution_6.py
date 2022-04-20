

# Read input
N, K = map(int, input().split())
snack_counts = [0]*N
for i in range(K):
    d = int(input())
    for j in map(int, input().split()):
        snack_counts[j-1] += 1

# Count victims
victims = 0
for n in snack_counts:
    if n == 0:
        victims += 1
print(victims)