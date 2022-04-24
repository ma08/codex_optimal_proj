

def get_input():
    n, r = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    return n, r, A

def solve(n, r, A):
    ans = 0
    i = 1
    while i <= n:
        if A[i-1] == 0:
            j = i
            while j <= n and A[j-1] == 0:
                j += 1
            if j - i + 1 > 2*r:
                return -1
            if j <= n:
                A[j-1] = 1
                ans += 1
            else:
                return -1
            i = j
        else:
            i += 1
    return ans

def main():
    n, r, A = get_input()
    ans = solve(n, r, A)
    print(ans)

if __name__ == '__main__':
    main()
