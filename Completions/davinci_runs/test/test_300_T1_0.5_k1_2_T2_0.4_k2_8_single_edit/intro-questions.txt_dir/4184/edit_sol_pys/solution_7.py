
N = int(input())  # N個の数字が入力される
A = list(map(int, input().split()))  # 1つ目の数字が入力される
B = list(map(int, input().split()))  # 2つ目の数字が入力される
C = list(map(int, input().split()))  # 3つ目の数字が入力される
ans = 0
for i in range(N):
    ans += B[A[i] - 1]
    if i > 0 and A[i] == A[i - 1] + 1:
        ans += C[A[i - 1] - 1]
print(ans)
