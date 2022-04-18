

def main():
    a, b = map(int, input().split(' '))
    m, sigma = map(int, input().split(' '))

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))


if __name__ == '__main__':
    main()
