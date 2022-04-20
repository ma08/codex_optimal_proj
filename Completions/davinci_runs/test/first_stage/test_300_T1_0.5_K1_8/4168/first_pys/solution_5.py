

import sys

def main():
    n = int(sys.stdin.readline())
    if n == 0:
        print('0')
        return
    ans = ''
    while n != 0:
        if n % 2 == 0:
            ans = '0' + ans
            n //= -2
        else:
            ans = '1' + ans
            if n > 0:
                n = (n - 1) // -2
            else:
                n = (n + 1) // -2
    print(ans)

if __name__ == '__main__':
    main()