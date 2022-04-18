

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    ans = 0

    for i in range(1, n+1):
        s = str(i)
        digit_sum = 0
        for c in s:
            digit_sum += int(c)

        if a <= digit_sum <= b:
            ans += i

    print(ans)

if __name__ == "__main__":
    main()