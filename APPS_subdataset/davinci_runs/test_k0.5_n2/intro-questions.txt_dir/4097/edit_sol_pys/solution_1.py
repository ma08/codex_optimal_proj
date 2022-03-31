import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().strip().split()))
    a.sort()
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            print("NO")
            return
    print("YES")

if __name__ == "__main__":
    main()
