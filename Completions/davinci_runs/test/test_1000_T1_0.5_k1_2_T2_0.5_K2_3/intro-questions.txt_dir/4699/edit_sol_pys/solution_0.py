
def main():
    n, k = map(int, input().split())
    d = set(map(int, input().split()))

    for i in range(n, n+10**5):
        if not any(c in d for c in str(i)):
            print(i)
            exit()


if __name__ == '__main__':
    main()
