

N = int(input())
H = list(map(int, input().split()))

cnt = 1
for i in range(1, N):
    if H[i-1] < H[i]:
        continue
    else:
        cnt += 1
print(cnt)