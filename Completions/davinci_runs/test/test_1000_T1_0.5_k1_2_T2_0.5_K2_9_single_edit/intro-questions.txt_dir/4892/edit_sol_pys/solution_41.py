
import sys

def read_input(input):
    n = int(input.readline())
    passwords = []
    for i in range(n):
        passwords.append(input.readline().split())
    return n, passwords

def solve(n, passwords):
    passwords.sort(key=lambda x: x[1], reverse=True)
    ans = 1
    for i in range(N):
        ans += (1 - float(pwds[i][1])) * (i + 1)
    return ans

def main():
    N, pwds = read_input(sys.stdin)
    ans = solve(N, pwds)
    print(ans)

if __name__ == '__main__':
    main()
