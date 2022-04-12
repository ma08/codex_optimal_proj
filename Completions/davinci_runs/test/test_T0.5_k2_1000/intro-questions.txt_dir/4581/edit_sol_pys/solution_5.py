

def main():
    # input and initialize
    S = input()  # input
    price = 700  # initialize

    # count and output
    for i in range(len(S)):
        if S[i] == 'o':
            price += 100

    # output
    print(price)

if __name__ == '__main__':
    main()
