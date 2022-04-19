

N = int(input())  # 3
H = list(map(int, input().split()))  # 4 1 3

ans = 0  # 0
curr = 0  # 0

for i in range(N-1):
    if H[i+1] <= H[i]:  # 1 <= 4, 3 <= 1
        curr += 1  # 1
    else:
        ans = max(ans, curr)
        curr = 0
print(max(ans, curr))
