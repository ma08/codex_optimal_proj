
def main():
    n, a, b = [int(x) for x in input().split()]

    if b / n > a:
        print(a * n)
    else:
        print(b)

if __name__ == '__main__':
    main()
