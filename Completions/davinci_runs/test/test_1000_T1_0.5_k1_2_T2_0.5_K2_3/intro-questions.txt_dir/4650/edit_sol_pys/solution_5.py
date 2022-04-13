
# this is a comment
import sys

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        cnt = 0
        i = 0
        while i < n:
            if a[i] % 3 == 0:
                cnt += 1
                i += 1
            elif i + 1 < n and a[i] % 3 == 1 and a[i + 1] % 3 == 2:
                cnt += 1
                i += 2
            elif i + 1 < n and a[i] % 3 == 2 and a[i + 1] % 3 == 1:
                cnt += 1
                i += 2
            else:
                i += 1
        print(cnt)

if __name__ == '__main__':
    sys.exit(main())
