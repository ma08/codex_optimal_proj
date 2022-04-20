
def main():
    x, k, d = map(int, input().split())
    if k * d <= x:
        print(abs(x - k * d))
    else:
        if (k - x // d) % 2 == 0:
            print(abs(x % d))
        else:
            print(d - x)

if __name__ == '__main__':
    main()
