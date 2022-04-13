
# SOLUTION

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    if S > a*n + b:
        print('NO')
    else:
        if S % n <= b and S % n != 0:
            print('YES')
        else:
            print('NO')
