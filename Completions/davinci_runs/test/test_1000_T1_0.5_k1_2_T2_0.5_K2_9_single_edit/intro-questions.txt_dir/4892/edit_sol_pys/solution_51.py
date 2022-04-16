
import sys

def read_input(inp):
    N = int(inp.readline())
    pwds = []
    for i in range(N):
        pwds.append(inp.readline().split())
    return N, pwds

def solve(N, pwds):
    return 0

def main():
    N, pwds = read_input(sys.stdin)
    ans = solve(N, pwds)
    print(ans)

if __name__ == '__main__':
    main()
