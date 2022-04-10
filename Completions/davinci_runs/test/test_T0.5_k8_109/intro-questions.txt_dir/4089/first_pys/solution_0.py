

import sys

def main():
    input = sys.stdin.readline()
    N = int(input)
    num = 1
    i = 1
    while num < N:
        num += 26 * i
        i += 1
    num -= 26 * (i - 1)
    index = N - num
    index -= 1
    result = ''
    while index >= 0:
        result = chr(ord('a') + index % 26) + result
        index = index // 26 - 1
    print(result)

if __name__ == '__main__':
    main()