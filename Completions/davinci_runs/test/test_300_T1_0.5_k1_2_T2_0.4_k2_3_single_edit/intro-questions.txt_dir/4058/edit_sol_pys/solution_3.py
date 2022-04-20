

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 1
    for i in range(n):
        if a[i] == 0:
            ans += 1
            j = i + r
            if j < n:
                a[j] = 1
            j = i - r
            if j >= 0:
                a[j] = 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
