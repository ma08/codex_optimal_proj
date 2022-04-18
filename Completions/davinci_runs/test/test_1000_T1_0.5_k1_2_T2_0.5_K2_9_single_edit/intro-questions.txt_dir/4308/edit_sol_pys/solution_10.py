
def main():
    n, k = map(int, input().split())

    if n > k:
        print(n % k)
    else:
        print(0)

if __name__ == '__main__':
    main()
