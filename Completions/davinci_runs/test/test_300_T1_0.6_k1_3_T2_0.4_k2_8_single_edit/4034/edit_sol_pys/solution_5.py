

import sys

def main():
    n = int(input())
    s = input()
    if n == 1:
        print("YES")
        print("0")
        return
    if n == 2:
        if s[0] <= s[1]:
            print("YES")
            print("00")
        else:
            print("YES")
            print("10")
        return
    print("YES")
    print('0', end='')
    for i in range(1, n - 1):
        if s[i] > s[i - 1]:
            print('1', end='')
        else:
            print('0', end='')
    print('0')

if __name__ == "__main__":
    main()
