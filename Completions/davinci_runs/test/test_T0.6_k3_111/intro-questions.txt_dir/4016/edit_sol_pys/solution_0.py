
def main():
    n, k = map(int, input().split())
    t = input()

    # t = 'abacaba'
    # n = 7
    # k = 4

    for i in range(1, n + 1):
        if k % i == 0 and k // i <= n:
            print(t[:i] * (k // i))
            return


main()
