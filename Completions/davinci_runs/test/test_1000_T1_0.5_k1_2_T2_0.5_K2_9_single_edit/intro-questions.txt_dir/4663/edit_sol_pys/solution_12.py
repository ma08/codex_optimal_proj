

import re

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        number = input()
        if re.match(r'[789]\d{9}$', number):




            print('YES')
        else:
            print('NO')
