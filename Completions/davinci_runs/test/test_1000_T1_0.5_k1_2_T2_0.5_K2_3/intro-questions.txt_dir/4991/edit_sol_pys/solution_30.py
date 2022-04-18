

def hailstone(n):
    if n == 1:
        return n
    else:
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1



def main():
    n = int(input())
    print(hailstone(n))


if __name__ == '__main__':
    main()
