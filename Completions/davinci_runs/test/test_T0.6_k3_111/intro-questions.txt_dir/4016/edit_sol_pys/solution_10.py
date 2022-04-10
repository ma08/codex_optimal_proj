
def main():
    # n, k = map(int, input().split())
    # t = input()
    t = 'aba'
    n = 3
    k = 4

    # t = 'cat'
    # n = 3
    # k = 2

    for i in range(1, n + 1):
        if k % i == 0 and k // i <= n:
            print(t[:i] * (k // i))
            return


main()
