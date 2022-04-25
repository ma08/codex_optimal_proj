
import sys

def main():
    n, m, c = map(int, sys.stdin.readline().split())
    b = list(map(int, sys.stdin.readline().split()))
    a = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
    count = 0
    for i in range(n):
        if sum(a[j][i]*b[j] for j in range(m)) + c > 0:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
