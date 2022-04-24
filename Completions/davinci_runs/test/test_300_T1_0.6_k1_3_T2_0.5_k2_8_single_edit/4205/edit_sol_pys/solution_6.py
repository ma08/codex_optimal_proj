
import sys
import itertools

def is_sorted(p):
    for i in range(1, len(p)):
        if p[i-1] > p[i]:
            return False
    return True

def main():
    N = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split()))
    for i, j in itertools.combinations(range(N), 2):  # enumerate all combinations of i,j
        if p[i] > p[j]:
            p[i], p[j] = p[j], p[i]  # swap
            if is_sorted(p):
                print("YES")
                sys.exit()
            p[i], p[j] = p[j], p[i]  # swap back
    print("NO")

if __name__ == "__main__":
    main()
