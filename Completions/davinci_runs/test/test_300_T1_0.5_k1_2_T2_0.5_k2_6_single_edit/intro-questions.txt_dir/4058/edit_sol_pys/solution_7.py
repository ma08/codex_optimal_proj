

def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    for i in range(n):
        if a[i] == 0:
            j = i+1
            while j < n and a[j] == 0:
                j += 1;
            if j - i > 2*r:
                return -1
            a[j-1] = 1
            ans += 1
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
