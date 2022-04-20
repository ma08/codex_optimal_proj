

def solve(n, a):
    pos = []
    neg = []
    zero = []
    for i in range(n):
        if a[i] > 0:
            pos.append(a[i])
        elif a[i] < 0:
            neg.append(a[i])
        else:
            zero.append(i)

    pos.sort()
    neg.sort()

    res = 0
    for i in range(len(pos)):
        for j in range(len(neg)):
            if pos[i] > neg[j]:
                res += 1
            else:
                break

    if len(zero) > 0:
        res += len(zero) - 1

    return res


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == "__main__":
    main()
