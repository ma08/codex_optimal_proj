

# N = int(input())
# A = list(map(int, input().split()))

# N = 3
# A = [5, 2, 4]

N = 10 ** 4
A = [10 ** 9] * N

def check_ans(A, n):
    while len(A) > 0:
        if A[0] % 2 == 0:
            A = [a // 2 for a in A]
            n += 1
        else:
            break
    return n

ans = 0

for i in range(N):
    a = A[i]
    if a % 2 == 0:
        A[i] = a // 2
        ans += 1
    elif a % 3 == 0:
        A[i] = a // 3
        ans += 1

ans = check_ans(A, ans)

print(ans)