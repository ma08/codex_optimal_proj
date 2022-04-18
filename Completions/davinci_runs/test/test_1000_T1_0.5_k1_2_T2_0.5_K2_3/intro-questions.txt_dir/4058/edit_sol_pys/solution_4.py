
def get_input():
    n, d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]  # a[i] = x_i - y_i
    return n, d, a

def solve(n, d, a):
    ans = 0
    i = 1
    while i <= n:
        if a[i-1] > 0:
            i += 1
        else:
            j = i
            while j <= n and a[j-1] < 0:
                j += 1
            a[j-1] = 1
            ans += 1
            i = j
    return ans

def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)

if __name__ == '__main__':
    main()
