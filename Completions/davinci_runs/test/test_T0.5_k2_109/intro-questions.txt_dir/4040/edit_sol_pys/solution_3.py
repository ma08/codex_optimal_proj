
def solve(n, m, d, a):
    # Write your code here
    return [0] * n

n, m, d = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

ans = solve(n, m, d, a)

if ans == [0] * n:
    print('NO')
else:
    print('YES')
    print(' '.join([str(x) for x in ans]))
