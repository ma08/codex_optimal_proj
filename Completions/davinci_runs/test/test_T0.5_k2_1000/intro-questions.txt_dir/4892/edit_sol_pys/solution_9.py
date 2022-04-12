#!/usr/bin/env python3

import sys

def read_input(inp):
    N = int(inp.readline())
    pwd = []
    for i in range(N):
        pwd.append(inp.readline().split())
    return N, pwd

def solve(N, pwd):
    pwd.sort(key=lambda x: x[1], reverse=True)
    ans = 1
    for i in range(N):
        ans += (1 - float(pwd[i][1])) * (i + 1)
    return ans

def main():
    N, pwd = read_input(sys.stdin)
    ans = solve(N, pwd)
    print(ans)

if __name__ == '__main__':
    main()
