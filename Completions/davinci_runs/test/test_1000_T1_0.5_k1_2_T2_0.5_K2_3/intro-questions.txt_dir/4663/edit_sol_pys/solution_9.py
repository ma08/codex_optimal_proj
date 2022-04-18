
import re

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        string = input()
        if re.match(r'^[789]\d{9}$', string):
            print('YES')
        else:
            print('NO')
