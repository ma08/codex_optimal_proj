

def get_input():
    n, r = input().split()
    n = int(n)
    r = int(r)
    a = input().split()
    a = [int(x) for x in a]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 1
    while i < n:
        if a[i] == 0:
            j = i + r
            if j >= n:
                j = n - 1
            while j >= i and a[j] == 0:
                j -= 1
            if j == i - 1:
                return 'impossible'
            if a[i-1] == 0 and i-1 >= 0:
                a[i-1] = 1
                ans += 1 
                i -= 1
            a[j] = 1
            ans += 1
            i = j + r
        else:
            i += 1
    return str(ans)

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(str(ans))

if __name__ == '__main__':
    main()
