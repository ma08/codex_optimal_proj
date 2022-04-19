
def get_input():
    n, r = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    return n, r, a


def solve(n, r, a, i):
    ans = 0
    while i <= n:
        if a[i] == 0:
            return -1
        else:
            a[i] = 0
            ans += 1
            i += r
            if i > n:
                break
            if a[i] == 0:
                return -1
            else:
                a[i] = 0
                ans += 1
                i += r
                if i > n:
                    break
    return ans


def main():
    n, r, a = get_input()
    ans = 0
    for i in range(n):
        if a[i] == 1:
            ans += solve(n, r, a, i)
            break
    if ans == 0:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
