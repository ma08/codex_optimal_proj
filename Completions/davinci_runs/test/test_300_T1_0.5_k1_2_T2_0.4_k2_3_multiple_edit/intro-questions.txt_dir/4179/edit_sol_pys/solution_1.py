import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    count = 0
    for i in range(m):
        if a[i] < b[i]:
            count += 1
    print(count)

if __name__ == "__main__":
    main()
