
N = int(input())
A = [int(input()) for i in range(N)]

cnt = 0
while all(a % 2 == 0 for a in A):
    A = [a // 2 for a in A]
    cnt += 1

print(cnt)
