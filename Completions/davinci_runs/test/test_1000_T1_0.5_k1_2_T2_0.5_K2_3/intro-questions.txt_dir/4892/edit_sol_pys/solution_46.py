

import sys

def read_input(inp):
    N = int(inp.readline())
    passwords = []
    for i in range(N):
        passwords.append(inp.readline().rstrip().split())
    return N, passwords

def solve(N, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    ans = 1
    for i in range(N):
        ans += (1 - float(passwords[i][1])) * (i + 1)
    return ans

def main():
    N, passwords = read_input(sys.stdin)
    ans = solve(N, passwords)
    print(ans)

if __name__ == '__main__':
    main()
