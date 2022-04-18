

import sys

def inp():
    return int(sys.stdin.readline())

def main():
    n = inp()
    for _ in range(n):
        s = list(sys.stdin.readline().strip())
        flag = True
        for i in range(len(s)):
            if s[i] == '1':
                s[i] = '0'
            else:
                s[i] = '1'
        for i in range(len(s)):
            if s[i] == '1':
                flag = False
        if flag:
            print("WIN")
        else:
            print("LOSE")

main()
