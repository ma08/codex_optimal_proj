

def get_input():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            j = i + 1
            while j < n and a[j] == 0:
                j += 1
            if j - i > 2*r:
                return -1, a
            if j < n:
                a[j] = 1
            ans += 1
            i = j + 1
        else:
            i += 1
    return ans, a

def main():
    n, r, a = get_input()
    ans, a = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
