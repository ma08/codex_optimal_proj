
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort(reverse=True)
    print(sum(a[i]*b[i] for i in range(n)))

if __name__ == "__main__":
    main()
