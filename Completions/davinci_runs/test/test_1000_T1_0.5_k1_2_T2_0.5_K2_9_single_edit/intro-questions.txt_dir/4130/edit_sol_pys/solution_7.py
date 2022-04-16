
import sys
readline = sys.stdin.readline

def main():
    n = int(readline())
    a = list(map(int, readline().split()))
    a.sort()
    ans = 1
    prev = a[0]
    for i in range(1, n):
        if a[i] == prev:
            prev += 1
        elif a[i] > prev + 1:
            prev = a[i] - 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
