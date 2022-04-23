
def solve(n, q):
    p = [0]
    for i in range(n - 1):
        if p[-1] + q[i] >= 0 and p[-1] + q[i] < n:
            p.append(p[-1] + q[i] + 1)
        else:
            print(p)
            return -1
    return p


def main():
    n = int(input())
    q = list(map(int, input().split()))
    p = solve(n, q)
    if p == -1:
        print(p)
    else:
        print(*p)


if __name__ == "__main__":
    main()
