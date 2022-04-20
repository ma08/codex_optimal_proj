def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(n, k, a):
    if len(set(a)) == 1:
        return 0
    
    m = min(a)
    for i in a:
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
