

import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    cnt = 0
    for i in range(n):
        if s[i] == '1':
            cnt += 1
    print((cnt + 1) * cnt // 2)

if __name__ == '__main__':
    main()
