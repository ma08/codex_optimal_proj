

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 1
    while i <= n and ans != -1:
        if a[i-1] == 0:
            j = i
            while j <= n and a[j-1] == 0 and ans != -1:
                j += 1
            if j - i + 1 > 2*r and ans != -1:
                ans = -1
            if j <= n:
                a[j-1] = 1
                ans += 1
            else:
                ans = -1
            i = j
        else:
            i += 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
