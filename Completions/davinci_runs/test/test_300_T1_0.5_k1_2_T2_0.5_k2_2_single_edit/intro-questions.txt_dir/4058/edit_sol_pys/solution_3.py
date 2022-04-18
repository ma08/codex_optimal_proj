

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()] + [0]
    return n, a

def solve(n, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            if a[i+1] == 0:
                return -1
            a[i+1] = 1
            ans += 1
            i += 2
        else:
            i += 1
    return ans

def main():
    n, a = get_input()
    ans = solve(n, a)
    print(ans)

if __name__ == '__main__':
    main()
