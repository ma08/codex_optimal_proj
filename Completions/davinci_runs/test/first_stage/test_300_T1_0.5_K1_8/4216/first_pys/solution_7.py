

import sys

def main():
    n = int(sys.stdin.readline().strip())
    ans = len(str(n))
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ans = min(ans, len(str(i)))
            ans = min(ans, len(str(n // i)))
    print(ans)

if __name__ == '__main__':
    main()