

def solve(n, m, d, c, s):
    # Write your code here
    return [0] * n 

n, m, d, s = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]

ans = solve(n, m, d, c, s)

if ans == [0] * n:
    print('NO')
else:
    print('YES')
    print(' '.join([str(x) for x in ans]))
