
# 
def isDancePossible(n, perm):
    if n == 1:
        return True
    perm = [i-1 for i in perm]
    for i in range(1, n):
        if abs(perm[i]-perm[i-1]) != 1 and abs(perm[i]-perm[i-1]) != n-1:
            return False
    return True

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        perm = list(map(int, input().split()))
        print("YES" if isDancePossible(n, perm) else "NO")
