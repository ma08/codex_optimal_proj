

def solve(n, a, b):
    pos = set()
    neg = set()
    for i in range(n):
        if b[i] > 0:
            pos.add(b[i] / a[i])
        elif b[i] < 0:
            neg.add(b[i] / a[i])

    return len(pos) * len(neg)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(n, a, b))


if __name__ == "__main__":
    main()
