

def get_input():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    return n, r, a

def solve(n, r, a, x):
    ans = 0
    for i in range(n):
        if a[i] == 0:
            if i == 0:
                if a[i+1] == 0:
                    return -1
                else:
                    a[i] = 1
                    ans += 1
            elif i == n-1:
                if a[i-1] == 0:
                    return -1
                else:
                    a[i] = 1
                    ans += 1
            else:
                if a[i-1] == 0 and a[i+1] == 0:
                    return -1
                else:
                    a[i] = 1
                    ans += 1
    if sum(a) < x:
        return -1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a, x)
    print(ans)

if __name__ == '__main__':
    main()
