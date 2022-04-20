


def main():
    n, m = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.sort()
    # print(n, m, xs)

    mvs = 0
    for i in range(m):
        # print("Start: ", xs[i], xs[i+1:])
        if i+1 < len(xs) and (xs[i+1] - xs[i]) > 1:
            # print("Move: ", xs[i], xs[i+1])
            mvs += 1
        else:
            # print("Skip: ", xs[i], xs[i+1])
            pass
    print(mvs)


if __name__ == '__main__':
    main()