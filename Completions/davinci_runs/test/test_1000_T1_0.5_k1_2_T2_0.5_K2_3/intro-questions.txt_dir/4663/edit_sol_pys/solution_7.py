
import sys
import re #regular expression

if __name__ == '__main__':
    N = int(sys.stdin.readline())

    for _ in range(N):
        number = sys.stdin.readline()
        if re.match(r'[789]\d{9}$', number):
            print('YES')
        else:
            print('NO')
