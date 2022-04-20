

def get_input():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, m, a

def solve(n, m, a):
    ans = 0
    i = 1
    while i <= n:
        if a[i-1] == 0:
            j = i
            while j <= n and a[j-1] == 0:
                j += 1
            if j - i + 1 > 2*m:
                return -1
            if j <= n:
                a[j-1] = 1
                ans += 1
            else:
                return -1
            i = j
        else:
            i += 1
    return ans

def main():
    n, m, a = get_input()
    ans = solve(n, m, a)
    print(ans)

if __name__ == '__main__':
    main()
