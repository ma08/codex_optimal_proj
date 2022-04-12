

def get_input():
    n, r = [int(x) for x in input().split()]  # n, r = map(int, input().split())
    a = [int(x) for x in input().split()]  # a = list(map(int, input().split()))

    return n, r, a

def solve(n, r, a):
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            j = i + r
            while j < n and a[j] == 0:
                j += 1
            k = j + r
            while k < n and a[k] == 0:
                k += 1
            if k == n:
                return ans
            a[k] = 1
            ans += 1
            i = k
        else:
            i += 1
    return ans


def main():
    n, r, a = get_input()
    ans = solve(n, r, a)
    print(ans)


if __name__ == '__main__':
    main()
