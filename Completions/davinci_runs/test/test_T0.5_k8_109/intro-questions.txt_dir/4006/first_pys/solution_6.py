

import sys

def main():
    s = sys.stdin.readline().rstrip()
    n = int(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 10 == 0:
        return 1 + main(n // 10)
    if n % 10 == 9:
        return 1 + main(n + 1)
    return 1 + main(n - 1)


if __name__ == "__main__":
    print(main())