
def main():
    n, a, b = [int(x) for x in input().split()]  # input

    if b / n > a:
        print(a * n)  # output
    else:
        print(b)

if __name__ == '__main__':
    main()
