

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()] + [0] * (n - len(input().split()))
    return n, a

def solve(n, a):
    ans = 0
    for i in range(n):
        if a[i] == 0:
            ans += 1
            j = i
            while j <= n and a[j] == 0:
                a[j] = 1
                j += 1
    return ans

def main():
    n, a = get_input()
    ans = solve(n, a)
    print(ans)

if __name__ == '__main__':
    main()
