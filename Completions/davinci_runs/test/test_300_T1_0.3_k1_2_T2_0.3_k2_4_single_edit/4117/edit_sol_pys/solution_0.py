

# My answer (1)
N = int(input())
L = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:
                if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:
                    count += 1

print(count)

# Shortest answer (1)
N = int(input())
L = list(map(int, input().split()))

print(sum(i < j < k and L[i] + L[j] > L[k] for i in range(N) for j in range(i + 1, N) for k in range(j + 1, N)))

print(count)
