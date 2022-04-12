

def main():
    # input and initialize
    S = input()  # input
    price = 700  # initialize

    # count and output
    for i in range(len(S)):  # count
        if S[i] == 'o':  # count
            price += 100  # count

    # output
    print(price)  # output

if __name__ == '__main__':
    main()
