
def main():
    n, k = map(int, input().split())
    s = input()

    if k > (1 << n) - 1:
        print(-1)
        return

    print(s)

main()
