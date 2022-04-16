

import sys

def read_input(inp):
    N = int(inp.readline())
    pwds = []
    for i in range(N):
        pwds.append(list(map(int, inp.readline().split())))
    return N, pwds

    pwds.sort(key=lambda x: x[0])
def solve(N, pwds):
    pwds.sort(key=lambda x: x[1], reverse=True)
    ans = 1
    for i in range(N):
        ans += (1 - pwds[i][1]) * (i + 1)
    return ans

def main():
    N, pwds = read_input(sys.stdin)
    ans = solve(N, pwds)
    print(int(ans))

if __name__ == '__main__':
    main()
