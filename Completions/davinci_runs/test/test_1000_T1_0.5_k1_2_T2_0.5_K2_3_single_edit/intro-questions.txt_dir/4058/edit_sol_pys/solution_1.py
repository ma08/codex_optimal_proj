

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 1
    if a[0] == 0:
        ans += 1
        a[0] = 1
    while i < n:
        if a[i] == 0:
            if a[i-1] == 0:
                return -1
            ans += 1
            a[i] = 1
        else:
            i += 1
    if a[n-1] == 0:
        return -1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
