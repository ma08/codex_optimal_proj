
# Solution

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    print('YES' if len(set(a)) in [1, 2] else 'NO')
