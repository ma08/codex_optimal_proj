

def main():
    a, b = map(int, input().split())  # a = 0, b = 1
    m, sigma = map(int, input().split())  # m = 2, sigma = 3

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))  # // is floor division, 1

if __name__ == '__main__':
    main()
