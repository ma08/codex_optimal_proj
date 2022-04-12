

def is_dance_possible(n, perm, k):
    if k == 1:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        n = int(input())
        perm = list(map(int, input().split()))
        k = int(input())
        print(is_dance_possible(n, perm, k))
