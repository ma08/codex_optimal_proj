
#!/bin/python3
# SOLUTION

q = int(input())
for _ in range(q):
    a, b, n, S = map(int, input().split())
    if S <= a*n + b:
        if S % n <= b:
            print('YES')
            continue
    print('NO')
