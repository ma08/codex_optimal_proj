

def main():
    a, b = map(int, input().split())
    m, sigma = map(float, input().split())

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))  # // is used for integer division

if __name__ == '__main__':
    main()
