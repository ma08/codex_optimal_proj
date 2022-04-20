


def main():
    n = int(input())
    x = [int(i) for i in input().split()]
    x.sort()
    d = x[1] - x[0]
    ans = [x[0]]
    for i in range(1, n):
        if x[i] - x[i-1] == d:
            ans.append(x[i])
        elif x[i] - x[i-1] == 2*d:
            continue
        else:
            d = x[i] - x[i-1]
            ans = [x[i-1], x[i]]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()