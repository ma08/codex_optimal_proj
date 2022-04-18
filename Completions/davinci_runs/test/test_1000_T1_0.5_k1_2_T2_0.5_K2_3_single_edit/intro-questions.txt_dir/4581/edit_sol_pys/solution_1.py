

def main():
    # Input
    S = input()

    # Initialization
    price = 700

    # Count
    for i in range(len(S)):
        if S[i] == 'o':
            price += 100

    # Output
    print(price)

if __name__ == '__main__':
    main()
