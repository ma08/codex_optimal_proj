

def solve(n, k, t):
    s = ''
    while k > 0:
        s += t
        k -= 1
    return s + t[0:n-(len(s) % n)]

if __name__ == '__main__':
    n, k = map(int, input().split())
    t = input()
    print(solve(n, k, t))
