
import sys

def main():
    n = int(sys.stdin.readline().strip())
    a = [int(x) for x in sys.stdin.readline().strip().split()]
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
