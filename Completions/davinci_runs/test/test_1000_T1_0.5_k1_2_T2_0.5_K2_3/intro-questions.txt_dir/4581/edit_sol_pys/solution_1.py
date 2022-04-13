

def main():
    # input
    S = input()

    # initialize
    price = 700

    # count
    for s in S:
        if s == 'o':
            price += 100

    # output
    print(price)

if __name__ == '__main__':
    main()
