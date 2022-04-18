

N = int(input())
A = list(map(int, input().split()))

# 解説AC
count = 0
for i in range(N):
    while A[i] % 2 == 0 or A[i] % 3 == 2:
        A[i] -= 1
        count += 1
print(count)
