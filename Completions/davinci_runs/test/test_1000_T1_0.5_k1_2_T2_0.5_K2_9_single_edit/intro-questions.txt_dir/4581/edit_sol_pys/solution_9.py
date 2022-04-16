

def main():
    # input
    S = input()

    # initialization
    price = 700

    # count
    for i in range(3):
        if S[i] == 'o':
            price += 100

    # output
    print(price)

if __name__ == '__main__':
    main()
