

import sys

def main():
    n = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    a = [0, 0, 0]
    for c in s:
        a[int(c)] += 1
    res = [0] * n
    for i in range(n):
        if s[i] == '1' and a[1] > a[0]:
            res[i] = '0'
            a[1] -= 1
            a[0] += 1
        elif s[i] == '2' and a[2] > a[1]:
            res[i] = '1'
            a[2] -= 1
            a[1] += 1
        else:
            res[i] = s[i]
    print(''.join(res))

if __name__ == '__main__':
    main()