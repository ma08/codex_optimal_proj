

# SOLUTION

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def solve(n, k, a):
    if len(set(a)) == 1:
        return 0
    
    m = min(a)
    for i in a[1:]:
        m = gcd(m, i)

    moves = 0
    for i in a:
        moves += i // m

    if moves >= k:
        return moves
    return -1


n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
