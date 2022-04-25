

def get_input():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, k, a

def solve(n, k, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            j = i
            while j < n and a[j] == 0:
                j += 1
            if j - i > 2*k:
                return -1
            if j < n:
                a[j] = 1
                ans += 1
            else:
                return -1
            i = j + 1
        else:
            i += 2
    return ans

def main():
    n, k, a = get_input()
    ans = solve(n, k, a)
    print(ans)

if __name__ == '__main__':
    main()
