

import sys

def main():
    n, m = map(int, input().split())
    digits = [0] * n
    for _ in range(m):
        s, c = map(int, input().split())
        digits[s-1] = c
    if digits[0] == 0 and n != 1:
        print(-1)
    else:
        print(''.join(list(map(str, digits))))

if __name__ == '__main__':
    main()