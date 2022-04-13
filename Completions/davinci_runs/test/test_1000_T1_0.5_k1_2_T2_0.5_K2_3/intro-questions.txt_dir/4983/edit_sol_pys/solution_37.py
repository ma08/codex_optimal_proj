

def main():
    x = int(input("Enter a positive integer: "))  # take user input
    while x > 9:
        digits = [int(d) for d in str(x)]  # convert list to string
        product = 1
        for d in digits:  # iterate through list
            if d != 0:
                product *= d
        x = product
    print(x)

if __name__ == "__main__":
    main()
