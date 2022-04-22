
def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            j = i + r
            if j >= n:
                return ans
            if a[j] == 0:
                return -1
            a[j] = 1
            ans += 1
            i = j + r
        else:
            i += 1
    return -1

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
