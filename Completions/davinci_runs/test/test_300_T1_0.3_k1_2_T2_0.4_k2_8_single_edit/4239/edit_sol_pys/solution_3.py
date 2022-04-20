import sys

def main():
    n = int(sys.stdin.readline())
    ans = 0
    while n > 0:
        if n % 6 == 0:
            n = n // 6 * 4
        elif n % 9 == 0:
            n = n // 9 * 4
        else:
            n -= 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
