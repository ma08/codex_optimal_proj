

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            k = i
            while k < n and a[k] == 0:
                k += 1
            if k - i + 1 > 2*r:
                return "IMPOSSIBLE"
            if k < n:
                a[k] = 1
            ans += 1
            i = k
        else:
            i += 1
    return str(ans)

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
