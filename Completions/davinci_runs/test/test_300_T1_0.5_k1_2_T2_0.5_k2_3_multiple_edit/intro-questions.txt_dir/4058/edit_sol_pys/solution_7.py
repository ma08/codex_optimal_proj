

def get_input():
    n = int(input())
    a = [int(x) for x in input().split()] + [0]
    return n, a

def solve(n, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            ans += 1
        i += 1
    return ans

def main():
    n, a = get_input()
    ans = solve(n, a)
    print(ans)

if __name__ == '__main__':
    main()
