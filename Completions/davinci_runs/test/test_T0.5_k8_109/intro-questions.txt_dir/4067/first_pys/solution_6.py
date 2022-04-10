

import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    s = input().strip()
    count = [0]*3
    for i in range(n):
        count[int(s[i])] += 1
    ans = [0]*n
    for i in range(n):
        if count[0] > count[1]:
            ans[i] = 1
            count[1] += 1
            count[int(s[i])] -= 1
        elif count[1] > count[2]:
            ans[i] = 2
            count[2] += 1
            count[int(s[i])] -= 1
        else:
            ans[i] = 0
            count[0] += 1
            count[int(s[i])] -= 1
    print(''.join(map(str, ans)))


if __name__ == '__main__':
    main()