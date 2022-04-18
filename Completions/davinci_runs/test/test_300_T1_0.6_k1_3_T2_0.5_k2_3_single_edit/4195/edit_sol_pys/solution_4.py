
def main():
    d, n = map(int, input().split())

    if d == 0:
        print(N)
    elif d == 1:
        print(100 * N)
    else:
        print(10000 * N)

if __name__ == '__main__':
    main()
