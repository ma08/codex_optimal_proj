

def get_input():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    return n, r, a

def solve(n, r, a, i=1):
    ans = 0
    while i <= n:
        if a[i-1] == 0:
            while i <= n and a[i-1] == 0:
                i += 1
            if i - j > 2*r:
                return -1
            if i <= n:
                a[i-1] = 1
                ans += 1
            else:
                return -1
        else:
            i += 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
