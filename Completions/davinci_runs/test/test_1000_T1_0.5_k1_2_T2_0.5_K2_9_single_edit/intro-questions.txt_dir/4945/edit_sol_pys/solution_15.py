import sys

def main():
    a, b = map(int, sys.stdin.readline().split())
    m, sigma = map(int, sys.stdin.readline().split())

    if sigma > m:
        print(0)
    else:
        print(max(0, (m-sigma)*a + sigma*b//2))

if __name__ == '__main__':
    main()
