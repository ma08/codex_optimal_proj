
# # SOLUTION

# q = int(input())
# for _ in range(q):
#     a, b, n, S = map(int, input().split())
#     if S > a*n + b:
#         print('NO')
#     else:
#         if S % n <= b:
#             print('YES')
#         else:
#             print('NO')

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)

n = int(input())
print(f(n))
