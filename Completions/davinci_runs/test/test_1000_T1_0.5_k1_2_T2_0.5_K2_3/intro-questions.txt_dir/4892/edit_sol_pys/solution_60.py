

import sys

def read_input(inp):
    N = int(inp.readline())
    pwds = [None] * N
    for i in range(N):
        pwds[i] = inp.readline().split()
    return N, pwds

def solve(N, pwds):
    pwds.sort(key=lambda x:x[1], reverse=True)
    ans = 1
    for i in range(1, N):
        ans += (1 - float(pwds[i][1])) * i
    return ans

def main():
    N, pwds = read_input(sys.stdin)
    ans = solve(N, pwds)
    print(ans)

if __name__ == '__main__':
    main()
