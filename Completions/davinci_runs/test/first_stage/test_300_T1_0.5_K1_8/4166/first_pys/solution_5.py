

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, sys.stdin.readline().split())
    for i in range(10 ** n):
        str_i = str(i)
        if len(str_i) < n:
            str_i = '0' * (n - len(str_i)) + str_i
        for j in range(m):
            if str_i[s[j] - 1] != str(c[j]):
                break
        else:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()