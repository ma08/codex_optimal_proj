

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

# My answer (2)
N = int(input())
L = list(map(int, input().split()))

count = 0  # 可能な三角形の数
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] != L[j] and L[i] != L[k] and L[j] != L[k]:  # 同じ辺の長さはない
                if L[i] + L[j] > L[k] and L[i] + L[k] > L[j] and L[j] + L[k] > L[i]:  # 三角形の不等式
                    count += 1

print(count)
