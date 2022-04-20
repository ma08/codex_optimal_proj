

def get_input():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()] + [0]
    return n, m, a

def solve(n, m, a):
    ans = 0
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        ans += (j - i - 1) // (m + 1)
        i = j
    return ans

def main():
    n, m, a = get_input()
    ans = solve(n, m, a)
    print(ans)

if __name__ == '__main__':
    main()
