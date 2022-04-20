

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
    if s[0] > s[1]:
        prev_color = '1'
    else:
        prev_color = '0'
    print("YES")
    print(prev_color, end='')
    for i in range(1, n - 1):
        if s[i] <= s[i - 1]:
            if prev_color == '0':
                prev_color = '1'
            else:
                prev_color = '0'
        print(prev_color, end='')
    if s[n - 2] > s[n - 1]:
        if prev_color == '0':
            prev_color = '1'
        else:
            prev_color = '0'
    print(prev_color)

if __name__ == "__main__":
    main()