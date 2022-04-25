

N = int(input())
H = list(map(int, input().split()))

count = 0
for i in range(N):
    if H[i] > 0:
        count += 1
        for j in range(i+1, N):
            if H[j] > 0:
                H[j] -= 1

print(count)
