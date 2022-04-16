

def main():
    # parse input
    S = list(input())

    # compute
    price = 700 + S.count('o') * 100

    # output
    print(price)

if __name__ == '__main__':
    main()
