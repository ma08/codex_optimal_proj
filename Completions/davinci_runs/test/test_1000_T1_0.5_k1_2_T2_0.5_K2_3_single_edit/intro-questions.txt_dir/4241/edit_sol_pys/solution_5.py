

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    count = 0
    while A[i]%2 == 0:
        count += 1
        A[i] //= 2
    ans += count

print(ans)

# 文字列の部分文字列を求める問題では，横方向のループを縦方向のループとすることで，効率的に解くことができる．
