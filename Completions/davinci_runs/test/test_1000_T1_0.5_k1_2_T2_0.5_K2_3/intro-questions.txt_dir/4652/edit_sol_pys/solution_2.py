
def isDancePossible(n, p):
    if n == 1:
        return True
    p = [i-1 for i in p]
    for i in range(1, n):
        if abs(p[i]-p[i-1]) != 1 and abs(p[i]-p[i-1]) != n-1:
            return False
    return True

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print("YES" if isDancePossible(n, p) else "NO")
