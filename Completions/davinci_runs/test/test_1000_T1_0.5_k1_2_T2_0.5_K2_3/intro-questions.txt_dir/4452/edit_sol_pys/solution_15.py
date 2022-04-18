import sys


def main():
    n = int(sys.stdin.readline())

    ans = []
    while n > 0:
        ans.append(n % 10)
        n //= 10
    for i in range(len(ans)):
        if ans[i] == 0:
            ans[i] = 10
        else:
            ans[i] = ans[i] * (10 ** i)
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
