

def isDancePossible(n, permutation):
    if n == 1:
        return True
    permutation = [i - 1 for i in permutation]
    for i in range(1, n):
        if abs(permutation[i] - permutation[i - 1]) != 1 and abs(permutation[i] - permutation[i - 1]) != n - 1:
            return False
    return True

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        permutation = list(map(int, input().split()))
        print("YES" if isDancePossible(n, permutation) else "NO")
