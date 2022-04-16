import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a_max = max(a)
    b_max = max(b)

    if a_max > b_max:
        print(-1)
        return 0
    else:
        a_max = max(a)
        b_max = max(b)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                if ai > bj:
                    a.pop(i)
                    b.pop(j)
                    a.append(bj)
                    b.append(ai)

        a_max = max(a)
        b_max = max(b)
        if a_max > b_max:
            print(-1)
            return 0
        else:
            print(sum(b))
            return 0


if __name__ == '__main__':
    main()
