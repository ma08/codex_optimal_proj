
import sys
import itertools

def main():
    N = int(sys.stdin.readline().strip())
    p = list(map(int, sys.stdin.readline().strip().split())) # p = [int(x) for x in sys.stdin.readline().strip().split()]
    for i, j in itertools.combinations(range(N), 2):
        if p[i] > p[j]:
            p[i], p[j] = p[j], p[i]
            if all(p[i] <= p[i+1] for i in range(N-1)):
                print("YES")
                sys.exit()
            p[i], p[j] = p[j], p[i]
    print("NO")

if __name__ == "__main__":
    main()
