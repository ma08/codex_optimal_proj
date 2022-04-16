
def isDancePossible(n, perm):
    pass

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        perm = list(map(int, input().split()))
        print("YES" if isDancePossible(n, perm) else "NO")
