
def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    for i in range(n):
        if a[i] == 1:
            continue
        if i + r >= n:
            if i + r == n and a[i+r] == 1:
                ans += 1
            else:  # i + r > n
                return -1
            continue
        if a[i+r] == 1:
            ans += 1
            continue
        if a[i+2*r] == 1:
            ans += 2
            continue
        return -1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
