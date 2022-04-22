

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    if a[0] == 0:
        return -1
    i = 1
    while i <= n:
        if a[i] == 1:
            i += 1
        else:
            if i + 2*r < n:
                i += 2*r
            elif i + r < n:
                i += r
            ans += 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
