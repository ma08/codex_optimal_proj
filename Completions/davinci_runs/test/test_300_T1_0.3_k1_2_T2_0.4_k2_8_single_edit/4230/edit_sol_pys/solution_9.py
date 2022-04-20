
import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = sum(a)
    if ans % n != 0:
        print(-1)
    else:
        ans = ans // n
        diff = 0
        for i in range(n):
            diff += a[i] - ans
            if diff != 0:
                print(i + 1)
                exit()
        print(0)

if __name__ == '__main__':
    main()
