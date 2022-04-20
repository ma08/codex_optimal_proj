

import sys

input = sys.stdin.readline

def main():
    n = int(input().rstrip())
    s = list(input().rstrip())

    ans = 0
    prev = s[0]
    for i in range(1, n):
        if prev == s[i]:
            continue
        else:
            ans += 1
            prev = s[i]
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()